# Frontend Django - Predictor de precios

Frontend en Django que consume el backend FastAPI de predicción de precios.

## Endpoint utilizado

El backend expone:

`POST /predict`

Body:

```json
{
  "aream2": 82.5
}
```

Respuesta:

```json
{
  "aream2": 82.5,
  "predicted_price": 203353.5
}
```

## Ejecutar localmente

1. Crear entorno virtual.
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Configurar la URL del backend:

Windows PowerShell:

```powershell
$env:API_URL="http://127.0.0.1:8000"
```

4. Ejecutar:

```bash
python manage.py runserver
```

## Railway

Crea un servicio separado para este frontend.

En Variables agrega:

```text
API_URL=https://TU-BACKEND.up.railway.app
```

Railway detectará el `Dockerfile` y ejecutará Django con Gunicorn usando el puerto `PORT` que Railway proporciona.
