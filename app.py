import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="Chat Agent", page_icon="🤖")
st.title("Chat Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=st.secrets["GOOGLE_API_KEY"],
        convert_system_message_to_human=True
    )
    
    response = llm.invoke([HumanMessage(content=prompt)])

    st.session_state.messages.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)