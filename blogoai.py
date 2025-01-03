import openai
import streamlit as st

# Set up OpenAI API key (replace with your own key)
openai.api_key = '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'

# Function to generate blog content based on topic
def generate_blog(topic):
    # Formulate the prompt for OpenAI API
    prompt = f"Write a comprehensive and well-structured blog article about '{topic}'. Include an introduction, detailed sections, and a conclusion. Make sure to keep the tone engaging and informative."

    try:
        # API call to OpenAI to generate content
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another model like GPT-4
            prompt=prompt,
            max_tokens=1500,  # You can increase the token limit for longer articles
            temperature=0.7,  # Adjust creativity level
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        # Return the generated text (remove extra whitespace)
        return response.choices[0].text.strip()

    except Exception as e:
        # Handle errors (e.g., API errors)
        st.error(f"Error generating content: {e}")
        return None

# Streamlit UI
def main():
    st.title("Blog/Article Generator")

    st.write(
        """
        This app allows you to generate a blog or article on a given topic. 
        Just enter a topic, and the app will create a well-structured blog/article 
        with an introduction, body, and conclusion.
        """
    )

    # Input field for the user to provide the blog topic
    topic = st.text_input("Enter the topic for the blog/article:")

    # Button to trigger the generation of the blog
    if st.button("Generate Blog"):
        if topic:
            st.write("Generating your blog/article...")
            # Generate blog content
            blog_content = generate_blog(topic)
            if blog_content:
                st.subheader("Generated Blog Article:")
                st.write(blog_content)
        else:
            st.warning("Please enter a topic to generate a blog.")

    # Add a section for information or feedback
    st.write(
        """
        ### How it works:
        1. Enter a topic in the input box above.
        2. Click the "Generate Blog" button.
        3. The app will use OpenAI's language model to create a detailed blog/article on the topic.
        
        ### Notes:
        - The length of the article depends on the topic and available tokens.
        - You can adjust the length and tone of the article by modifying parameters in the code.
        """
    )

    # Footer with additional resources or contact info
    st.write("Made with ❤️ using OpenAI and Streamlit")

if __name__ == "__main__":
    main()
