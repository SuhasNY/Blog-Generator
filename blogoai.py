import openai
import streamlit as st

# Set up OpenAI API key (using Streamlit secrets)
openai.api_key = st.secrets["openai"]["api_key"]

# Function to generate blog content based on topic
def generate_blog(topic):
    # Formulate the prompt for OpenAI API
    prompt = f"Write a comprehensive and well-structured blog article about '{topic}'. Include an introduction, detailed sections, and a conclusion. Make sure to keep the tone engaging and informative."

    try:
        # API call to OpenAI to generate content using the new chat-based model
        response = openai.chat.Completion.create(
            model="gpt-3.5-turbo",  # You can also use "gpt-4" if you have access to GPT-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,  # You can adjust the token limit for longer articles
            temperature=0.7,  # Adjust creativity level
        )

        # Return the generated text
        return response['choices'][0]['message']['content'].strip()

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
