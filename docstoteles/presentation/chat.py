import streamlit as st
from service.rag import RAGService

def show():
    st.header("💬 Chat with Documentation")
    
    if "collection" not in st.session_state or not st.session_state.collection:
        st.warning("Select a collection in the sidebar to get started.")
        return
    
    st.info(f"📂 **Active collection:** {st.session_state.collection}")

    # Só carrega se ainda não carregou, ou se a coleção mudou
    if "rag" not in st.session_state or st.session_state.get("loaded_collection") != st.session_state.collection:
        with st.spinner("Loading collection..."):
            rag = RAGService()
            loaded = rag.load_collection(st.session_state.collection)
            if not loaded:
                st.error("Could not load the selected collection.")
                return
            st.session_state.rag = rag
            st.session_state.loaded_collection = st.session_state.collection

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    with st.form("chat_form"):
        question = st.text_input("Ask something about the documentation:")
        submitted = st.form_submit_button("Send")

    if submitted and question:
        with st.spinner("Consulting AI..."):
            answer = st.session_state.rag.ask_question(question)
            st.session_state.messages.append((question, answer))
    
    st.divider()
    st.subheader("History")
    for q, a in st.session_state.messages[::-1]:
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Docstoteles:** {a}")