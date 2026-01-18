import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from post_generator import rewrite_post


# Options
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    col1, col2 = st.columns([1, 10])

    with col1:
        st.image("linkedin.jpg", width=60)

    with col2:
        st.subheader("LinkedIn Post Generator using Gen AI")




    fs = FewShotPosts()

    mode = st.radio(
        "Choose Mode",
        options=["Generate New Post", "Rewrite My Post"]
    )


    # Creator selection
    selected_creator = st.selectbox(
        "Select Creator",
        options=list(fs.creator_data.keys())
    )

    if mode == "Rewrite My Post":
        user_post = st.text_area(
            "Paste your LinkedIn post here",
            height=200,
            placeholder="Paste your draft LinkedIn post..."
        )
        language_options = ["English", "Hinglish"]
        language = st.selectbox("Select Language", options=language_options)
        if st.button("Generate"):
            st.subheader("Rewritten Post:")
            rewritten_post = rewrite_post(
                user_post,
                length=fs.categorize_length(len(user_post.splitlines())),
                language=language,
                creator=selected_creator
            )
            st.write(rewritten_post)
            return
        
    else:
        # Get creator-specific tags
        tags = sorted(fs.get_tags(selected_creator))

        # Layout
        col1, col2, col3 = st.columns(3)
        language_options = ["English", "Hinglish"]
        with col1:
            selected_tag = st.selectbox("Topic", options=tags)

        with col2:
            selected_length = st.selectbox("Length", options=length_options)

        with col3:
            selected_language = st.selectbox("Language", options=language_options)

        # Generate
        if st.button("Generate"):
            post = generate_post(
                selected_length,
                selected_language,
                selected_tag,
                selected_creator
            )
            st.write(post)

if __name__ == "__main__":
    main()
