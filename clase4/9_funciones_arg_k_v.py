def presentar_a_persona(**kwargs) -> None:
    # print(len(kwargs))
    nombre = kwargs.get("nombre")
    edad = kwargs.get("edad")
    altura = kwargs.get("altura")
    activo = kwargs.get("activo", False)
    print(
        f"Hola, {nombre}! Tienes {edad} años. Tu altura es {altura} y estas "
        f"{'activo' if activo else 'inactivo'}"
    )


presentar_a_persona(nombre="María", edad=20)
presentar_a_persona(nombre="Pepe", edad=24, altura=1.8)
presentar_a_persona(nombre="Lu", edad=30, altura=1.5, activo=True)

una_persona = {"nombre": "Horacio", "edad": 17, "activo": False}
presentar_a_persona(**una_persona)
