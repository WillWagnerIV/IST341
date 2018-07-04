# Will Wagner
# 3/26/2018
# IST341 - hw 8 - iris
# coding: utf-8

import numpy as np
from sklearn import cross_validation
import pandas as pd

# N = 0
# y_known = []
# X_known = []


print("+++ Start of pandas +++\n")
# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
df = pd.read_csv('./hw8/iris.csv', header=0)    # read the file
df.head()                                 # first five lines
df.info()                                 # column details



print("+++ Start of numpy/scikit-learn +++")
#
# We create numpy arrays out of the pandas dataframes...
#

# Data needs to be in numpy arrays - these next two lines convert to numpy arrays
X_data_complete = df.iloc[:,0:4].values        # iloc == "integer locations" of rows/cols
y_data_complete = df[ 'irisname' ].values      # individually addressable columns (by name)

# Remember
#
# capital X refers to the inputs (the "independent" variables)
# lower-case y refers to the output (the "dependent" variable, being modeled)
#

#
# We create the appropriate subsets of data
#

# First, the TRULY UNKNOWN data rows - we don't know which flowers these are!
# 
X_unknown = X_data_complete[:9,:]   # 2d array
y_unknown = y_data_complete[:9]     # 1d column


#
# Next, we have our KNOWN data - 
# 
X_known = X_data_complete[9:,]
y_known = y_data_complete[9:]


# In[12]:

# Now, let's shuffle it!
def shuffle_data(X_known,y_known):
    N = len(y_known)
    indices = np.random.permutation(N)  # this is a random permutation
    X_known = X_known[indices]
    y_known = y_known[indices]
    return X_known,y_known

X_known,y_known = shuffle_data(X_known,y_known)

#
# feature engineering!...
#


# here is where we can re-scale our feature values...
X_known[:,0] *= 1.0   # or 42.0: maybe the first column is worth 42x more?!
X_known[:,3] *= 1.0   # or 100.0: maybe the fourth column is worth 100x more?!

# Now, let's split our KNOWN data into a training set and testing set...
# We'll use an 80/20 split...
#
N = int(0.80*len(y_known))  # N is the size of the training set == 0.80*size of all known data

# training set:
X_train = X_known[:N]
y_train = y_known[:N]

# testing set:
X_test = X_known[N:]
y_test = y_known[N:]

# Now, we create a model, knn_model
#
#   we need to choose a value for k  Let's choose 42.
#   later, we'll choose more carefully!
#
from sklearn.neighbors import KNeighborsClassifier
knn_model = KNeighborsClassifier(n_neighbors=42)   # 42 is the "k" in kNN

# then, we train that model...
knn_model.fit(X_train, y_train)  # done!

# Then, we test by running the model, 
y_predicted = knn_model.predict(X_test)

# Let's look at the predicted values:
print("the predicted labels are")
y_predicted  

print("the correct labels are")
y_test[0]


# let's see these next to each other...

N = len(y_test)

s = "{0:>4s} | {1:>12s} {2:<12s} {3:^7s}".format("i", "PRED", "ACTUAL", "EQUAL?")
print(s)

s = "{0:>4s} | {1:>12s} {2:<12s} {3:^7s}".format("-", "----", "------", "------")
print(s)

correct = 0

for i in range(N):
    predicted_label = y_predicted[i]
    actual_label = y_test[i]
    correctness = str(predicted_label == actual_label)
    s = "{0:>4d} | {1:>12s} {2:<12s} {3:^7s}".format(i,predicted_label,actual_label,correctness)
    print(s)
    
    if predicted_label == actual_label: correct += 1
        
print("\n")
score = correct / N
print("Percentage correct =", score)


# The process above is a by-hand example of "cross-validation"

# It can be done many times with a single call! Here is an example
try:
    from sklearn.model_selection import cross_val_score
except:
    from sklearn.cross_validation import cross_val_score

# notice we use X_known and y_known --> the cross-validation splits it up for us...
scores = cross_val_score(knn_model, X_known, y_known, cv=5)  # 5-fold cross-validation (80/20 split)
print(scores)
print(scores.mean())



# But, 42 is not necessarily the correct value for k ...   counter-intuitive as that may seem...
# So, we run this same process on LOTS of values of k and find the best
# That's your task! You should loop over k here and print all of the average (mean) scores:
#

NN = len(y_known)

best_n_neighbors = 1
best_score = float(scores.mean())

for n_neighbors in range(1,int(NN/2)):
    knn_model = KNeighborsClassifier(n_neighbors)   # 42 is the "k" in kNN
    # could reshuffle... so we will!
    X_known,y_known = shuffle_data(X_known,y_known)

    scores = cross_val_score(knn_model, X_known, y_known, cv=5)
    print(n_neighbors)
    print(scores)
    print(scores.mean())

    sm = float(scores.mean())
    print("sm = " + str(sm))

    if sm > best_score:
        best_n_neighbors = n_neighbors
        best_score = float(scores.mean())

n_neighbors = best_n_neighbors

print('\n\n')
print("The best k was "+ str(n_neighbors) + " at " + str(best_score))
print()

#
# Now, use your best value of k, train on ALL KNOWN data, and test on the UNKNOWN data!
#

knn_model = KNeighborsClassifier(n_neighbors)   # Fix this to be YOUR value of k, determined above!

# then, we train that model on ALL known data...
knn_model.fit(X_known,y_known)

# Then, we test by running the model, 
y_predicted = knn_model.predict(X_unknown)

# Let's look at the predicted values:
print("the predicted labels are")
print(y_predicted)

# compare with the real labels:
#
# Virginica, Virginica, Versicolor, Versicolor, Setosa, Setosa, Virginica, Versicolor, Setosa
# 
# The first one is often misclassified as versicolor, but that's because it's uncharacteristic!




#
# a function for testing values typed in
#
def test_by_hand(knn_model):
    """ allows the user to enter values and predict the
        label using the knn model passed in
    """
    print()
    Arr = np.array([[0,0,0,0]]) # correct-shape array
    T = Arr[0]
    T[0] = float(input("sepal length? "))
    T[1] = float(input("sepal width? "))
    T[2] = float(input("petal length? "))
    T[3] = float(input("petal width? "))
    prediction = knn_model.predict(Arr)[0]
    print("The prediction is", prediction)
    print()


# test_by_hand( knn_model )  

