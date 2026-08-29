# Consigna: Generador de Reportes con Metadatos

Crea una función llamada crear_reporte que reciba un título obligatorio, una cantidad variable de observaciones o puntos clave (*args) y una cantidad variable de metadatos en formato clave-valor (**kwargs).

## Función crear_reporte(titulo: str, *puntos: str, **metadatos: str) -> str:

- Recibe el parámetro obligatorio titulo.

- Recibe observaciones ilimitadas mediante *puntos (se iteran como viñetas).

- Recibe datos opcionales clave=valor mediante **metadatos (se iteran como un diccionario con .items()).

- Devuelve todo consolidado en un solo texto.

## Función main:

Debe llamar a la función pasando distintas combinaciones de puntos clave y metadatos nombrados (ej: autor="Ana", prioridad="Alta").

## Ejercicio

### Ejemplo 1: Dos puntos de texto (*args) y dos metadatos clave=valor (**kwargs)
```py
    reporte_1 = crear_reporte(
        "Inicio de Proyecto",
        "Reunión con cliente realizada",
        "Presupuesto aprobado",
        autor="Carlos",
        fecha="2026-08-28"
    )
```

### Ejemplo 2: Tres puntos y tres metadatos distintos

```py
reporte_2 = crear_reporte(
    "Mantenimiento Web",
    "Base de datos actualizada",
    "Servidor optimizado",
    "Certificado SSL renovado",
    responsable="Ana",
    prioridad="Alta",
    estado="Completado",
)
```