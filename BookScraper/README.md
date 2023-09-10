# BookstoreScraper 📚

A simple practice scraper tool that fetches and compiles book details from [books.toscrape.com](https://books.toscrape.com/).

## Description

Simple script to scrape [books.toscrape.com](https://books.toscrape.com/) and gather detailed information about a wide range of books across various categories. The extracted details, including the title, price, availability, and rating, are neatly organized and stored in a CSV file for easy access and future reference.

## Features

- **Category-wise Scraping**: Allows users to select a specific category or scrape all categories.
- **Pagination Handling**: Seamlessly fetches books from multiple pages within a category.
- **Detailed Extraction**: Each book's title, price, availability, and rating are meticulously extracted.
- **CSV File Storage**: Automatically saves the fetched book details in a structured format to a CSV file.
- **Built with BeautifulSoup**: Utilizes the power and flexibility of BeautifulSoup for web scraping.

## Setup

1. Install the required libraries:

   ```
   pip install requests beautifulsoup4
   ```

## Usage

After setting up, navigate to the directory containing the script:

1. Run the BookstoreScraper:

   ```
   python books.py
   ```

2. Follow the on-screen prompts to select a category.
3. Once the script completes, check the generated `books.csv` file for all the scraped book details.
