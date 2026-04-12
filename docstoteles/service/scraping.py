import os
import requests
from firecrawl.v1 import V1FirecrawlApp  # used to perform web scraping

class ScrapingService:
    def __init__(self):  # initialize 2 properties
        self.api_key = os.getenv("FIRECRAWL_API_KEY")
    #    self.api_url = os.getenv("FIRECRAWL_API_URL")

        self.app = V1FirecrawlApp(api_key=self.api_key)
    #    self.app = V1FirecrawlApp(api_key=self.api_key, api_url=self.api_url)

    def scrape_website(self, url, collection_name):
        """Complete scraping process in a single function"""
        try:
            # 1. Map URLs
            map_result = self.app.map_url(url)  # checks all sublinks on this page
            
            # map_result is a MapResponse object, not a dict
            # so we access links directly
            if hasattr(map_result, 'links'):      
                links = map_result.links[:30]
            elif hasattr(map_result, 'data') and hasattr(map_result.data, 'links'):
                links = map_result.data.links[:10]  
            else:
                # fallback in case the structure is different
                links = getattr(map_result, 'links', [])[:10]
            
            if not links:
                raise Exception("No links found!")
            
            print(f"Found {len(links)} links")
            
            # 2. Run scraping
            scrape_result = self.app.batch_scrape_urls(links)
            
            # 3. Extract data from the result
            if hasattr(scrape_result, 'data'):
                scraped_data = scrape_result.data
            else:
                scraped_data = scrape_result.get("data", []) if hasattr(scrape_result, 'get') else []
            
            # 4. Save files
            collection_path = f"data/collections/{collection_name}"
            os.makedirs(collection_path, exist_ok=True)
            
            saved_count = 0
            for i, page in enumerate(scraped_data, 1):
                # access markdown content from each page
                if hasattr(page, 'markdown') and page.markdown:
                    markdown_content = page.markdown
                elif hasattr(page, 'data') and hasattr(page.data, 'markdown'):
                    markdown_content = page.data.markdown
                elif isinstance(page, dict) and page.get("markdown"):
                    markdown_content = page["markdown"]
                else:
                    continue
                
                with open(f"{collection_path}/{i}.md", "w", encoding="utf-8") as f:
                    f.write(markdown_content)
                saved_count += 1
            
            return {"success": True, "files": saved_count}
            
        except Exception as e:
            print(f"Scraping error: {str(e)}")
            return {"success": False, "error": str(e)}