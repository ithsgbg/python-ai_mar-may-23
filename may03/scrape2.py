import requests_html
from bs4 import BeautifulSoup

session = requests_html.HTMLSession()

result = session.get('http://time-time.net/timer/digital-clock.php')

result.html.render()

if result.ok:
    text = result.html.html
    soup = BeautifulSoup(text, 'html.parser')
    content = soup.find('div', id='timenow')
    print(content.text)
else:
    print('Page not found')
    # with open('./may03/time.html', 'w', encoding='utf-8') as out_file:
    #     out_file.write(text)
