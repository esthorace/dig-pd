def crear_reporte(titulo: str, *puntos: str, **metadatos: str) -> str:
    lineas = [f"--- REPORTE: {titulo.upper()} ---"]

    # si hay *args
    if puntos:
        lineas.append("\nPuntos claves:")
        for punto in puntos:
            lineas.append(f" - {punto}")

    # si hay **kwargs
    if metadatos:
        lineas.append("\nInformación adicional:")
        for k, v in metadatos.items():
            lineas.append(f" {k.capitalize()}: {v}")

    return "\n".join(lineas)


def main():

    reporte_1 = crear_reporte(
        "Inicio de Proyecto",
        "Reunión con cliente realizada",
        "Presupuesto aprobado",
        autor="Carlos",
        fecha="2026-08-28",
    )
    reporte_2 = crear_reporte(
        "Mantenimiento Web",
        "Base de datos actualizada",
        "Servidor optimizado",
        "Certificado SSL renovado",
        responsable="Ana",
        prioridad="Alta",
        estado="Completado",
    )
    print(reporte_1)
    print(reporte_2)


main()
