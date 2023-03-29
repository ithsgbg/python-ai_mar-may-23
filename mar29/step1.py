"""
1. Contractions 
2. Make lower case
3. Remove punctiuation
4. Remove numbers
5. Remove stopwords
"""
import contractions
from string import punctuation
import re

def clean_text(text):
    text = contractions.fix(text)
    print('Contractions: ', text)
    text = text.lower()
    print('Lower: ', text)
    text = re.sub(f'[{re.escape(punctuation)}]', '', text)
    print('Punctuation: ', text)
    text = re.sub('\d', '', text)
    print('Numbers: ', text)
    stopwords = [word.strip() for word in open('./mar29/stopwords_en.txt', 'r')]
    text = ' '.join([word for word in text.split() if word not in stopwords])
    print('Stopwords: ', text)
    return text

text = "I read this book for the first time in 1987, and it's still one of my favorites!"
text = clean_text(text)