import streamlit as st
# import os
from service.scraping import ScrapingService

def show():
    st.header("🔍 Web Scraping")
    
    scraper = None
    
    # Data submission mechanism
    with st.form("scraping_form"):
        url = st.text_input("Website URL:", placeholder="https://example.com")
        collection_name = st.text_input("Collection name:", placeholder="my-collection")
        submitted = st.form_submit_button("Start Scraping")  # submit button
    
    if submitted and url and collection_name:
        scraper = ScrapingService()
        with st.spinner("Extracting content..."):  # loading spinner shown to the user
            result = scraper.scrape_website(url, collection_name)
            
            if result["success"]:
                st.success(f"✅ {result['files']} files saved!")
                if st.button("Go to Chat"):
                    st.rerun()
            else:
                st.error(f"❌ Error: {result['error']}")
            
    