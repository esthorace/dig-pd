# Datos sucios
correos_raw = [
    "  juan.perez@gmail.com ",
    "MARIA@HOTMAIL.COM",
    "",
    "  ",
    "pedro@yahoo.com  ",
]

# correos_limpios = []
# for correo in correos_raw:
#     correo_limpio = correo.strip().lower()
#     if correo_limpio:
#         correos_limpios.append(correo_limpio)

correos_limpios = [c.strip().lower() for c in correos_raw if c.strip()]

print(correos_limpios)
