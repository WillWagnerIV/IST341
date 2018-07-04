# Will Wagner
# 3/26/2018
# IST341 - hw8
# 
# 
# # coding: utf-8



#
#
# titanic.py
#
#

import numpy as np
from sklearn import datasets
from sklearn import cross_validation
import pandas as pd

# For Pandas's read_csv, use header=0 when you know row 0 is a header row
# df here is a "dataframe":
df = pd.read_csv('hw8/titanic.csv', header=0)
df.head()
df.info()

# let's drop columns with too few values or that won't be meaningful
# Here's an example of dropping the 'body' column:
df = df.drop('body', axis=1)  # axis = 1 means column
df = df.drop('name', axis=1)  # axis = 1 means column
df = df.drop('sibsp', axis=1)  # axis = 1 means column
df = df.drop('parch', axis=1)  # axis = 1 means column
df = df.drop('ticket', axis=1)  # axis = 1 means column
df = df.drop('cabin', axis=1)  # axis = 1 means column
df = df.drop('embarked', axis=1)  # axis = 1 means column
df = df.drop('boat', axis=1)  # axis = 1 means column
df = df.drop('home.dest', axis=1)  # axis = 1 means column

# let's drop all of the rows with missing data:
df = df.dropna()

# let's see our dataframe again...
# I ended up with 1001 rows (anything over 500-600 seems reasonable)
# _Don't_ use the result if it has fewer than 500 rows!
# Instead, drop more columns BEFORE the df = df.dropna() call...
df.head()
df.info()


# In[6]:

# You'll need conversion to numeric datatypes for all input columns
#   Here's one example
#
def tr_mf(s):
    """ from string to number
    """
    d = { 'male':1, 'female':0 }
    return d[s]

df['sex'] = df['sex'].map(tr_mf)  # apply the function to the column

# let's see our dataframe again...
df.head()
df.info()


# you will need others!

# Re-Mapping Age
# Will's ruthless factor

def tr_age(s):
    """ favor persons closest to age 22
    """
    # d = { 'male':0, 'female':1 }
    return d[s]

# df['sex'] = df['sex'].map(tr_age)  # apply the function to the column

# let's see our dataframe again...
df.head()
df.info()

print("+++ end of pandas +++\n")


# In[8]:

print("+++ start of numpy/scikit-learn +++")

# Note that you'll likely split cell this into multiple cells...

#
# Let's convert parts of the dataframe, df, to a numpy array
# 

# extract the underlying data with the values attribute:
X_data_complete = df.drop('survived', axis=1).values        # everything except the 'survival' column
y_data_complete = df[ 'survived' ].values      # also addressable by column name(s)

# let's see our dataframe again...
df.head()
df.info()

#
# you need to take away the top 42 passengers (with unknown survival/perish data) here:
#

X_unknown = X_data_complete[42,:]   # 2d array
y_unknown = y_data_complete[:42]     # 1d column

#
# Next, we have our KNOWN data - 
# 
X_known = X_data_complete[42:,]
y_known = y_data_complete[42:]


# Now, let's shuffle it!
def shuffle_data(X_known,y_known):
    N = len(y_known)
    indices = np.random.permutation(N)  # this is a random permutation
    X_known = X_known[indices]
    y_known = y_known[indices]
    return X_known,y_known

X_known,y_known = shuffle_data(X_known,y_known)


# feature engineering...
X_data_complete[:,0] = (3/X_data_complete[:,0])*.10   # 
X_data_complete[:,2] *= 1   # 
# X_data_complete[:,4] *= 1   # 
X_data_complete[:,3] *= 100   # 




#
# the rest of this model-building, cross-validation, and prediction will come here:
#     build from the experience and code in the other two examples... (iris and digits)
#


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


knn_model = KNeighborsClassifier(n_neighbors=42)   # the "k" in kNN

# then, we train that model...
knn_model.fit(X_train, y_train)  # done!

# Then, we test by running the model, 
y_predicted = knn_model.predict(X_test)

# Let's look at the predicted values:
print("the predicted labels are", y_predicted)
  
print("the correct labels are", y_test)

# let's see these next to each other...

print()

N = len(y_test)

s = "{0:>4s} | {1:>12s} {2:<12s} {3:^7s}".format("i", "PRED", "ACTUAL", "EQUAL?")
print(s)

s = "{0:>4s} | {1:>12s} {2:<12s} {3:^7s}".format("-", "----", "------", "------")
print(s)

correct = 0

for i in range(N):
    predicted_label = str(y_predicted[i])
    actual_label = str(y_test[i])
    correctness = str(predicted_label == actual_label)
    s = "{0:>4d} | {1:>12s} {2:<12s} {3:^7s}".format(i,predicted_label,actual_label,correctness)
    print(s)
    
    if predicted_label == actual_label: correct += 1
        
print("\n")
score = (correct * 100) / N
print("Percentage correct =", score)
print()
print("="*15)


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

