import streamlit as st
# import os
from service.scraping_pt import ScrapingService

def show():
    st.header("🔍 Web Scraping")
    
    # mecanismo de envio de dados
    with st.form("scraping_form"):
        url = st.text_input("URL do site:", placeholder="https://exemplo.com")              
        collection_name = st.text_input("Nome da coleção:", placeholder="minha-colecao")    
        submitted = st.form_submit_button("Iniciar Scraping")                               # botão de envio
    
    if submitted and url and collection_name:
        scraper = ScrapingService()
        with st.spinner("Extraindo conteúdo..."):       # rodinha que mostra pro usuário que é pra aguardar
            result = scraper.scrape_website(url, collection_name)   
            
            if result["success"]:
                st.success(f"✅ {result['files']} arquivos salvos!")
                if st.button("Ir para Chat"):
                    st.rerun()
            else:
                st.error(f"❌ Erro: {result['error']}")
            
