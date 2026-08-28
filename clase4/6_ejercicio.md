# Ejercicio

Debes crear un programa en Python que formatee mensajes del sistema (logs)
aplicando prefijos y estilos según los parámetros recibidos.

## Función formatear_log (función principal de procesamiento):

- **Parámetro obligatorio**: `mensaje` (cadena de texto).

- **Parámetro opcional 1**: `nivel` (cadena de texto, valor por defecto `"INFO"`).

- **Parámetro opcional 2**: `urgente` (booleano, valor por defecto `False`).

## Comportamiento:

- Si urgente es True, la función debe devolver el mensaje en mayúsculas y agregar el texto "!!! " al inicio.

- Si urgente es False, el mensaje mantiene su formato normal.

- El nivel puede ser:
    
    1. INFO
    2. WARNING
    3. ERROR

- La función debe retornar una cadena formateada con la estructura: `"[NIVEL] Mensaje"`.

## Función main:

- Debe ejecutar al menos 4 llamadas distintas a formatear_log probando las siguientes combinaciones e imprimiendo el resultado en consola:

    1. Pasando solo el mensaje obligatorio (usando ambos valores por defecto).

    2. Cambiando solo el nivel (por ejemplo, a "WARNING").

    3. Cambiando solo la bandera urgente a True mediante argumento por nombre (keyword argument).

    4. Cambiando ambos parámetros opcionales (por ejemplo, nivel="ERROR" y urgente=True).
