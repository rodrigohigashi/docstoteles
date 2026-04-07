import os
import requests
from firecrawl.v1 import V1FirecrawlApp # pra fazer o web scraping

class ScrapingService:
    def __init__(self):             # 2 propriedades
        self.api_key = os.getenv("FIRECRAWL_API_KEY")
        self.api_url = os.getenv("FIRECRAWL_API_URL")

        self.app = V1FirecrawlApp(api_key=self.api_key, api_url=self.api_url)
    
    def scrape_website(self, url, collection_name):
        """Scraping completo em uma função"""
        try:
            # 1. Mapear URLs - CORREÇÃO AQUI
            map_result = self.app.map_url(url)      # verificar todos os sublinks nessa página
            
            # O map_result é um objeto MapResponse, não um dict
            # Vamos acessar os links diretamente
            if hasattr(map_result, 'links'):        # links estão dentro da raíz?      
                links = map_result.links
            elif hasattr(map_result, 'data') and hasattr(map_result.data, 'links'):     # verifica o atributo data e    
                links = map_result.data.links[:10]  # caso contrário, pegar apenas 10 desses links
            else:
                # Se não conseguir acessar, tentar como dict (fallback)
                links = getattr(map_result, 'links', [])[:10]
            
            if not links:
                raise Exception("Nenhum link encontrado!")
            
            print(f"Encontrados {len(links)} links")
            
            # 2. Fazer scraping - CORREÇÃO: batch_scrape_urls só aceita 1 argumento
            scrape_result = self.app.batch_scrape_urls(links)
            
            # 3. Extrair dados do resultado
            if hasattr(scrape_result, 'data'):      # verifica se existe o atributo data
                scraped_data = scrape_result.data   # se existir, é definida aqui
            else:
                scraped_data = scrape_result.get("data", []) if hasattr(scrape_result, 'get') else []
                                                    # caso contrário, vai pegar 
            # 4. Salvar arquivos
            collection_path = f"data/collections/{collection_name}"
            os.makedirs(collection_path, exist_ok=True)
            
            saved_count = 0
            for i, page in enumerate(scraped_data, 1):  # primeira validação
                # Acessar markdown do objeto page
                if hasattr(page, 'markdown') and page.markdown:     # se dentro de página contém markdown e página não é nulo
                    markdown_content = page.markdown                # define markdown dentro da página
                elif hasattr(page, 'data') and hasattr(page.data, 'markdown'):  # verifica data dentro de page e se markdown tá dentro de data
                    markdown_content = page.data.markdown
                elif isinstance(page, dict) and page.get("markdown"):   # verifica se page é dicionário e se consegue pegar markdown dentro de page
                    markdown_content = page["markdown"]
                else:
                    continue        # ignora e segue adiante
                
                with open(f"{collection_path}/{i}.md", "w", encoding="utf-8") as f:
                    f.write(markdown_content)
                saved_count += 1
            
            return {"success": True, "files": saved_count}  # informa o número de arquivos encontrados e o número de arquivos salvos
            
        except Exception as e:
            print(f"Erro no scraping: {str(e)}")
            return {"success": False, "error": str(e)} 