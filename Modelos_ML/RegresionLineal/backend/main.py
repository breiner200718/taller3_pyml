import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pathlib import Path

app = FastAPI(title="API de Predicción de Precios de Viviendas", description="Esta API predice el precio de una vivienda según su superficie en metros cuadrados utilizando un modelo de regresión lineal entrenado.", version="1.0.0")

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "linear_model.joblib"

try:
    # Cargar el modelo entrenado
    model = joblib.load(MODEL_PATH)
except Exception:
    model = None

class housem2(BaseModel):
    aream2: float = Field(..., example=82.5, description="Superficie de la vivienda en metros cuadrados")


@app.get("/")
def health_check():
    return {"status": "OK", "message": "API de predicción de precios de viviendas está funcionando correctamente.","model_loaded": model is not None}

@app.post("/predict")
def predict_price(data: housem2):
    if not model:
        raise HTTPException(status_code=500, detail="Modelo no disponible. Por favor, intente nuevamente más tarde.")

    # Realizar la predicción
    prediction = model.predict([[data.aream2]])[0]
    return {
        "aream2": data.aream2,
        "predicted_price": round(prediction, 2)
    }