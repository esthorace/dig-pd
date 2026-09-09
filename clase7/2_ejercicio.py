"""
Crear un programa que tenga dos modelos: Biblioteca y Libro.

Atributos de Libro: titulo, autor, año
Atributos de Biblioteca: nombre, libros (lista de instancias de Libro)
Métodos de Biblioteca: agregar(libro: Libro), eliminar, listar

- Crear 3 libros, agregarlos a la biblioteca y listarlos

libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Órganon", "Aristóteles", -384)
"""


class Libro:
    def __init__(self, titulo: str, autor: str, año: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self) -> str:
        periodo = "a.C." if self.año < 0 else ""
        año_texto = f"{abs(self.año)} {periodo}".strip()
        return f'"{self.titulo}", de {self.autor} ({año_texto})'


class Biblioteca:
    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.libros: list[Libro] = []

    # def agregar_libro(self, libro: Libro) -> None:
    #     self.libros.append(libro)

    def agregar_libros(self, *libros: Libro):
        self.libros.extend(libros)

    def eliminar_libro(self, libro: Libro):
        if libro not in self.libros:
            print(f"-> El libro '{libro.titulo}' no está en la biblioteca.")
            return
        self.libros.remove(libro)

    def listar(self) -> None:
        print(f"\n*** Biblioteca {self.nombre} ***")
        if not self.libros:
            print("La biblioteca está vacía")
            return
        for indice, libro in enumerate(self.libros, start=1):
            print(f"   {indice}. {libro}")


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Órganon", "Aristóteles", -384)

biblioteca = Biblioteca("La Gran Biblioteca")
# biblioteca.agregar_libro(libro1)
# biblioteca.agregar_libro(libro2)
# biblioteca.agregar_libro(libro3)
biblioteca.agregar_libros(libro1, libro2, libro3)
biblioteca.listar()
biblioteca.eliminar_libro(libro3)
biblioteca.eliminar_libro(libro3)
biblioteca.listar()
