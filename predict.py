import subprocess
import joblib
import numpy as np
import sys

# 1. Ejecutar el script de verificación
result = subprocess.run(["python", "check_integrity.py"], capture_output=True, text=True)

# 2. Mostrar resultado de la verificación
print(result.stdout)

# 3. Si hay señales de manipulación, no continuar
if "CUIDADO" in result.stdout or "INCORRECTO" in result.stdout:
    print("Verificación fallida: el modelo puede estar manipulado. Abortando inferencia.")
    sys.exit(1)

# 4. Si todo está bien, cargar modelo y hacer predicción
model = joblib.load("model.pkl")

# Ejemplo de predicción con datos Iris
X_nuevo = np.array([[5.1, 3.5, 1.4, 0.2]])
pred = model.predict(X_nuevo)

print("Predicción realizada correctamente:")
print("Resultado:", pred)
