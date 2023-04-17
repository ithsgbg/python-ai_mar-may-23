import requests

number = input('Enter a number to get fact about: ')

result = requests.get(f'http://numbersapi.com/{number}')
print(result.text)