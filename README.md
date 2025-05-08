# mlsecops-integrity

# MLSecOps - Verificación de Integridad de Modelos ML

Este repositorio contiene un sistema de verificación de integridad para modelos de Machine Learning en producción. Combina técnicas como hashes SHA-256, firmas digitales, verificación estructural, ejecución automatizada en contenedor y escaneo de seguridad con Trivy. También incluye verificación automática en tiempo de inferencia para evitar el uso de modelos manipulados.


## Archivos clave

- `train_model.py`: Entrena un modelo, calcula el hash SHA256 y guarda metadatos (`model_metadata.json`).
- `check_integrity.py`: Verifica que el modelo (`model.pkl`) no ha sido alterado (hash + metadatos).
- `fake_model_train.py`: Simula una manipulación, sobrescribiendo el modelo original con uno distinto.
- `predict.py`: Automatiza la verificación antes de predecir. Si el modelo está manipulado, detiene la ejecución.
- `Dockerfile`: Contenedor que empaqueta el sistema de verificación (`check_integrity.py`).
- `model.pkl`: Modelo serializado con joblib.
- `model_hash.txt`: Hash esperado del modelo.
- `model_metadata.json` : Información estructural del modelo (tipo, tamaño, input shape, fecha).
- `.github/workflows/integrity.yml` : Automatiza verificación en GitHub al subir cambios. 
- `requirements.txt` : Librerías necesarias para ejecutar el proyecto.

## Requisitos

- Python 3.12
- Docker 
- GPG 
- GitHub + GitHub Actions (para CI/CD)
- Trivy 

## Cómo ejecutar

1. Entrenar y verificar:
```bash
python train_model.py
gpg --output model.pkl.sig --detach-sign model.pkl
python predict.py
```

2. Simular ataque
```bash
python fake_model_train.py
python predict.py
```

3. Ejecutar verificación en Docker
```bash
docker build -t model-checker .
docker run --rm model-checker
```

4. Escanear contenedor con Trivy
```bash
docker run --rm aquasec/trivy image model-checker
```

5. Verificación automática en GitHub (CI/CD)
Cada vez que subas un cambio al repositorio que modifique `model.pkl`, `model_hash.txt` o `model_metadata.json`, GitHub ejecutará automáticamente la verificación de integridad.
Puedes consultar los resultados en la pestaña **Actions** del repositorio


## Resultado esperado

Este sistema detecta cualquier intento de manipulación del modelo. Si el modelo ha sido modificado:
- El hash no coincide
- Los metadatos no concuerdan
- La firma digital es inválida
- La predicción no se ejecuta
Esto garantiza que el modelo en producción es exactamente el mismo que el entrenado y firmado por el autor original.