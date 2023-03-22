from my_knn import KNNClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

my_knn = KNNClassifier(k=7)
sk_knn = KNeighborsClassifier(n_neighbors=7)

female = pd.read_csv('./mar22/new_female.csv')
male = pd.read_csv('./mar22/new_male.csv')

combined = pd.concat([female, male], ignore_index=True)

X = combined[['height', 'weight']].values / 10
y = combined['tshirt_size'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# X_train = X[:5500]
# y_train = y[:5500]
# X_test = X[5501:]
# y_test = y[5501:]

my_knn.fit(X_train, y_train)  # Training
pickle.dump(my_knn, open('./mar22/my_knn.pkl', 'wb'))
sk_knn.fit(X_train, y_train)
pickle.dump(sk_knn, open('./mar22/sk_knn.pkl', 'wb'))
# Predict
prediction = my_knn.predict([(172, 81)])
print(prediction[0])
# my_predictions = my_knn.predict(X_test)
# knn_predictions = sk_knn.predict(X_test)

# correct = 0
# for i, prediction in enumerate(my_predictions):
#     if prediction == y_test[i]:
#         correct += 1

        
# print(f'We were correct {correct} times out of {len(my_predictions)}')

# correct = 0
# for i, prediction in enumerate(knn_predictions):
#     if prediction == y_test[i]:
#         correct += 1

        
# print(f'We were correct {correct} times out of {len(knn_predictions)}')