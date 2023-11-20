from psycopg2.extras import execute_values
import psycopg2
from playwright.sync_api import sync_playwright
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://coinmarketcap.com/')

        # scrolling down
        for i in range(6):
            page.mouse.wheel(0,500)
            page.wait_for_timeout(2000)

        trs_xpath = "//table[@class='sc-66133f36-3 etbEmy cmc-table  ']/tbody/tr"
        trs_list = page.query_selector_all(trs_xpath)

        master_list = []

        for tr in trs_list[:50]:           
            coin_dict = {}
            tds = tr.query_selector_all('td')
            if tds:
                coin_dict['id'] = tds[1].inner_text() if len(tds) > 1 else None
                coin_dict['name'] = tds[2].query_selector("//p[@color='text']").inner_text()
                coin_dict['symbol'] = tds[2].query_selector("//p[@color='text3']").inner_text()
                coin_dict['price_usd'] = float(tds[3].inner_text().replace('$', '').replace(',', ''))
                coin_dict['market_cap_usd'] = int(tds[7].inner_text().replace('$', '').replace(',', ''))
                coin_dict['volume_24h_usd'] = int(tds[8].query_selector('//p[@color="text"]').inner_text().replace('$', '').replace(',', ''))

            master_list.append(coin_dict)
        
        # creating tuple
        list_of_tuples = [tuple(dic.values()) for dic in master_list]
            
        pgconn = psycopg2.connect(
            host = 'localhost',
            database = 'postgres',
            user = 'postgres',
            password = 'postgres'
        )
        
        pgcursor = pgconn.cursor()
        execute_values(pgcursor,
                       "INSERT INTO crypto (id, name, symbol, price_usd, market_cap_usd, volume_24h_usd) VALUES %s",
                       list_of_tuples)
        
        pgconn.commit()
        pgcursor.close()
        pgconn.close()
        browser.close()
        
        # Query the database again to get the updated data
        df = pd.read_sql_query('SELECT * FROM crypto', engine)
        df.to_csv('scraping_data.csv', index=False)

        engine.dispose()

if __name__ == '__main__':
    main()
