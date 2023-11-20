# Cryptocurrency Data Scraping Script Documentation

# Overview
This Python script is a tool for scraping cryptocurrency data from CoinMarketCap. It extracts information about the top 50 cryptocurrencies listed on the site, including their ID, name, symbol, current price in USD, market cap in USD, and 24-hour trading volume in USD. The data is then inserted into a PostgreSQL database and exported to a CSV file.

# Requirements
Python 3.x
Libraries: pandas, sqlalchemy, psycopg2, playwright
PostgreSQL server running with a database and a table named crypto
Access to the internet to scrape data from CoinMarketCap

# Installation

1. Install required Python libraries:
`pip install pandas sqlalchemy psycopg2 playwright`

2. Install Playwright browsers:
`playwright install`

# Configuration
1. Set up a PostgreSQL database named postgres with a user postgres and password postgres.
2. Create a table named crypto with appropriate fields (id, name, symbol, price_usd, market_cap_usd, volume_24h_usd).

# Usage
1. Run the script using Python:
`python script.py`

2. The script will launch a browser, navigate to CoinMarketCap, scrape data, insert it into the PostgreSQL database, and then save it to a CSV file named scraping_data.csv.


# Functionality
1. Web Scraping: Uses Playwright to scrape cryptocurrency data from CoinMarketCap.
2. Data Storage: Inserts scraped data into a PostgreSQL database.
3. Data Export: Exports the entire content of the crypto table from the database to a CSV file.

# Important Notes
1. The script scrapes data in real-time, so an internet connection is required.
2. Ensure that the CoinMarketCap website structure has not changed, as it could affect the script's XPath queries.
3. The script is configured for educational purposes and should be used responsibly with respect to web scraping ethics and legality.

# License
This script is provided for educational purposes. Users are responsible for ensuring they comply with CoinMarketCap's terms of service and legal regulations regarding web scraping and data use.
