import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def guardar():
    with open("14-test.txt", "w") as f:
        f.write("Python\n")
        f.write("Django\n")
        logging.debug("✅ Archivo guardado exitosamente")


def leer():
    try:
        with open("14-test.txt", "r") as f:
            contenido = f.read()
            logging.debug("✅ Archivo leído exitosamente")
    except FileNotFoundError:
        logging.error("🚨  El archivo no existe")
    except Exception as e:
        logging.critical(f"Error inesperado: {repr(e)}")
    else:
        print(contenido)
        logging.info("✅ Se imprimió el contenido")


def main():
    guardar()
    leer()


main()
