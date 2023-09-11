from collections import namedtuple
import altair as alt
import math
import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents import AgentType
from langchain.callbacks import StreamlitCallbackHandler

load_dotenv()

llm = OpenAI(temperature=0, streaming=True, open_api_key=os.getenv('OPENAI_API_KEY'))
tools = Tool(
     ["ddg-search",]
) 
agent = initialize_agent(
     tools=tools,
     llm=llm,
     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)


# STREAMLIT
st.set_page_config(page_title="Chatbot", page_icon=":tada:", layout="wide")

#  streamlit run streamlit_app.py
st.title("ChatBot")

# st.chat_input(placeholder="Your message", disabled=False, on_submit=None, args=None, kwargs=None)
prompt = st.chat_input()
if prompt:
     st.chat_message("user").write(prompt)
     with st.chat_message("assistant"):
          st.write("thinking......")
          st_callback = StreamlitCallbackHandler(st.container())
          response = agent.run(prompt, callbacks=[st_callback])
          st.write(response)