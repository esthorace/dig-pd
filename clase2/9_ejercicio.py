"""
A partir de las siguientes tuplas, realizar las siguientes operaciones:
cajon_verduras = ("zanahorias", "papas", "repollo", "cebollas")
cajon_frutas = ("manzanas", "naranjas", "peras", "uvas")

- Cargar el camion_1 (tupla) con 1 cajon de verduras y 1 cajon de frutas (print)
- Descargar el camion_1 (unpacking)
- Cargar el camion_2 (tupla) con concatenacion de las tuplas cajon_verduras y cajon_frutas
- Cargar el camion_3 (tupla) con * para desempaquetar las tuplas cajon_verduras y cajon_frutas
"""

cajon_verduras = ("zanahorias", "papas", "repollo", "cebollas")
cajon_frutas = ("manzanas", "naranjas", "peras", "uvas")

# Carga de camión 1
camion_1 = (cajon_verduras, cajon_frutas)
print("Carga de camión 1:", camion_1)

# Descarga de camión 1
verduras, frutas = camion_1
print("Descarga de camión 1:")
print(f"\tVerduras: {', '.join(verduras)}")
print(f"\tFrutas: {', '.join(frutas)}")

# Carga de camión 2
camion_2 = cajon_verduras + cajon_frutas
print("Carga de camión 2:", camion_2)

# Carga de camión 3
camion_3 = (*cajon_verduras, *cajon_frutas)
print("Carga de camión 3:", camion_3)
