import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
RUTA = BASE_DIR / "15_posts.json"


def leer_posts() -> list[dict]:
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            posts: list[dict] = json.load(archivo)
    except FileNotFoundError:
        print("El archivo no existe")
        posts = []
    except json.decoder.JSONDecodeError:
        print("El archivo existe pero el JSON está corrupto")
        posts = []

    return posts


def main():
    posts = leer_posts()
    print(posts)


if __name__ == "__main__":
    main()
