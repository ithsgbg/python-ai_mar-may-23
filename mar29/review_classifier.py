import contractions
import re
import json
from string import punctuation

def clean_text(text):
    text = contractions.fix(text)
    text = text.lower()
    text = re.sub(f'[{re.escape(punctuation)}]', '', text)
    text = re.sub('\d', '', text)
    stopwords = [word.strip() for word in open('./mar29/stopwords_en.txt', 'r')]
    text = ' '.join([word for word in text.split() if word not in stopwords])
    return text

class Review:
    def __init__(self, text, score):
        self.text = text
        self.score = score
        self.cleaned = clean_text(text)
        self.sentiment = 'NEGATIVE' if score <= 2 else 'NEUTRAL' if score <= 3 else 'POSITIVE'
      
reviews = []
with open('./mar29/Pet_Supplies_1000.json', 'r') as in_file:
    for line in in_file:
        data = json.loads(line)
        review_text = data['reviewText']
        overall = data['overall']
        reviews.append(Review(review_text, overall))
