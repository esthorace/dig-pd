diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "JavaScript", "Java"],
    "activo": True,
}

# get()
print(diccionario["nombre"])
print(diccionario.get("nombre"))
print(diccionario.get("nombresssss", "- No encontrado"))  # Devuelve None por defecto

# update(dict)
diccionario.update({"edad": 31, "email": "juan@example.com"})
diccionario.update(apellido="Pérez")

# pop(key)
diccionario.pop("activo")
print(diccionario)

# keys()
print(diccionario.keys())
print(list(diccionario.keys()))

# values()
precios = {"manzana": 4, "naranja": 3}
print(precios.values())
print(sum(precios.values()))

# items() -> devolver pares clave:valor

for k, v in diccionario.items():
    print(f"    {k} ->  {v}")

print("****************")
for _, v in diccionario.items():
    print(f" ->  {v}")

print("****************")
for v in diccionario.values():
    print(f" ->  {v}")
