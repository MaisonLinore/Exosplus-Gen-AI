import streamlit as st
from core.engine import ExosEngine

st.set_page_config(page_title="Exos+ Gen AI", page_icon="🌐", layout="wide")

st.title("🌐 Exos+ Gen AI")
st.caption("The Sovereign Agentic AI Ecosystem | Powered by Aeterna EM+")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan riwayat chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input User
if prompt := st.chat_input("How can Exos+ assist you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        # Panggil Engine Exos+
        engine = ExosEngine()
        full_response = engine.generate_response(prompt)
        response_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
