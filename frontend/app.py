import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OPENAI_API_KEY not found in .env file.")
    st.stop()

st.title("CodeBase Genius")
st.subheader("AI-Powered Code Documentation Generator")

# File uploader
uploaded_file = st.file_uploader("Upload your code file", type=['py', 'js', 'java'])

if uploaded_file:
    # Read file content
    content = uploaded_file.read().decode()
    
    # Display code
    st.code(content, language='python')

    # Generate documentation button
    if st.button("Generate Documentation"):
        with st.spinner("Analyzing code..."):
            try:
                # Pass the API key in headers for security
                response = requests.post(
                    "http://localhost:8000/generate-docs",
                    headers={"Authorization": f"Bearer {openai_api_key}"},
                    json={"code": content}
                )
                response.raise_for_status()

                # Display results
                doc = response.json().get("documentation", "No documentation returned.")
                st.success("Documentation generated!")
                st.markdown(doc)
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
