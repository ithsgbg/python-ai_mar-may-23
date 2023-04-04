from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC

corpus = [
    'I love the book',
    'This book was not so good',
    'the fit was great',
    'i love the shoes'
]

books = 'Books'
clothing = 'Clothing'

categories = [books, books, clothing, clothing]

vectorizer = CountVectorizer(ngram_range=(2, 3))

vectors = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names_out())
print(vectors.toarray())

# svm = SVC(kernel='linear')
# svm.fit(vectors, categories)


# test_X = [
#     'I love this read',
#     'such a nice hat',
#     'what a great book'
# ]

# test_y = [books, clothing, books]
# test_vectors = vectorizer.transform(test_X)
# print('The result is:', svm.score(test_vectors, test_y))

