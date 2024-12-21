import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')
model = ChatGroq(model="Gemma2-9b-it", api_key= groq_api_key)

sys_template = "Translate the Sentence into {language}"

prompt = ChatPromptTemplate.from_messages([
    ("system", sys_template),
    ("user", "{text}")
])

parser = StrOutputParser()
chain = prompt|model|parser

st.title('Language Translation')
Language = st.text_input('Language to be translated to')
Text = st.text_input('Word to be Translated')

result = chain.invoke({'language': Language, 'text': Text})

if st.button('Result'):
    st.success(f"The result is {result}")