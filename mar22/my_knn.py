import numpy as np

class KNNClassifier:
    def __init__(self, k):
        self.k = k
        self.X = None
        self.y = None
        
    def _calculate_distance(self, x1, x2):
        return ((x1 - x2)**2).sum() ** 0.5
    
    def fit(self, X, y):
        self.X = np.array(X)
        self.y = np.array(y)
    
    def _knn_predict(self, x):
        # Create a list to store the distances
        distances = []
        
        # Loop through each sample in the list of samples
        for i in range(len(self.X)):
            distance = self._calculate_distance(x, self.X[i])
    
            distances.append((distance, self.y[i]))
            
        distances.sort()
        
        return distances[:self.k]
    
    def predict(self, X):
        # X = [(178, 86), (164, 52)]
        
        # Make predictions on new data
        predictions = []
        
        for x in X:
            # x = (178, 86)
            # x is the height and weight for one person
            neighbors = self._knn_predict(x)
            prediction = self._predict(neighbors)
            predictions.append(prediction)
            
        return predictions
    
    def _predict(self, neighbors):
        labels = [n[1] for n in neighbors]
        return max(set(labels), key=labels.count)

    def _predict_new(self, neighbors):
        labels = [n[1] for n in neighbors]
        result = {}
        for n in neighbors:
            if n[1] in result:
                result[n[1]] += 1
            else:
                result[n[1]] = 1
        prediction = 'We predict:\n'
        for k, v in result.items():
            prediction += f'{k} with a chance of {(v / len(neighbors)) * 100:.2f}%\n'
            
        return prediction