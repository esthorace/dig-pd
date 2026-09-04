"""
Crear una clase para una tienda que gestione el precio de un artículo usando getters, setters
y una propiedad calculada

class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        # TODO: Asigna el precio usando el setter

    # TODO: Define el getter para 'precio'

    # TODO: Define el setter para 'precio' (valida que sea > 0)

    # TODO: Define el getter para 'precio_con_iva' (solo lectura)


# --- Casos de prueba ---
# 1. Producto válido
p1 = Producto("Teclado Mecánico", 100.0)
print(f"Producto: {p1.nombre}")
print(f"Precio base: ${p1.precio}")          # Esperado: 100.0
print(f"Precio con IVA: ${p1.precio_con_iva}") # Esperado: 121.0

# 2. Modificación válida
p1.precio = 150.0
print(f"Nuevo precio con IVA: ${p1.precio_con_iva}") # Esperado: 181.5

# 3. Intentar crear producto inválido (debe lanzar ValueError)
# p2 = Producto("Mouse", -50)
"""


class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio  # Debo pasar por el setter para validar

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, nuevo_valor: float) -> None:
        if nuevo_valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self.__precio = nuevo_valor  # Aquí creo el atributo privado

    @property
    def precio_con_iva(self) -> float:
        return round(self.__precio * 1.21, 2)


# --- Casos de prueba ---
# 1. Producto válido
p1 = Producto("Teclado Mecánico", 100.0)
print(f"Producto: {p1.nombre}")
print(f"Precio base: ${p1.precio}")  # Esperado: 100.0
print(f"Precio con IVA: ${p1.precio_con_iva}")  # Esperado: 121.0

# 2. Modificación válida
p1.precio = 150.0
print(f"Nuevo precio con IVA: ${p1.precio_con_iva}")  # Esperado: 181.5

# 3. Intentar crear producto inválido (debe lanzar ValueError)
# p2 = Producto("Mouse", -50)
