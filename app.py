from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "qnachatbot")

# Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the questions asked."),
    ("user", "Question: {question}")
])

def generate_response(question, model_name="gemma2:2b"):
    try:
        llm = Ollama(model=model_name)
        chain = prompt_template | llm | StrOutputParser()
        return chain.invoke({"question": question})
    except Exception as e:
        return f"\u26a0\ufe0f Error: {str(e)}"
    
# This function takes the user’s question.

# Connects to an AI model (like "gemma2:2b") via Ollama.

# Uses LangChain's "chain" to structure the prompt → run the model → parse the output.

# Returns the model’s answer or an error if something goes wrong.



# Streamlit Page Configuration
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #f7f7f8; padding: 2rem; }
    .stChatMessage { padding: 1.5rem; border-radius: 0.75rem; margin-bottom: 1.5rem; box-shadow: 0 1px 2px rgba(0,0,0,0.1); }
    .stChatMessage[data-testid="stChatMessage"] { background-color: #black; border: 1px solid #e5e5e5; }
    .stChatInput { position: fixed; bottom: 0; left: 0; right: 0; padding: 1.5rem; background-color: #ffffff; border-top: 1px solid #e5e5e5; box-shadow: 0 -2px 10px rgba(0,0,0,0.05); }
    .css-1d391kg { background-color: #ffffff; }
    h1 { color: #1f1f1f; font-size: 2rem !important; font-weight: 600 !important; margin-bottom: 2rem !important; }
    .stButton button { background-color: #10a37f; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.5rem; font-weight: 500; }
    .stButton button:hover { background-color: #0d8c6d; }
</style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.markdown("""<div style='text-align: center; padding: 1rem;'><h2>Settings</h2></div>""", unsafe_allow_html=True)

    available_models = ["gemma2:2b", "llama3", "mistral"]
    model_name = st.selectbox("Select Model", available_models, help="Choose the AI model to use for generating responses")

    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    if st.button("Download Chat History", use_container_width=True):
        chat_log = "\n\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.messages])
        st.download_button("Download", chat_log, file_name="chat_history.txt")

# Header
st.markdown("""<div style='text-align: center; padding: 1rem;'>
<h1>AI Chat Assistant 🤖</h1>
<p style='color: #666; font-size: 1.1rem;'>Your intelligent conversation partner</p>
</div>""", unsafe_allow_html=True)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt, model_name)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
