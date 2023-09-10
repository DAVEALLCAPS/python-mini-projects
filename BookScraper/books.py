import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://books.toscrape.com/"

def fetch_all_category_urls():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    return [(category.a.text.strip(), BASE_URL + category.a['href']) for category in soup.select('.side_categories ul li')[1:]]  # [1:] to exclude the "Books" category

def fetch_books_from_category(category_url):
    books = []
    while category_url:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for book in soup.select('article.product_pod'):
            title = book.select_one('h3 a')['title']
            price = book.select_one('.price_color').text
            availability = book.select_one('.availability').text.strip()
            rating = book.select_one('p')['class'][1]
            books.append([title, price, availability, rating])
        
        # Handle pagination
        next_page = soup.select_one('.next a')
        category_url = category_url.rsplit('/', 1)[0] + '/' + next_page['href'] if next_page else None

    return books

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Availability", "Rating"])
        writer.writerows(data)

def main():
    categories = fetch_all_category_urls()
    
    print("Available Categories:")
    for idx, (name, _) in enumerate(categories, 1):
        print(f"{idx}. {name}")
    
    choice = input("\nEnter the number of the category you want to scrape (or press Enter to scrape all): ")
    
    all_books = []
    if not choice:
        for _, cat_url in categories:
            all_books.extend(fetch_books_from_category(cat_url))
    else:
        _, category_url = categories[int(choice) - 1]
        all_books = fetch_books_from_category(category_url)
    
    save_to_csv(all_books, "books.csv")
    print(f"\nScraped {len(all_books)} books and saved to books.csv")

if __name__ == "__main__":
    main()
