from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import hashlib
import json
from datetime import datetime
import os

#Entrenar
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

# Crear archivo de metadatos
metadata = {
    "created_at": datetime.now().isoformat(),
    "model_type": "RandomForestClassifier",
    "input_shape": X.shape,
    "file_size_bytes": os.path.getsize("model.pkl")
}

with open("model_metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)

print("✅ Modelo entrenado y guardado con hash:", model_hash)
