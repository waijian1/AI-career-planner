from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# Scrape website (for running as a plain .py script)
def scrape_website_sync(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
 
        page.goto(url)
        content = page.content()
 
        browser.close()
        return content
 
 
def summarize_content_sync(url):
    html_content = scrape_website_sync(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    summary_text = soup.get_text(separator=' ', strip=True)
    return summary_text
 
if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    print(summarize_content_sync(url))
 