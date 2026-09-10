import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
RUTA = BASE_DIR / "15_posts.json"


def guardar_posts(posts: list[dict]) -> None:
    with open(RUTA, "w", encoding="utf-8") as archivo:
        json.dump(posts, archivo, indent=4, ensure_ascii=False)


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


def introducir_post(posts: list[dict]) -> dict:
    max_id = 0
    for post in posts:
        post_id = post.get("id", 0)
        max_id = max(max_id, post_id)
    titulo = input("Introduce el título del post: ")
    contenido = input("Introduce el contenido del post: ")
    estado = input("Introduce el estado del post (publicado/borrador): ")
    post = {"id": max_id + 1, "titulo": titulo, "contenido": contenido, "estado": estado}
    return post


def main():
    posts = leer_posts()
    nuevo_post = introducir_post(posts)
    posts.append(nuevo_post)
    guardar_posts(posts)


if __name__ == "__main__":
    main()
