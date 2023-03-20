def calculate_distance(height1, weight1, height2, weight2):
    # Calculate the distance between two points
    distance = ((height1 - height2) ** 2 + (weight1 - weight2) ** 2) ** 0.5
    return distance

# knn function to predict t-shirt size from height, weight, compared to values in a list
def knn_predict(k, height, weight, list_of_samples):
    # Create a list to store the distances
    distances = []
    
    # Loop through each sample in the list of samples
    for sample in list_of_samples:
        # Calculate the distance between the sample and the input measurements
        distance = calculate_distance(height, weight, sample[0]/10, sample[1]/10)
        
        # Add the distance and the label (t-shirt size) to the list of distances
        distances.append((distance, sample[3]))
    
    # Sort the list of distances from smallest to largest
    distances.sort()
    
    return distances[:k]

def predict(neigbors):
    tshirt_size = {}
    for n in neigbors:
        if n[1] in tshirt_size:
            tshirt_size[n[1]] += 1
        else:
            tshirt_size[n[1]] = 1
    return max(tshirt_size, key=tshirt_size.get)
    
   