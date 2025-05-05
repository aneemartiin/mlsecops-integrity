from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import hashlib

# Entrenar modelo
X, y = load_iris(return_X_y=True)
clf = RandomForestClassifier()
clf.fit(X, y)

# Guardar modelo
joblib.dump(clf, "model.pkl")

# Calcular hash del modelo
with open("model.pkl", "rb") as f:
    model_bytes = f.read()
    model_hash = hashlib.sha256(model_bytes).hexdigest()

# Guardar hash en archivo
with open("model_hash.txt", "w") as f:
    f.write(model_hash)

print("✅ Modelo entrenado y guardado con hash:", model_hash)
