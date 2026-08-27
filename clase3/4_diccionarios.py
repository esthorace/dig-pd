from pprint import pprint

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "JavaScript", "Java"],
    "activo": True,
}


pprint(diccionario)
diccionario_vacio = {}
diccionario_vacio = dict()
pprint(diccionario_vacio)

# Acceder
print(diccionario["nombre"])
print(diccionario["edad"])

# Crear
diccionario["email"] = "juan@example.com"

# Actualizar
diccionario["edad"] += 1

# Eliminar
del diccionario["email"]
pprint(diccionario)

# Unpacking (desempaquetar) con **
datos_civiles = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
}

datos_estudios = {
    "universidad": "Universidad de Madrid",
    "carrera": "Ingeniería Informática",
    "promedio": 8.5,
}

datos_completos = {**datos_civiles, **datos_estudios}
pprint(datos_completos)
