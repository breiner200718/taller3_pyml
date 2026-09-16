from flask import Flask, request, jsonify, send_from_directory



import cv2

import numpy as np

import base64

import os





# Crear aplicación Flask

app = Flask(__name__, static_folder="../public")





# ==========================================================

# CARGAR CLASIFICADOR DE ROSTROS

# ==========================================================



CASCADE_PATH = os.path.join(

    os.path.dirname(__file__),

    "..",

    "haarcascade_frontalface_default.xml"

)



face_classifier = cv2.CascadeClassifier(CASCADE_PATH)





# Verificar que el clasificador se haya cargado correctamente

if face_classifier.empty():

    print("ERROR: No se pudo cargar haarcascade_frontalface_default.xml")





# ==========================================================

# SERVIR FRONTEND

# ==========================================================



@app.route("/")

def serve_index():

    return send_from_directory(app.static_folder, "index.html")





@app.route("/<path:path>")

def serve_static(path):

    return send_from_directory(app.static_folder, path)





# ==========================================================

# DETECCIÓN DE ROSTROS

# ==========================================================



@app.route("/api/detect", methods=["POST"])

def detect_faces():



    # Verificar que se haya enviado una imagen

    if "image" not in request.files:

        return jsonify({

            "error": "No se proporcionó ninguna imagen"

        }), 400



    file = request.files["image"]



    try:



        # Leer archivo

        filestr = file.read()



        # Convertir los bytes a un array de NumPy

        npimg = np.frombuffer(filestr, np.uint8)



        # Convertir el array en una imagen OpenCV

        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)



        # Verificar que la imagen sea válida

        if img is None:

            return jsonify({

                "error": "Formato de imagen inválido"

            }), 400



        # Crear copia para dibujar los resultados

        output_img = img.copy()



        # Convertir imagen a escala de grises

        gray_image = cv2.cvtColor(

            img,

            cv2.COLOR_BGR2GRAY

        )



        # Detectar rostros

        faces = face_classifier.detectMultiScale(

            gray_image,

            scaleFactor=1.1,

            minNeighbors=5,

            minSize=(40, 40)

        )



        # Dibujar rectángulos alrededor de los rostros

        for x, y, w, h in faces:



            cv2.rectangle(

                output_img,

                (x, y),

                (x + w, y + h),

                (0, 255, 0),

                3

            )



        # Convertir imagen procesada a JPG

        success, buffer = cv2.imencode(

            ".jpg",

            output_img

        )



        if not success:

            return jsonify({

                "error": "No se pudo procesar la imagen"

            }), 500



        # Convertir imagen a Base64

        encoded_image = base64.b64encode(

            buffer

        ).decode("utf-8")



        # Respuesta JSON

        return jsonify({

            "success": True,

            "faces_detected": len(faces),

            "image": f"data:image/jpeg;base64,{encoded_image}"

        })



    except Exception as e:



        return jsonify({

            "error": str(e)

        }), 500





# ==========================================================

# CONFIGURACIÓN

# ==========================================================



app.debug = False





# ==========================================================

# EJECUTAR SERVIDOR LOCAL

# ==========================================================



if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )



#melos
