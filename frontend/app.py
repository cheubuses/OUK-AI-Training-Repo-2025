import streamlit as st
import requests
from dotenv import load_dotenv
import oscd



# Load environment variables
load_dotenv()
API_URL = os.getenv('JAC_API_URL', 'http://localhost:8000')

st.title('CodeBase Genius - Frontend')

# Input for GitHub repo
repo_url = st.text_input('GitHub repo URL')

# Button to generate docs
if st.button('Generate docs'):
    if not repo_url:
        st.error('Please enter a GitHub repository URL')
    else:
        with st.spinner('Requesting docs...'):
            try:
                resp = requests.post(f"{API_URL}/api/run", json={'url': repo_url})
                data = resp.json()
            except Exception:
                st.error('Invalid response from backend')
                data = None

            if data and data.get('success'):
                st.success('Docs generated')
                st.write('Docs path: ', data.get('docs_path'))
                
                # Show markdown
                path = data.get('docs_path')
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        st.markdown(f.read())
                except Exception as e:
                    st.warning(f'Could not read docs file: {e}')
            else:
                st.error('Backend failed: ' + str(data))
