"""
Usar

"https://jsonplaceholder.typicode.com/posts"

Imprimir el título
"""

import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    for post in posts[:5]:
        print(post["id"], post["title"])
else:
    print("Error de conexión")
