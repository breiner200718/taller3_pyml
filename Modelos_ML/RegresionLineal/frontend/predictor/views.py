import os
import requests
from django.shortcuts import render

def home(request):
    context = {}
    if request.method == "POST":
        area_raw = request.POST.get("area", "").strip()

        try:
            area = float(area_raw)
            if area <= 0:
                raise ValueError

            api_url = os.getenv("API_URL", "").rstrip("/")
            if not api_url:
                context["error"] = "La variable API_URL no está configurada en Railway."
            else:
                response = requests.post(
                    f"{api_url}/predict",
                    json={"aream2": area},
                    timeout=15,
                )
                response.raise_for_status()
                result = response.json()

                context["result"] = result
                context["area"] = area_raw

        except ValueError:
            context["error"] = "Ingresa una superficie válida mayor que 0."
        except requests.exceptions.RequestException:
            context["error"] = (
                "No fue posible conectar con la API. "
                "Verifica que el backend esté funcionando y que API_URL sea correcta."
            )

    return render(request, "home.html", context)
