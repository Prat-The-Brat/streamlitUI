import streamlit as st
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from streamlit_chat import message

from dotenv.main import load_dotenv
import os

load_dotenv()
key = os.environ['KEY']

db = SQLDatabase.from_uri(
    "postgresql://dykrojjj:x0tLUyYZUdP3jmM4borqLnMMH2S-Lc7q@trumpet.db.elephantsql.com/dykrojjj")
llm = OpenAI(openai_api_key=key, temperature=0)
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

st.title("🏳️ WHITE APP")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}]

with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])
    user_input = a.text_input(
        label="Your message:",
        placeholder="What would you like to say?",
        label_visibility="collapsed",
    )
    b.form_submit_button("Send", use_container_width=True)

    if user_input:
        st.session_state.messages.append(
            {"role": "user", "content": user_input})

        response = db_chain.run(user_input)

        st.session_state.messages.append(
            {"role": "assistant", "content": response})

# Display chat messages
for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user")
