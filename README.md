## K-Means-toy-dataset
## This is an example of using the K-Means Cluster algorithm to solve a problem of finding the centroids in a toy 2D example 

## Prerequisites

All the dependencies and required libraries are included in the file <code>requirements.txt</code>  
Use the following commands to install all the dependencies:
```
$ pip3 install sklearn
$ pip3 install pandas
$ pip3 install matplotlib
```

## Installation
Clone the repo
```
$ git clone https://github.com/ABraik-bit/K-Means-toy-dataset
```


## Working

To run the algorithm
```
$ python3 main.py 
```
## Visualizing the data
![Starting iteration](https://github.com/ABraik-bit/K-Means-toy-dataset/blob/main/plot1.png)
![First iteration](https://github.com/ABraik-bit/K-Means-toy-dataset/blob/main/plot2.png)
![Second iteration](https://github.com/ABraik-bit/K-Means-toy-dataset/blob/main/plot3.png)
![Third iteration](https://github.com/ABraik-bit/K-Means-toy-dataset/blob/main/plot4.png)
![Forth iteration](https://github.com/ABraik-bit/K-Means-toy-dataset/blob/main/plot5.png)
![Fifth iteration](https://github.com/ABraik-bit/K-Means-toy-dataset/blob/main/plot6.png)

To understand the algorithm, here is an example of the final output of the data
```
   Object    X_value  Y_value   C1_Distance  C2_Distance Cluster
0  Object 1        1        0     2.266912    10.049876      C1
1  Object 2        2        0     1.343710     9.055385      C1
2  Object 3        3       -1     1.674979     8.246211      C1
3  Object 4        4        1     0.897527     7.000000      C1
4  Object 5        4        2     1.572330     7.071068      C1
5  Object 6        5        2     2.266912     6.082763      C1
6  Object 7       10        0     6.865777     1.414214      C2
7  Object 8       12        2     8.933396     1.414214      C2
[[ 3.16666667  0.66666667]
 [11.          1.        ]] #centroid final coordinates 
```


