class Usuario:
    def __init__(self, username: str, email: str, nombre: str):
        self.username = username
        self.email = email
        self.nombre = nombre

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "nombre": self.nombre,
        }


class Post:
    def __init__(self, titulo: str, contenido: str, autor: Usuario):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor  # es una instancia de la clase Usuario (también de la clase Post)
        self.estado = "borrador"

    def publicar(self):
        self.estado = "publicado"

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "estado": self.estado,
        }


from pprint import pprint

usuario = Usuario(username="juan123", email="juan@example.com", nombre="Juan")
post = Post("Mi primer post", "Este es el contenido", usuario)
pprint(post.to_dict())
post.publicar()
pprint(post.to_dict())
