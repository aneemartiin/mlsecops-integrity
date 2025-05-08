import hashlib
import json
import os
import joblib

# Leer modelo actual
with open("model.pkl", "rb") as f:
    current_bytes = f.read()
    current_hash = hashlib.sha256(current_bytes).hexdigest()

# Leer hash original
with open("model_hash.txt", "r") as f:
    original_hash = f.read()

# Comparar
if current_hash == original_hash:
    print("Modelo íntegro: No ha sido manipulado.")
else:
    print("CUIDADO: Modelo manipulado o corrupto.")



# Verificar metadatos
with open("model_metadata.json", "r") as f:
    expected = json.load(f)

actual_size = os.path.getsize("model.pkl")
if actual_size != expected["file_size_bytes"]:
    print("INCORRECTO: Tamaño del archivo no coincide con los metadatos.")
else:
    print("CORRECTO: Tamaño del archivo verificado.")

# Cargar modelo para comprobar tipo
model = joblib.load("model.pkl")
actual_type = type(model).__name__

if actual_type != expected["model_type"]:
    print(f"INCORRECTO: Tipo de modelo diferente: se esperaba {expected['model_type']} pero se encontró {actual_type}.")
else:
    print("CORRECTO: Tipo de modelo correcto.")

# Mostrar info de creación (no se puede verificar directamente sin firma temporal, pero se muestra)
print(f"Fecha de creación registrada: {expected['created_at']}")
print(f"Forma esperada del input: {expected['input_shape']}")