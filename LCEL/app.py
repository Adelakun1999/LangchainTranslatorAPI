import streamlit as st 
import os 
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

model = ChatGroq(model="llama3-8b-8192", groq_api_key=groq_api_key)


prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are an helpful AI assistant. please help to answer the question to the best of your ability '),
        ('user','{text}')
    ]
)

parser = StrOutputParser()
chain = prompt|model|parser

st.set_page_config(
    page_title= 'Your Custom Assistant',
    page_icon= '🤖')

st.sidebar.title('Question and Answer Chatbot')


if 'conversation' not in st.session_state :
    st.session_state.conversation = []

with st.sidebar : 
    text = st.text_input('Enter the question to be asked')
    result = chain.invoke({ 'text':text})
    button = st.button('Generate Answer')

    if button : 
        st.success(f'The result is {result}')
        st.session_state.conversation.append(('user',text))
        st.session_state.conversation.append(('assistant',result))



st.title('Conversation')
for role, message in st.session_state.conversation:
    if role == 'user':
        st.write(f"**You:** {message}")
    else:
        st.write(f"**Assistant:** {message}")






