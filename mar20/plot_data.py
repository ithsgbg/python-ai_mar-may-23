import pandas as pd
import matplotlib.pyplot as plt
from mar20.predict import knn_predict, predict


female = pd.read_csv('./mar20/new_female.csv')
male = pd.read_csv('./mar20/new_male.csv')

combined = female.append(male, ignore_index=True)
combined_list = combined.values.tolist()
weight = 71
height = 170
prediction = knn_predict(77, height, weight, combined_list)
print(predict(prediction))
plt.scatter(combined['weight'], combined['height'], c=combined['color'])
plt.show()
