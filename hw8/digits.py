# Will Wagner
# 3/26/2018
# IST341 - hw8
# coding: utf-8

#
#
# digits.py
#
#

import numpy as np
from sklearn import cross_validation
import pandas as pd

# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
df = pd.read_csv('./hw8/digits.csv', header=0)
df.head()
df.info()



# Convert feature columns as needed...
# You may to define a function, to help out:
def transform(s):
    """ from number to string
    """
    return 'digit ' + str(s)
    
df['label'] = df['64'].map(transform)  # apply the function to the column
print()
print("+++ End of pandas +++\n")

print()

print("+++ Start of numpy/scikit-learn +++")
print()

# We'll stick with numpy - here's the conversion to a numpy array
X_data_complete = df.iloc[:,0:64].values        # iloc == "integer locations" of rows/cols
y_data_complete = df[ 'label' ].values      # also addressable by column name(s)

#
# you can divide up your dataset as you see fit here...
#

# Remember
#
# capital X refers to the inputs (the "independent" variables)
# lower-case y refers to the output (the "dependent" variable, being modeled)
#

#
# We create the appropriate subsets of data
#

# First, the TRULY UNKNOWN data rows - we don't know which numbers these are!
# 
X_unknown = X_data_complete[:22,:]   # 2d array
y_unknown = y_data_complete[:22]     # 1d column


#
# Next, we have our KNOWN data - 
# 
X_known = X_data_complete[22:,]
y_known = y_data_complete[22:]


# Now, let's shuffle it!
def shuffle_data(X_known,y_known):
    N = len(y_known)
    indices = np.random.permutation(N)  # this is a random permutation
    X_known = X_known[indices]
    y_known = y_known[indices]
    return X_known,y_known

X_known,y_known = shuffle_data(X_known,y_known)

#
# feature display - use %matplotlib to make this work smoothly
#
from matplotlib import pyplot as plt


def show_digit( Pixels ):
    """ input Pixels should be an np.array of 64 integers (from 0 to 15) 
        there's no return value, but this should show an image of that 
        digit in an 8x8 pixel square
    """
    print(Pixels.shape)
    Patch = Pixels.reshape((8,8))
    plt.figure(1, figsize=(4,4))
    plt.imshow(Patch, cmap=plt.cm.gray_r, interpolation='nearest')  # cm.gray_r   # cm.hot
    plt.show()





def try_picture():
    row = 63
    Pixels = X_data_complete[row:row+1,:]
    show_digit(Pixels)
    print("That image has the label:", y_data_complete[row])





print("The rest of the digits problem...")


#
# feature engineering...
#

""" Your task:

Use iris.py as a starting point to create

X_known
y_known

X_train
y_train

X_test
y_test

and so on...
"""

# here is where we can re-scale our feature values...
X_known[:,0] *= .01   # or 42.0: maybe the first column is worth 42x more?!
X_known[:,63] *= 1.0   # or 100.0: maybe the fourth column is worth 100x more?!

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


# Then, use knn to model and match the digits data!

from sklearn.neighbors import KNeighborsClassifier


knn_model = KNeighborsClassifier(n_neighbors=42)   # 42 is the "k" in kNN

# then, we train that model...
knn_model.fit(X_train, y_train)  # done!

# Then, we test by running the model, 
y_predicted = knn_model.predict(X_test)

# Let's look at the predicted values:
#print("the predicted labels are", y_predicted)
  
# print("the correct labels are", y_test[0])

# let's see these next to each other...

print()

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


best_n_neighbors = 42
best_score = float(scores.mean())

for n_neighbors in (1,2,3,4,5,7,9,11,15):
    knn_model = KNeighborsClassifier(n_neighbors)   # 42 is the "k" in kNN
    # could reshuffle... so we will!
    X_known,y_known = shuffle_data(X_known,y_known)

    scores = cross_val_score(knn_model, X_known, y_known, cv=5)
    print(n_neighbors)
    print(scores)
    #print(scores.mean())

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

knn_model = KNeighborsClassifier(n_neighbors)   # YOUR value of k, determined above!

# then, we train that model on ALL known data...
knn_model.fit(X_known,y_known)

# Then, we test by running the model, 
y_predicted = knn_model.predict(X_unknown)

# Let's look at the predicted values:
print("the predicted labels are")
print(y_predicted)


# try_picture()
a = 64 * 35
b = 64 * 36
Pixels = y_data_complete[a:b]
show_digit( Pixels )


#
# a function for testing values typed in
#
# def test_by_hand(knn_model):
#     """ allows the user to enter values and predict the
#         label using the knn model passed in
#     """
#     print()
#     Arr = np.array([[0,0,0,0]]) # correct-shape array
#     T = Arr[0]
#     T[0] = float(input("sepal length? "))
#     T[1] = float(input("sepal width? "))
#     T[2] = float(input("petal length? "))
#     T[3] = float(input("petal width? "))
#     prediction = knn_model.predict(Arr)[0]
#     print("The prediction is", prediction)
#     print()


# # test_by_hand( knn_model )  


#
# and then see how it does on the two sets of unknown-label data... (!)
#





"""
Comments and results:

Briefly mention how this went:
  + what value of k did you decide on for your kNN?
  + how smoothly were you able to adapt from the iris dataset to here?
  + how high were you able to get the average cross-validation (testing) score?

Then, include the predicted labels of the 12 digits with full data but no label:
Past those labels (just labels) here:
You'll have 12 lines:

'digit 9' 'digit 9' 'digit 5' 'digit 5' 'digit 6' 
'digit 5' 'digit 0' 'digit 9' 'digit 8' 'digit 9' 
'digit 8' 'digit 4'




And, include the predicted labels of the 10 digits that are "partially erased" and have no label:
Mention briefly how you handled this situation!?

Past those labels (just labels) here:
You'll have 10 lines:

'digit 0' 'digit 0' 'digit 0' 'digit 1' 'digit 7' 
'digit 7' 'digit 7' 'digit 4' 'digit 0' 'digit 9'



"""

