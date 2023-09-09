import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "http://quotes.toscrape.com/"

def get_quotes_from_page(url):
    """Fetch quotes from a given page URL"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract quotes
    quotes_divs = soup.find_all("div", class_="quote")
    quotes = []
    for quote_div in quotes_divs:
        quote_text = quote_div.find("span", class_="text").text
        author = quote_div.find("small", class_="author").text
        tags = [tag.text for tag in quote_div.find_all("a", class_="tag")]
        quotes.append({
            "quote": quote_text,
            "author": author,
            "tags": tags
        })
    return quotes

def scrape_all_quotes(base_url):
    """Scrape quotes from all pages of the website"""
    quotes = []
    page_url = base_url
    while True:
        print(f"Scraping quotes from: {page_url}")
        quotes_on_page = get_quotes_from_page(page_url)
        if not quotes_on_page:
            break
        quotes.extend(quotes_on_page)
        
        # Check for next page
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_button = soup.find("li", class_="next")
        if next_button:
            page_url = urljoin(BASE_URL, next_button.a["href"])
        else:
            break

    return quotes

if __name__ == "__main__":
    all_quotes = scrape_all_quotes(BASE_URL)
    
    # Save to quotes.txt file with UTF-8 encoding
    with open("quotes.txt", "w", encoding="utf-8") as file:
        for idx, quote_info in enumerate(all_quotes, 1):
            quote_str = f"{idx}. {quote_info['quote']} - {quote_info['author']}\n"
            quote_str += f"Tags: {', '.join(quote_info['tags'])}\n"
            quote_str += '-' * 80 + "\n"
            file.write(quote_str)
            