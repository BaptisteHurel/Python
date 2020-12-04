#Data cleaning
df = pd.read_csv("./data/labels.csv", usecols=['class', 'tweet'])
df['tweet'] = df['tweet'].apply(lambda tweet: re.sub('[^A-Za-z]+', ' ', tweet.lower()))


from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
X, y= datasets.load_iris(return_X_y=True)
clf.fit(X, y)
SVC()

import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])
array([0])
y[0]

from joblib import dump, load
dump(clf, 'algo.joblib')

clf = load('algo.joblib')

#Algo de prediction

#labels du fichier tweets
# 0 - hate speech 1 - offensive language 2 - neither

@app.route(/predict)

def predict()

return {class1: p1,class2:p2,class3:p3}
