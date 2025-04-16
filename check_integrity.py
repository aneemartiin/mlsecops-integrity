<<<<<<< HEAD
import hashlib

# Leer modelo actual
with open("model.pkl", "rb") as f:
    current_bytes = f.read()
    current_hash = hashlib.sha256(current_bytes).hexdigest()

# Leer hash original
with open("model_hash.txt", "r") as f:
    original_hash = f.read()

# Comparar
if current_hash == original_hash:
    print("✅ Modelo íntegro. No ha sido manipulado.")
else:
    print("❌ ALERTA: Modelo manipulado o corrupto.")
=======
import hashlib

# Leer modelo actual
with open("model.pkl", "rb") as f:
    current_bytes = f.read()
    current_hash = hashlib.sha256(current_bytes).hexdigest()

# Leer hash original
with open("model_hash.txt", "r") as f:
    original_hash = f.read()

# Comparar
if current_hash == original_hash:
    print("✅ Modelo íntegro. No ha sido manipulado.")
else:
    print("❌ ALERTA: Modelo manipulado o corrupto.")
>>>>>>> 7a7e51dcc8535757c7d45ef09ad3374d5ac3aba7
