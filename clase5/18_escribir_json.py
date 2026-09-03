import json
from pathlib import Path
from pprint import pprint

ruta = Path(__file__).resolve().parent

# lectura
with open(ruta / "17-mi-json.json", encoding="utf-8") as archivo:
    datos: list[dict] = json.load(archivo)

# más datos
persona_nueva = {
    "active": None,
    "age": 20,
    "city": "Bs.As.",
    "name": "Romina",
}
datos.append(persona_nueva)

# escritura
with open(ruta / "17-mi-json.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)
