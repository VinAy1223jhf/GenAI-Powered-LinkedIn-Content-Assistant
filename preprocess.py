import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm

def clean_text(text: str) -> str:
    # Remove invalid unicode surrogate characters
    return text.encode("utf-8", "ignore").decode("utf-8")


def process_posts(raw_file_path, processed_file_path):
    enriched_data = []
    with open(raw_file_path, encoding='utf-8') as raw_file:
        raw_posts = json.load(raw_file)

        for post in raw_posts:
            cleaned_text = clean_text(post["text"])
            metadata = extract_metadata(cleaned_text)
            post_with_metadata=post | metadata
            enriched_data.append(post_with_metadata)
        
    for epost in enriched_data:
        print(epost)

    unified_tags = get_unified_tags(enriched_data)


    for post in enriched_data:
        current_tags = post['tags']
        new_tags = {unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, 'w', encoding='utf-8') as processed_file:
        json.dump(enriched_data, processed_file, indent=4)


def get_unified_tags(enriched_data):
    unique_tags = set()
    for post in enriched_data:
        unique_tags.update(post['tags'])

    unique_tags_list = ', '.join(unique_tags)

    template = """You will be given a list of tags extracted from LinkedIn posts.
These tags are noisy, inconsistent, duplicated, and semantically overlapping.

Your task is to unify and normalize these tags based on the rules below.

RULES:

1. Merge semantically similar tags into a single unified tag.
   Infer mappings based on meaning, not exact spelling.

   Examples (non-exhaustive):
   - "Job", "Jobs", "Job Search", "Job Hunting", "Jobseekers" → "Job Search"
   - "Career", "Career Advice" → "Career"
   - "Motivation", "Inspiration", "Hope", "SelfCare" → "Motivation"
   - "Personal Growth", "Self Improvement", "Self-Improvement" → "Self Improvement"
   - "Mental Health", "Anxiety", "Burnout" → "Mental Health"
   - "Scam", "Scams", "Fraud", "Recruiters Scam" → "Scams"
   - "Leadership", "ToxicManager", "Management" → "Leadership"
   - "Workplace", "Toxic Workplace", "Toxic Environment", "Workplace Culture" → "Workplace Culture"
   - "Influencer", "PersonalBrand", "Personal Branding" → "Personal Branding"
   - "Humor", "Sarcasm" → "Humor"
   - "LinkedIn", "Success Stories" → "LinkedIn"

2. Unified tags must:
   - Be concise
   - Use Title Case
   - Represent one clear core concept

3. Preserve semantic intent.
   - Do NOT merge unrelated ideas.
   - Do NOT invent new tags unless necessary.

4. Output format rules (VERY IMPORTANT):
   - Output ONLY a valid JSON object
   - No explanations
   - No markdown
   - No comments
   - No extra text

5. The JSON must map EACH ORIGINAL TAG to EXACTLY ONE unified tag.

Example output format:
{{
  "Job": "Job Search",
  "Job Hunting": "Job Search",
  "Self-Improvement": "Self Improvement",
  "Scams": "Scams"
}}

Here is the list of tags:
{tags}
"""



    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({'tags': str(unique_tags_list)})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException(f"Failed to parse unified tags from LLM response")
    
    return res


# now we need to soke some information from the post(which is a basic text) like number of lines, language, tags etc and add it to the post dictionary
def extract_metadata(post):
    # Placeholder for metadata extraction logic
    prompt = '''
    You are an expert content analyzer. Given the following text, extract the following metadata:
    1. Line Count: The number of lines in the text.
    2. Language: The primary language of the text.
    3. Tags: A list of relevant tags that describe the content.
    Return the metadata in JSON format. No preamble.
    Json object should hae exactly three keys: line_count, language, tags
    Language should be a single word like English or Hinglish(if it is a mix of Hindi and English)
    Tags is n array of text tags. Dont extract more than 3 tags.
    Here is the actual post on which you need to extract metadata:
    {post}
    '''

    pt = PromptTemplate.from_template(prompt)
    chain = pt | llm
    response = chain.invoke({'post': post})


    json_parser = JsonOutputParser()
    res = json_parser.parse(response.content)
    
    return res

if __name__ == "__main__":
    # process_posts("data/raw_posts_muskan_handa.json", "data/processed_posts_muskan_handa.json") 
    process_posts("data/raw_posts_ankur_warikoo.json", "data/processed_posts_ankur_warikoo.json")