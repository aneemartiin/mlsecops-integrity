import subprocess
import joblib
import numpy as np
import sys

#ejecutar check_integrity
result = subprocess.run(["python", "check_integrity.py"], capture_output=True, text=True)
print(result.stdout)

#si hay manipulación que no continue
if "CUIDADO" in result.stdout or "INCORRECTO" in result.stdout:
    print("Verificación fallida: el modelo puede estar manipulado. Abortando inferencia.")
    sys.exit(1)

#y si todo está bien entonces se puede cargar el modelo
model = joblib.load("model.pkl")

#un ejemplo de predicción para comprobar
X_nuevo = np.array([[5.1, 3.5, 1.4, 0.2]])
pred = model.predict(X_nuevo)

print("Predicción realizada correctamente:")
print("Resultado:", pred)
