# mlsecops-integrity

# MLSecOps - Verificación de Integridad de Modelos ML

Este proyecto demuestra un pipeline básico de seguridad para modelos en producción, usando hashes SHA256 para detectar manipulaciones en archivos de modelos.

## 🚀 Archivos clave

- `train_model.py`: Entrena un modelo y guarda su hash.
- `check_integrity.py`: Verifica que el modelo actual no ha sido alterado.
- `fake_model_train.py`: Simula un modelo diferente (manipulación).
- `Dockerfile`: Contenedor que corre la verificación.
- `model.pkl`: Modelo serializado.
- `model_hash.txt`: Hash esperado del modelo.

## 🧪 Cómo ejecutar

1. Entrena y genera hash:
```bash
python train_model.py