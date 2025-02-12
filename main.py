from sklearn import tree
import matplotlib.pyplot as plt
import csv

#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: decision_tree.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
#AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

db = []
X = []
Y = []

#reading the data in a csv file
file_path = "C:\\Users\\sophi\\Downloads\\contact_lens (1).csv"
with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append(row)
            print(row)

#transform the original categorical training features into numbers and add to the
#4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
age_mapping = {'Young': 1, 'Prepresbyopic': 2, 'Presbyopic': 3}
spectacle_mapping = {'Myope': 1, 'Hypermetrope': 2}
tear_mapping = {'Reduced': 1, 'Normal': 2}
astigmatism_mapping = {'No': 1, 'Yes': 2}

for row in db:
    X.append([
        age_mapping[row[0]],
        spectacle_mapping[row[1]],
        astigmatism_mapping[row[2]],
        tear_mapping[row[3]]
    ])

#transform the original categorical training classes into numbers and add to the
#vector Y. For instance Yes = 1, No = 2
class_mapping = {'Yes': 1, 'No': 2}
for row in db:
    Y.append(class_mapping[row[4].strip()])

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'],
               class_names=['Yes', 'No'], filled=True, rounded=True)
plt.show()