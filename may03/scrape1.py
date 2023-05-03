import requests

page_data = requests.get('https://dn.se')
if page_data.ok:
    with open('./may03/dn.html', 'w', encoding='utf-8') as out_file:
        out_file.write(page_data.text)
else:
    print('Page not found')