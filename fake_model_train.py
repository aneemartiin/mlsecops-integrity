<<<<<<< HEAD
# fake_model_train.py
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
import joblib

X, y = load_digits(return_X_y=True)
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Guardarlo con el mismo nombre que el original
=======
# fake_model_train.py
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
import joblib

X, y = load_digits(return_X_y=True)
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Guardarlo con el mismo nombre que el original
>>>>>>> 7a7e51dcc8535757c7d45ef09ad3374d5ac3aba7
joblib.dump(clf, "model.pkl")