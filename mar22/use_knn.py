import pickle

my_knn = pickle.load(open('./mar22/my_knn.pkl', 'rb'))
sk_knn = pickle.load(open('./mar22/sk_knn.pkl', 'rb'))
prediction = my_knn.predict([(152, 52), (172, 67)])
prediction2 = sk_knn.predict([(152, 52), (172, 67)])
print(prediction)
print(prediction2)