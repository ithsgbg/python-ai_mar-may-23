import contractions
import re
import json
from string import punctuation
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC


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

training_data, test_data = train_test_split(reviews, test_size=0.2, random_state=42)

train_X = [review.cleaned for review in training_data]
train_y = [review.sentiment for review in training_data]

test_X = [review.cleaned for review in test_data]
test_y = [review.sentiment for review in test_data]

vectorizer = CountVectorizer()
train_x_vectors = vectorizer.fit_transform(train_X)

clf_svc = SVC(kernel='linear')
clf_svc.fit(train_x_vectors, train_y)

test_x_vectors = vectorizer.transform(test_X)
# for i, vector in enumerate(test_x_vectors):
#     prediction = clf_svc.predict(vector)
#     if prediction[0] != test_y[i]:
#         print('Predicted', prediction[0])
#         print('Was', test_y[i])
#         print("Review text:", test_X[i])

#print(clf_svc.score(test_x_vectors, test_y))

review_text = "I bought Teddy's Pride Oral Care with the hope it would help to keep my dog's teeth clean and freshen her breath like the product information says it will do. Unfortunately, it doesn't do anything! I've now used the entire jar of powder as directed, but the claims for cleaning a dog's teeth and freshening a dog's breath were not kept in the slightest. I certainly won't buy more! Total waste of money and disappointment!"
#review_text = "I hate this. It is awful. Warning!"
review_cleaned = clean_text(review_text)
review_vector = vectorizer.transform([review_text])
print(clf_svc.predict(review_vector))