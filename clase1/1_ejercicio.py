"""
A partir de dos variables llamadas nombre y edad:
crear una variable que almacene si se cumplen las siguientes condiciones,
y mostrar al usuario True o False:
    - nombre sea diferente de cuatro asteriscos ****
    - edad sea mayor que 5 y a su vez menor que 20
    - Que la longitud de nombre sea mayor o igual a 4 pero a la vez menor que 8
    - edad multiplicada por 3 sea mayor que 35

No debes usar funciones, ni condicionales (if), bucles (while-for) o cualquier
otra instrucción que no hayamos visto.
"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

es_valido_nombre = nombre != "****"
es_valido_nombre_longitud = len(nombre) >= 4 and len(nombre) < 8
es_valido_edad = edad > 5 and edad < 20
es_valido_edad_calculada = (edad * 3) > 35

es_valido_todo = all(
    [
        es_valido_nombre,
        es_valido_nombre_longitud,
        es_valido_edad,
        es_valido_edad_calculada,
    ]
)

print(es_valido_todo)
