import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def calculate_distance(centroid, X, Y):
    distances = []
    # Unpack the x and y coordinates of the centroid
    c_x, c_y = centroid
    # Iterate over the data points and calculate the distance using the           # given formula
    for x, y in list(zip(X, Y)):
        root_diff_x = (x - c_x) ** 2
        root_diff_y = (y - c_y) ** 2
        distance = np.sqrt(root_diff_x + root_diff_y)
        distances.append(distance)
    return distances


def toy_dataset():
    X = np.array([[1, 0], [2, 0], [3, -1], [4, 1], [4, 2], [5, 2], [10, 0], [12, 2]])

    # Convert the data points into a pandas DataFrame
    # Generate indicators for the data points
    obj_names = []
    for i in range(1, 9):
        obj = "Object " + str(i)
        obj_names.append(obj)

    # Create a pandas DataFrame with the names and (x, y) coordinates
    data = pd.DataFrame({
        'Object': obj_names,
        'X_value': X[:, 0],
        'Y_value': X[:, -1]
    })

    # Initialize the centroids
    c1 = (1, 0)
    c2 = (2, 0)

    for i in range(0, 7):
        plt.scatter(X[:, 0], X[:, -1])
        plt.xlabel('X Coordinates')
        plt.ylabel('Y Coordinates')
        plt.scatter(c1[0], c1[1], c='red', marker='x')
        plt.scatter(c2[0], c2[1], c='red', marker='x')
        plt.title('Data points and cluster centroids iteration ' + str(i+1))
        plt.grid()
        plt.savefig('plot'+str(i+1))
        plt.show()
        data['C1_Distance'] = calculate_distance(c1, data.X_value, data.Y_value)
        data['C2_Distance'] = calculate_distance(c2, data.X_value, data.Y_value)
        # Get the minimum distance centroids
        data['Cluster'] = data[['C1_Distance', 'C2_Distance']].apply(np.argmin, axis=1)
        # Map the centroids accordingly and rename them
        data['Cluster'] = data['Cluster'].map({0: 'C1', 1: 'C2'})

        # Calculate the coordinates of the new centroid from cluster 1
        x_new_centroid1 = data[data['Cluster'] == 'C1']['X_value'].mean()
        y_new_centroid1 = data[data['Cluster'] == 'C1']['Y_value'].mean()

        # Calculate the coordinates of the new centroid from cluster 2
        x_new_centroid2 = data[data['Cluster'] == 'C2']['X_value'].mean()
        y_new_centroid2 = data[data['Cluster'] == 'C2']['Y_value'].mean()

        # Print the coordinates of the new centroids
        print('Centroid 1 ({}, {})'.format(x_new_centroid1, y_new_centroid1))
        print('Centroid 2 ({}, {})'.format(x_new_centroid2, y_new_centroid2))
        c1 = (x_new_centroid1, y_new_centroid1)
        c2 = (x_new_centroid2, y_new_centroid2)
        print(i+1)
        print(data)

    # Get a preview of the data
    # print(data.head(10))
    ###################################################
    # This is only used to check that the final answer is correct using the internal KMeans function in sklearn
    kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
    print(kmeans.cluster_centers_)
    ####################################################



if __name__ == '__main__':
    toy_dataset()
