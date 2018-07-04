# Will Wagner
# IST 341
# April 18, 2018
# #
# digits5: modeling the digits data with DTs and RFs
#


import numpy as np            
import pandas as pd

from sklearn import tree      # for decision trees
from sklearn import ensemble  # for random forests

try: # different imports for different versions of scikit-learn
    from sklearn.model_selection import cross_val_score   # simpler cv this week
except ImportError:
    try:
        from sklearn.cross_validation import cross_val_score
    except:
        print("No cross_val_score!")

#
# The "answers" to the 20 unknown digits, labeled -1:
#
answers = [9,9,5,5,6,5,0,9,8,9,8,4,0,1,2,3,4,5,6,7]


print("+++ Start of pandas' datahandling +++\n")
# df here is a "dataframe":
df = pd.read_csv('hw9/digits5.csv', header=0)    # read the file w/header row #0
df.head()                                 # first five lines
df.info()                                 # column details
print("\n+++ End of pandas +++\n")



#
# now, model from iris5.py to try DTs and RFs on the digits dataset!
# 



print("+++ Start of numpy/scikit-learn +++\n")
# Data needs to be in numpy arrays - these next two lines convert to numpy arrays
X_all = df.iloc[:,0:64].values        # iloc == "integer locations" of rows/cols
y_all = df[ '64' ].values      # individually addressable columns (by name)


# ------

X_data_full = X_all[21:,:]  # 
y_data_full = y_all[21:]    # 

X_train = X_data_full[:21,:]
y_train = y_data_full[:21]

print(X_train)
print(y_train)


#
# some labels to make the graphical trees more readable...
#
print("Some labels for the graphical tree:")

feature_names = []
# create a list of column names
for x in range(65):
    column_name = "column " + str(x)
    feature_names.append(column_name)

feature_names.append('Value')
print(feature_names)

target_names = ['1', '2', '3','4','5','6','7','8','9','0']

#
# show the creation of three tree files (at three max_depths)
#
for max_depth in [2,4,25]:
    # the DT classifier
    dtree = tree.DecisionTreeClassifier(max_depth=max_depth)

    # train it (build the tree)
    dtree = dtree.fit(X_train, y_train) 

    # write out the dtree to tree.dot (or another filename of your choosing...)
    filename = 'tree_digits' + str(max_depth) + '.dot'
    tree.export_graphviz(dtree, out_file=filename,   # the filename constructed above...!
                            feature_names=feature_names,  filled=True, 
                            rotate=False, # LR vs UD
                            class_names=target_names, 
                            leaves_parallel=False )  # lots of options!
    #
    # Visualize the resulting graphs (the trees) at www.webgraphviz.com
    #
    print("Wrote the file", filename)  
    #


#
# cross-validation and scoring to determine parameter: max_depth
# 
best_cv_score = 0
for max_depth in range(1,50,2):
    # create our classifier
    dtree = tree.DecisionTreeClassifier(max_depth=max_depth)
    #
    # cross-validate to tune our model (this week, all-at-once)
    #
    scores = cross_val_score(dtree, X_train, y_train, cv=5)
    average_cv_score = scores.mean()
    print("For depth=", max_depth, "average CV score = ", average_cv_score)  
    # print("      Scores:", scores)

    # I automated the selection process
    if average_cv_score > best_cv_score:
        best_cv_score = average_cv_score
        MAX_DEPTH = max_depth

# import sys
# print("bye!")
# sys.exit(0)

# MAX_DEPTH = 3   # choose a MAX_DEPTH based on cross-validation... 
print("\nChoosing MAX_DEPTH =", MAX_DEPTH, "\n")

#
# now, train the model with ALL of the training data...  and predict the unknown labels
#

X_unknown = X_all[0:9,0:4]              # the final testing data
X_train = X_all[9:,0:4]              # the training data

y_unknown = y_all[0:9]                  # the final testing outputs/labels (unknown)
y_train = y_all[9:]                  # the training outputs/labels (known)

# our decision-tree classifier...
dtree = tree.DecisionTreeClassifier(max_depth=MAX_DEPTH)
dtree = dtree.fit(X_train, y_train) 

#
# and... Predict the unknown data labels
#
print("Decision-tree predictions:\n")
predicted_labels = dtree.predict(X_unknown)
answer_labels = answers

#
# formatted printing! (docs.python.org/3/library/string.html#formatstrings)
#
s = "{0:<11} | {1:<11}".format("Predicted","Answer")
#  arg0: left-aligned, 11 spaces, string, arg1: ditto
print(s)
s = "{0:<11} | {1:<11}".format("-------","-------")
print(s)
# the table...
for p, a in zip( predicted_labels, answer_labels ):
    s = "{0:<11} | {1:<11}".format(p,a)
    print(s)

#
# feature importances!
#
print()
print("dtree.feature_importances_ are\n      ", dtree.feature_importances_) 
print("Order:", feature_names[0:4])
