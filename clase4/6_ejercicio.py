def formatear_log(mensaje: str, nivel: str = "INFO", urgente: bool = False) -> str:
    if urgente:
        texto_mensaje = f"!!! {mensaje.upper()}"
    else:
        texto_mensaje = mensaje
    return f"[{nivel}] {texto_mensaje}"


def main() -> None:
    # 1. Pasando solo el mensaje obligatorio (usando ambos valores por defecto).
    print(formatear_log("Sistema iniciado con éxito"))
    #  2. Cambiando solo el nivel (por ejemplo, a "WARNING").
    print(formatear_log("Espacio de disco bajo", "WARNING"))
    # 3. Cambiando solo la bandera urgente a True mediante argumento por nombre
    print(formatear_log("Datos siendo transferidos", urgente=True))
    # 4. Cambiando ambos parámetros opcionales (por ejemplo, nivel="ERROR" y urgente=True).
    print(formatear_log("Base de datos no responde", nivel="ERROR", urgente=True))


main()
