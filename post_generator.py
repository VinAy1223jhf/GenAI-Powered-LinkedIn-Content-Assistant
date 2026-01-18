from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def sanitize_text(text: str) -> str:
    if not isinstance(text, str):
        return text
    return text.encode("utf-8", "ignore").decode("utf-8")


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"

def rewrite_post(user_post, length, language, creator):
    user_post = sanitize_text(user_post)
    prompt = f"""
    Rewrite the LinkedIn post below in the writing style of {creator}.
    Do NOT change the core message of the original post.
    Improve clarity, flow, and engagement.
    No preamble.

    Language: {language}
    Length: {get_length_str(length)}
    Original Post:
    {user_post}
    """

    examples = few_shot.get_filtered_posts(
        length=length,
        language=language,
        tag=None,  # just to get some examples
        creator=creator
    )

    if len(examples) > 0:
        prompt += "\n\nUse the writing style from the following examples:\n"

    for i, post in enumerate(examples):
        post_text = sanitize_text(post["text"])
        prompt += f"\n\nExample {i+1}:\n{post_text}"

        if i == 2:
            break
    

    response = llm.invoke(prompt)
    return sanitize_text(response.content)


def generate_post(length, language, tag, creator):
    prompt = get_prompt(length, language, tag, creator)
    response = llm.invoke(prompt)
    return sanitize_text(response.content)


def get_prompt(length, language, tag, creator):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
    # prompt = prompt.format(post_topic=tag, post_length=length_str, post_language=language)
    # few_shot = FewShotPosts()
    examples = few_shot.get_filtered_posts(length, language, tag, creator)
    
    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples. Keep the post in different paragraphs as shown in the examples. Use emojis as per the examples."

    for i, post in enumerate(examples):
        post_text = sanitize_text(post["text"])
        prompt += f"\n\nExample {i+1}:\n{post_text}"

        if i == 2:
            break

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health"))