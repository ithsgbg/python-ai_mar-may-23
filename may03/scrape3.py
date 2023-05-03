import requests_html
from bs4 import BeautifulSoup
import time

url = 'https://www.avanza.se/marknadsoversikt.html'

session = requests_html.HTMLSession()

with open('./may03/avanza.csv', 'w', encoding='utf-8') as csv_file:
    csv_file.write('id,time,change_percent,last_price\n')

for i in range(10):
    # Get page content
    result = session.get(url)

    # Render the page
    result.html.render()

    # Create a bs4 parser for the page
    soup = BeautifulSoup(result.html.html, 'html.parser')

    # Find the right tr
    tr = soup.find('tr', {'data-oid': '334593', 'data-delayed': 'true'})

    # Get the change percent value
    change_percent = tr.find('td', {'class': 'changePercent'}).text.strip()
    change_percent = change_percent.replace(',', '.')
    change_percent = float(change_percent)

    # Get the last price
    last_price = tr.find('td', {'class': 'lastPrice'}).text.strip()
    last_price = last_price.replace('\xa0', '').replace(',', '.')
    last_price = float(last_price)

    # Get updated time stamp
    updated = tr.find('td', {'class': 'updated'}).text.strip()

    with open('./may03/avanza.csv', 'a', encoding='utf-8') as csv_file:
        csv_file.write(f'{i+1},{updated},{change_percent},{last_price}\n')
    print(f'Done with round {i+1}')
    time.sleep(60)