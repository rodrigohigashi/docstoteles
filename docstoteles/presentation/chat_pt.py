import streamlit as st
from service.rag import RAGService

def show():
    st.header("💬 Chat com Documentação")
    
    if "collection" not in st.session_state or not st.session_state.collection:
        st.warning("Selecione uma coleção na barra lateral para começar.")
        return
    
    # Mostra a coleção ativa
    st.info(f"📂 **Coleção ativa:** {st.session_state.collection}")

    # Só carrega se ainda não carregou, ou se a coleção mudou
    if "rag" not in st.session_state or st.session_state.get("loaded_collection") != st.session_state.collection:
        with st.spinner("Carregando coleção..."):
            rag = RAGService()
            loaded = rag.load_collection(st.session_state.collection)
            if not loaded:
                st.error("Não foi possível carregar a coleção selecionada.")
                return
            st.session_state.rag = rag
            st.session_state.loaded_collection = st.session_state.collection

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    with st.form("chat_form"):
        question = st.text_input("Pergunte algo sobre a documentação:")
        submitted = st.form_submit_button("Enviar")

    if submitted and question:
        with st.spinner("Consultando IA..."):
            answer = st.session_state.rag.ask_question(question)
            st.session_state.messages.append((question, answer))
    
    st.divider()
    st.subheader("Histórico")
    for q, a in st.session_state.messages[::-1]:
        st.markdown(f"**Você:** {q}")
        st.markdown(f"**Docstóteles:** {a}")