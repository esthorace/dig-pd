usuarios: list[dict] = [
    {
        "nombre": "Juan",
        "nacionalidades": ["argentina", "española"],
    },
    {
        "nombre": "María",
        "nacionalidades": ["colombiana"],
    },
    {
        "nombre": "Pedro",
        "nacionalidades": ["chilena"],
    },
    {
        "nombre": "Ana",
        "nacionalidades": ["uruguaya"],
    },
]

print(f"{'NOMBRE':<20} | {'NACIONALIDADES':<20}")
for usuario in usuarios:
    nombre = usuario["nombre"]
    nacionalidades = ", ".join(usuario["nacionalidades"])
    print(f"{nombre:<20} | {nacionalidades:<20}")

nacionalidad_española_juan = usuarios[0]["nacionalidades"][1]
print(nacionalidad_española_juan)
