from pprint import pprint

import requests

API_KEY = "0192c56b53f3118e7e26f50005474a62"
ciudad = "Mendoza"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"

respuesta = requests.get(URL)
if respuesta.status_code == 200:
    diccionario = respuesta.json()
    # pprint(diccionario)
    temperatura = diccionario["main"]["temp"]
    descripcion = diccionario["weather"][0]["description"]
    print(f"La temperatura en {ciudad} es de {temperatura}ºC")
    print(f"La descripción del clima es: {descripcion}")
else:
    print("Error al obtener la información")
