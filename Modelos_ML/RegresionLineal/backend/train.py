from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

# Predecir precios de viviendas según la superficie en m2

# Datos de entrenamiento X y Y
x = np.array([[40], [50], [60], [85], [100], [120]])
y = np.array([100000, 120000, 150000, 200000, 250000, 300000])

# Entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(x, y)

"""# Predicción de prueba
y_pred = model.predict(x)

# Imprimir los resultados de la predicción
print("Coeficiente de regresión lineal:", model.coef_[0])
print("Término independiente:", model.intercept_)

# Graficar los datos del entrenamiento y las predicciones
plt.plot(x, y_pred, color="red", label="Línea de regresión")
plt.scatter(x, y, color="blue", label="Datos de entrenamiento")

plt.xlabel("Superficie (m2)")
plt.ylabel("Precio (COP)")
plt.title("Regresión lineal: Precio de vivienda según superficie")
plt.legend()
plt.grid(True)

# Crear la carpeta models si no existe
os.makedirs("models", exist_ok=True)


# Mostrar la gráfica
plt.show()


# Guardar el modelo entrenado"""

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "linear_model.joblib"

joblib.dump(model, MODEL_PATH)


