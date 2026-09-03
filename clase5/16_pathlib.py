from pathlib import Path

# print(Path(__file__).resolve())
# print(Path(__file__).resolve().parent)
# print(Path(__file__).resolve().parent.parent)

ruta = Path(__file__).resolve().parent

with open(ruta / "16-test.txt", "w") as f:
    f.write("Python\n")
    f.write("Django\n")
