# Ejercicios

## ¿Qué tipo de estructura de datos recibe una función internamente cuando usamos *args?

- tuple

## Si definimos def mi_funcion(**kwargs):, ¿cómo accederíamos al valor de un argumento llamado 'nombre' pasado a la función?

- kwargs[]
- kwargs(*nombre)
- kwargs["nombre"]
- kwarts.nombre

## ¿Cuál es el orden correcto de los parámetros al definir una función que utiliza todos estos tipos?

A. def func(*args, a, b, **kwargs):

B. def func(a, b, *args, **kwargs):

C. def func(**kwargs, *args, a, b):

D. def func(a, **kwargs, *args):

## Tienes la lista precios = [10, 20, 30]. ¿Cómo la pasarías a una función calcular_total(*args) para que cada número sea un argumento independiente?

A. calcular_total(precios[:])

B. calcular_total(precios)

C. calcular_total(*precios)

D. calcular_total(**precios)

## ¿Es obligatorio usar los nombres 'args' y 'kwargs' después de los asteriscos?

A. Sí, son palabras reservadas.

B. No, puedes usar nombres como *detalles o **opciones.

C. Solo es obligatorio 'args'.

D. Solo en funciones de clase (métodos).

## Si ejecutas print(*[1, 2, 3]), ¿qué verás en la consola?

A. Un SyntaxError.

B. 1 2 3

C. [1, 2, 3]

D. (1, 2, 3)

## ¿Qué ocurre si intentas pasar un argumento posicional después de haber pasado uno nombrado (keyword)? Ejemplo: func(a=1, 2).

A. El valor 2 sobreescribe al 1.

B. Python lo asigna a *args.

C. Lanza un SyntaxError.

D. Funciona correctamente.