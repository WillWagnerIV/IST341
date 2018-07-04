# Will Wagner
# 4/18/2018
# IST341 - hw9
# #
# titanic5: modeling the Titanic data with DTs and RFs
#

import numpy as np            
import pandas as pd

from sklearn import tree      # for decision trees
from sklearn import ensemble  # for random forests

try: # different imports for different versions of scikit-learn
    from sklearn.model_selection import cross_val_score   # simpler cv
except ImportError:
    try:
        from sklearn.cross_validation import cross_val_score
    except:
        print("No cross_val_score!")


#
# The "answers" to the 30 unlabeled passengers:
#
answers = [0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,
            1,0,1,1,1,1,0,0,0,1,1,0,1,0]

#

print("+++ Start of pandas' datahandling +++\n")
# df here is a "dataframe":
df = pd.read_csv('hw9/titanic5.csv', header=0)    # read the file w/header row #0
df.head()
df.info()
#
# Drop columns with too few values or that won't be meaningful
df = df.drop('name', axis=1)  # axis = 1 means column
df = df.drop('sibsp', axis=1)  # axis = 1 means column
df = df.drop('parch', axis=1)  # axis = 1 means column
df = df.drop('ticket', axis=1)  # axis = 1 means column
df = df.drop('cabin', axis=1)  # axis = 1 means column
df = df.drop('embarked', axis=1)  # axis = 1 means column
df = df.drop('home.dest', axis=1)  # axis = 1 means column

df.head()                                 # first five lines
df.info()                                 # column details

# One important one is the conversion from string to numeric datatypes!
# Define a function, to help out...
def tr_mf(s):
    """ from string to number
    """
    d = { 'male':0, 'female':1 }
    return d[s]

df['sex'] = df['sex'].map(tr_mf)  # apply the function to the column
#
# end of conversion to numeric data...
# drop rows with missing data!
df = df.dropna()
#
print("\n+++ End of pandas +++\n")

# END of PANDAS

# START of NUMPY / SCIKIT-LEARN

print("+++ Start of numpy/scikit-learn +++\n")
# Data needs to be in numpy arrays - these next two lines convert to numpy arrays 
X_all = df.drop('survived', axis=1).values       
y_all = df[ 'survived' ].values      



#
# now, building from iris5.py and/or digits5.py
#      create DT and RF models on the Titanic dataset!
#      Goal: find feature importances ("explanations")
#      Challenge: can you get over 80% CV accuracy?
# 

# ----------


X_labeled = X_all  
y_labeled = y_all    

#
# we can scramble the data - but only the labeled data!
# 
indices = np.random.permutation(len(X_labeled))  # this scrambles the data each time
X_data_full = X_labeled[indices]
y_data_full = y_labeled[indices]

X_train = X_data_full
y_train = y_data_full

#
# some labels to make the graphical trees more readable...
#
print("Some labels for the graphical tree:")
feature_names = ['pclass','sex','age','fare']
target_names = ['Deceased','Survived','-1']



#
# cross-validation and scoring to determine parameter: max_depth
# 
best_cv_score = 0
for max_depth in range(1,12):
    # create our classifier
    dtree = tree.DecisionTreeClassifier(max_depth=max_depth)
    #
    # cross-validate to tune our model (this week, all-at-once)
    #
    scores = cross_val_score(dtree, X_train, y_train, cv=10)
    average_cv_score = scores.mean()
    print("For depth=", max_depth, "average CV score = ", average_cv_score)  
    # print("      Scores:", scores)

    if average_cv_score > best_cv_score:
        best_cv_score = average_cv_score
        MAX_DEPTH = max_depth

# import sys
# print("bye!")
# sys.exit(0)

# MAX_DEPTH = 3   # choose a MAX_DEPTH based on cross-validation... 
print("\nChoosing MAX_DEPTH =", MAX_DEPTH, "\n")

max_depth = MAX_DEPTH
# the DT classifier
dtree = tree.DecisionTreeClassifier(max_depth=max_depth)

# train it (build the tree)
dtree = dtree.fit(X_train, y_train) 

# write out the dtree to tree.dot (or another filename of your choosing...)
filename = 'tree_titanic' + str(max_depth) + '.dot'
tree.export_graphviz(dtree, out_file=filename,   # the filename constructed above...!
                        feature_names=feature_names,  filled=True, 
                        rotate=False, # LR vs UD
                        class_names=target_names, 
                        leaves_parallel=True )  # lots of options!
#
# Visualize the resulting graphs (the trees) at www.webgraphviz.com
#
print("Wrote the file", filename)  
#

#
# now, train the model with ALL of the training data...  and predict the unknown labels
#
rows = 32
X_unknown = X_all[rows:]              # the final testing data
X_train = X_all[rows:]              # the training data

y_unknown = y_all[:rows]                  # the final testing outputs/labels (unknown)
y_train = y_all[rows:]                  # the training outputs/labels (known)




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
