# fake_model_train.py
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
import joblib

X, y = load_digits(return_X_y=True)
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Guardarlo con el mismo nombre que el original
joblib.dump(clf, "model.pkl")