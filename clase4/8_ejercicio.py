# def generar_lista(titulo, *tareas):
#     lineas = [f"=== LISTA DE {titulo.upper()} ==="]

#     for i, tarea in enumerate(tareas, start=1):
#         lineas.append(f"{i}. {tarea}")
#     return "\n".join(lineas)


def generar_lista(titulo: str, *tareas: str) -> str:
    lineas: list[str] = [f"=== LISTA DE {titulo.upper()} ==="]

    for i, tarea in enumerate(tareas, start=1):
        lineas.append(f"{i}. {tarea}")
    return "\n".join(lineas)


def main():
    # Caso 1 elemento
    print(generar_lista("Urgencias", "Llamar al médico"))
    print()
    # Caso 3 elementos
    print(generar_lista("Tareas", "Estudiar Python", "Lavar los platos", "Salir a correr"))
    print()
    # Caso 4 elementos
    print(generar_lista("Super", "Leche", "Huevos", "Pan", "Frutas"))


main()
