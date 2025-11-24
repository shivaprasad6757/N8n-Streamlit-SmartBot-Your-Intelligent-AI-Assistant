import streamlit as st
import requests

st.title("🤖SmartBot–Your Intelligent AI Assistant")
st.subheader(":blue[Feel Free to ask any type of Questions]")

if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

prompt = st.chat_input("Write your Query")

if prompt:
    st.session_state["conversation"].append({"role": "user", "data": prompt})
    
    response = requests.post(
        url="https://shivan8n12.app.n8n.cloud/webhook-test/9a95d7e1-dce0-41fd-8bf9-e1c634a53d12",
        json={"prompt": prompt}
    )

    if response.status_code == 200:
        st.session_state["conversation"].append(
            {"role": "ai", "data": response.json()["output"]}
        )

for con in st.session_state["conversation"]:
    with st.chat_message(con["role"]):
        st.write(con["data"])
