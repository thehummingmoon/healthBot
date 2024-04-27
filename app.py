import streamlit as st
import openai

# Set up OpenAI API
openai.api_key = "your_api_key"

def generate_response(input_text):
    # Use OpenAI API to generate response
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=input_text,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    st.title('Health Bot')

    # User input
    user_input = st.text_area('Enter your health-related query:')
    if st.button('Ask'):
        if user_input:
            # Generate response
            response_text = generate_response(user_input)
            st.text_area('Response:', value=response_text, height=200)

if __name__ == '__main__':
    main()
