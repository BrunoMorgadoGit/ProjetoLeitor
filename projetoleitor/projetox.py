from flask import Flask, request, jsonify
import easyocr
import cv2
import numpy as np
import os
import re

print(">>> PROJETOX NOVO CARREGADO <<<")

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# OCR
ocr = easyocr.Reader(['pt'], gpu=False)

# Regex placa Mercosul
PLACA_REGEX = re.compile(r'[A-Z]{3}[0-9][A-Z0-9][0-9]{2}')

@app.route("/", methods=["GET"])
def home():
    return {"status": "Servidor ONLINE"}, 200
@app.route("/processar", methods=["POST"])
def processar():
    if "file" not in request.files:
        return {"erro": "Arquivo não enviado"}, 400

    file = request.files["file"]
    img_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)

    if image is None:
        return {"erro": "Imagem inválida"}, 400

    h, w, _ = image.shape

    # Recorte onde a placa realmente está (ajuste fino)
    y1, y2 = int(h * 0.70), int(h * 0.83)
    x1, x2 = int(w * 0.34), int(w * 0.66)
    placa = image[y1:y2, x1:x2]

    # Pasta de debug
    debug_dir = "debug"
    os.makedirs(debug_dir, exist_ok=True)

    # 1️⃣ salvar recorte original
    cv2.imwrite(f"{debug_dir}/01_recorte.jpg", placa)

    # 2️⃣ HSV + canal V
    hsv = cv2.cvtColor(placa, cv2.COLOR_BGR2HSV)
    v = hsv[:, :, 2]
    cv2.imwrite(f"{debug_dir}/02_v_channel.jpg", v)

    # 3️⃣ CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    v = clahe.apply(v)
    cv2.imwrite(f"{debug_dir}/03_clahe.jpg", v)

    # 4️⃣ Resize forte
    v = cv2.resize(v, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(f"{debug_dir}/04_resize.jpg", v)

    # OCR SEM NENHUM FILTRO
    resultados = ocr.readtext(v, detail=1)

    textos = []
    for _, texto, conf in resultados:
        textos.append((texto, conf))

    if not textos:
        return {
            "mensagem": "Placa não reconhecida",
            "ocr_bruto": [],
            "debug": "Veja a pasta /debug"
        }, 200

    texto_completo = "".join(t[0].replace(" ", "").upper() for t in textos)
    match = PLACA_REGEX.search(texto_completo)

    if not match:
        return {
            "mensagem": "Placa não reconhecida",
            "ocr_bruto": textos,
            "debug": "Veja a pasta /debug"
        }, 200

    return {
        "mensagem": "Placa reconhecida com sucesso",
        "placa": match.group()
    }, 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