for n_neighbors in range(1,50):
    knn_model = KNeighborsClassifier(n_neighbors)   # is the "k" in kNN
    # could reshuffle... so we will!
    X_known,y_known = shuffle_data(X_known,y_known)

    scores = cross_val_score(knn_model, X_known, y_known, cv=10)
    print(n_neighbors)
    print(scores)
    #print(scores.mean())

    sm = float(scores.mean())
    print("sm = " + str(sm))

    if sm > best_score:
        best_n_neighbors = n_neighbors
        best_score = float(scores.mean())

n_neighbors = best_n_neighbors

print()
print("The best k was "+ str(n_neighbors) + " at " + str(best_score))
print()

#
# Now, use your best value of k, train on ALL KNOWN data, and test on the UNKNOWN data!
#

knn_model = KNeighborsClassifier(n_neighbors)   # YOUR value of k, determined above!

# then, we train that model on ALL known data...

# X_known = X_data_complete[43:,]
# y_known = y_data_complete[43:]


# then, we train that model...
knn_model.fit(X_train, y_train)  # done!

# Then, we test by running the model, 
y_predicted = knn_model.predict(X_test)

# Let's look at the predicted values:
print("the predicted labels are", y_predicted)
  
print("the correct labels are", y_test)

# let's see these next to each other...

print()

N = len(y_test)

s = "{0:>4s} | {1:>12s} {2:<12s} {3:^7s}".format("i", "PRED", "ACTUAL", "EQUAL?")
print(s)

s = "{0:>4s} | {1:>12s} {2:<12s} {3:^7s}".format("-", "----", "------", "------")
print(s)

correct = 0

for i in range(N):
    predicted_label = str(y_predicted[i])
    actual_label = str(y_test[i])
    correctness = str(predicted_label == actual_label)
    s = "{0:>4d} | {1:>12s} {2:<12s} {3:^7s}".format(i,predicted_label,actual_label,correctness)
    print(s)
    
    if predicted_label == actual_label: correct += 1
        
print("\n")
score = (correct * 100) / N
print("Percentage correct =", score)
print()
print("="*15)








