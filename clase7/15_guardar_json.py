import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
archivo = "15_posts.json"


posts = [
    {"id": 1, "titulo": "Introducción a Python", "autor": "Ana", "estado": "publicado"},
    {"id": 2, "titulo": "Aprendiendo JSON", "autor": "Luis", "estado": "borrador", "activo": True},
]

# print(json.dumps(posts, ensure_ascii=False, indent=4))
with open(BASE_DIR / archivo, "w", encoding="utf-8") as archivo:
    json.dump(posts, archivo, ensure_ascii=False, indent=4)
