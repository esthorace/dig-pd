# Generador de Listas de Texto

Crea una función llamada `generar_lista` que reciba un título obligatorio y una cantidad variable de elementos en texto (*args), retornado la lista con formato.

## Función generar_lista(titulo: str, *elementos: str) -> str:

- Recibe el `título` de la lista (ej. "Compras", "Pendientes").

- Recibe cualquier cantidad de cadenas de texto mediante `*elementos`.

- Retorna un texto formateado con el título en la primera línea y cada elemento numerado abajo.
    Ej:
        --- LISTA DE "COMPRAS" ---
        1. Pan
        2. Leche
        3. Vino
## Función main:

Debe llamar a generar_lista al menos 3 veces pasando 1, 3 y 4 elementos respectivamente, e imprimir los resultados.