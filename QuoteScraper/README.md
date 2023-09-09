# QuoteScraper 📜

A simple practice scraper tool that fetches and compiles quotes from [quotes.toscrape.com](http://quotes.toscrape.com/).

## Description

Simple script to scrape [quotes.toscrape.com](http://quotes.toscrape.com/) and gather an assortment of inspiring and thought-provoking quotes. The extracted quotes, along with their respective authors and tags, are neatly organized and stored in a text file for easy access and future reference.

## Features

- **Comprehensive Scraping**: Fetches quotes from multiple pages seamlessly.
- **Detailed Extraction**: Each quote is accompanied by its author and associated tags.
- **Text File Storage**: Automatically saves the fetched quotes in a structured format to a text file.
- **Built with BeautifulSoup**: Utilizes the power and flexibility of BeautifulSoup for web scraping.

## Setup

1. Install the required libraries:

   ```
   pip install requests beautifulsoup4
   ```

## Usage

After setting up, navigate to the directory containing the script:

1. Run the QuoteScraper:

   ```
   python quotes.py
   ```

2. Once the script completes, check the generated `quotes.txt` file for all the scraped quotes.