"""
Comments and results:

Briefly mention how this went:
  + what value of k did you decide on for your kNN?
  + how high were you able to get the average cross-validation (testing) score?



Then, include the predicted labels of the 12 digits with full data but no label:
Paste those labels (just labels) here:
You'll have 12 lines:




And, include the predicted labels of the 10 digits that are "partially erased" and have no label:
Mention briefly how you handled this situation!?

Past those labels (just labels) here:
You'll have 10 lines:






My best run?

The best k was 13 at 0.692982398239824

the predicted labels are [0 0 1 0 1 0 0 0 0 0 0 1 0 1 1 0 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 1 1
 1 1 0 1 0 0 1 0 0 1 0 0 0 0 0 1 0 0 1 0 1 0 1 1 0 0 1 1 1 1 0 0 0 0 0 0 1
 0 0 1 1 1 0 1 0 1 0 1 1 0 0 0 0 1 1 0 1 1 1 0 0 1 0 1 0 1 1 0 0 0 1 1 0 1
 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 1 0 0 1 0 0 0 1 0 0 0 0 0 1 0 1 0
 0 1 1 0 1 0 0 1 0 1 0 0 0 0 0 1 0 0 1 1 0 1 0 0 0 1 0 1 0 0 1 0 1 0 1 1 0
 0 1 0 0 0 1 0 1 0 0 1 1 0 0 1 0]
the correct labels are [1 0 1 0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 0 1 0 0 1 0 1 0 1 0 0 1 1 0 1 1 0 0 1
 1 1 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 1 1 0 0 1 1 0 1 0 0 0 0 1 0 1
 0 0 1 1 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 1 0 1 0 0 1 0 1 0 1 1 0 0 0 1 0 0 1
 0 1 0 1 0 0 0 1 0 0 1 1 0 0 0 0 0 1 0 0 1 0 0 1 0 1 0 1 0 0 0 0 0 1 0 1 0
 0 1 1 1 0 0 0 1 0 0 0 0 0 1 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 1 0 1 0 1 1 0
 0 1 0 1 1 1 0 1 0 1 1 0 0 0 1 0]

   i |         PRED ACTUAL       EQUAL?
   - |         ---- ------       ------
   0 |            0 1             False
   1 |            0 0             True
   2 |            1 1             True
   3 |            0 0             True
   4 |            1 1             True
   5 |            0 0             True
   6 |            0 0             True
   7 |            0 1             False
   8 |            0 0             True
   9 |            0 0             True
  10 |            0 0             True
  11 |            1 1             True
  12 |            0 0             True
  13 |            1 0             False
  14 |            1 1             True
  15 |            0 0             True
  16 |            0 0             True
  17 |            0 0             True
  18 |            0 0             True
  19 |            1 1             True
  20 |            0 0             True
  21 |            0 0             True
  22 |            1 1             True
  23 |            0 0             True
  24 |            1 1             True
  25 |            0 0             True
  26 |            0 1             False
  27 |            0 0             True
  28 |            0 0             True
  29 |            1 1             True
  30 |            0 1             False
  31 |            0 0             True
  32 |            1 1             True
  33 |            0 1             False
  34 |            0 0             True
  35 |            1 0             False
  36 |            1 1             True
  37 |            1 1             True
  38 |            1 1             True
  39 |            0 0             True
  40 |            1 0             False
  41 |            0 1             False
  42 |            0 0             True
  43 |            1 1             True
  44 |            0 0             True
  45 |            0 0             True
  46 |            1 0             False
  47 |            0 0             True
  48 |            0 0             True
  49 |            0 0             True
  50 |            0 0             True
  51 |            0 0             True
  52 |            1 1             True
  53 |            0 0             True
  54 |            0 0             True
  55 |            1 0             False
  56 |            0 0             True
  57 |            1 1             True
  58 |            0 1             False
  59 |            1 1             True
  60 |            1 1             True
  61 |            0 0             True
  62 |            0 0             True
  63 |            1 1             True
  64 |            1 1             True
  65 |            1 0             False
  66 |            1 1             True
  67 |            0 0             True
  68 |            0 0             True
  69 |            0 0             True
  70 |            0 0             True
  71 |            0 1             False
  72 |            0 0             True
  73 |            1 1             True
  74 |            0 0             True
  75 |            0 0             True
  76 |            1 1             True
  77 |            1 1             True
  78 |            1 0             False
  79 |            0 0             True
  80 |            1 1             True
  81 |            0 0             True
  82 |            1 0             False
  83 |            0 0             True
  84 |            1 0             False
  85 |            1 1             True
  86 |            0 0             True
  87 |            0 0             True
  88 |            0 0             True
  89 |            0 0             True
  90 |            1 1             True
  91 |            1 0             False
  92 |            0 0             True
  93 |            1 1             True
  94 |            1 0             False
  95 |            1 1             True
  96 |            0 0             True
  97 |            0 0             True
  98 |            1 1             True
  99 |            0 0             True
 100 |            1 1             True
 101 |            0 0             True
 102 |            1 1             True
 103 |            1 1             True
 104 |            0 0             True
 105 |            0 0             True
 106 |            0 0             True
 107 |            1 1             True
 108 |            1 0             False
 109 |            0 0             True
 110 |            1 1             True
 111 |            0 0             True
 112 |            0 1             False
 113 |            0 0             True
 114 |            0 1             False
 115 |            0 0             True
 116 |            0 0             True
 117 |            0 0             True
 118 |            0 1             False
 119 |            0 0             True
 120 |            0 0             True
 121 |            1 1             True
 122 |            0 1             False
 123 |            0 0             True
 124 |            0 0             True
 125 |            0 0             True
 126 |            0 0             True
 127 |            0 0             True
 128 |            1 1             True
 129 |            0 0             True
 130 |            0 0             True
 131 |            1 1             True
 132 |            0 0             True
 133 |            0 0             True
 134 |            1 1             True
 135 |            0 0             True
 136 |            0 1             False
 137 |            0 0             True
 138 |            1 1             True
 139 |            0 0             True
 140 |            0 0             True
 141 |            0 0             True
 142 |            0 0             True
 143 |            0 0             True
 144 |            1 1             True
 145 |            0 0             True
 146 |            1 1             True
 147 |            0 0             True
 148 |            0 0             True
 149 |            1 1             True
 150 |            1 1             True
 151 |            0 1             False
 152 |            1 0             False
 153 |            0 0             True
 154 |            0 0             True
 155 |            1 1             True
 156 |            0 0             True
 157 |            1 0             False
 158 |            0 0             True
 159 |            0 0             True
 160 |            0 0             True
 161 |            0 1             False
 162 |            0 1             False
 163 |            1 1             True
 164 |            0 0             True
 165 |            0 1             False
 166 |            1 1             True
 167 |            1 0             False
 168 |            0 0             True
 169 |            1 0             False
 170 |            0 0             True
 171 |            0 1             False
 172 |            0 0             True
 173 |            1 1             True
 174 |            0 1             False
 175 |            1 1             True
 176 |            0 1             False
 177 |            0 0             True
 178 |            1 1             True
 179 |            0 0             True
 180 |            1 1             True
 181 |            0 0             True
 182 |            1 1             True
 183 |            1 1             True
 184 |            0 0             True
 185 |            0 0             True
 186 |            1 1             True
 187 |            0 0             True
 188 |            0 1             False
 189 |            0 1             False
 190 |            1 1             True
 191 |            0 0             True
 192 |            1 1             True
 193 |            0 0             True
 194 |            0 1             False
 195 |            1 1             True
 196 |            1 0             False
 197 |            0 0             True
 198 |            0 0             True
 199 |            1 1             True
 200 |            0 0             True


Percentage correct = 80.09950248756219

===============

"""


