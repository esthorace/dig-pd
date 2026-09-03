import json
from pathlib import Path
from pprint import pprint

ruta = Path(__file__).resolve().parent

with open(ruta / "17-mi-json.json", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    print(type(datos))
    print(len(datos))

pprint(datos)
