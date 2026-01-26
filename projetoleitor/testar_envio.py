import requests
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
imagem = os.path.join(BASE_DIR, "carroteste.jpg")

url = "http://localhost:5000/processar"

if not os.path.exists(imagem):
    print("Imagem não encontrada:", imagem)
    exit()

print("Enviando imagem para o servidor...")

with open(imagem, "rb") as f:
    resposta = requests.post(url, files={"file": f})

print("\nSTATUS:", resposta.status_code)
print("RESPOSTA:", resposta.json())
