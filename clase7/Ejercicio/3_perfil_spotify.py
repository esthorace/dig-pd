import json


class PerfilSpotify:
    def __init__(self, username: str, nombre_mostrar: str, es_premium: bool = False):
        self.username = username
        self.nombre_mostrar = nombre_mostrar
        self.es_premium = es_premium
        self.seguidores = 0
        self.playlists = []
        self.cancion_actual = None

    def reproducir_cancion(self, cancion: str):
        self.cancion_actual = cancion

    def pausar(self):
        self.cancion_actual = None

    def crear_playlist(self, nombre_playlist: str):
        self.playlists.append(nombre_playlist)

    def to_json(self) -> str:
        datos = {
            "username": self.username,
            "nombre_mostrar": self.nombre_mostrar,
            "es_premium": self.es_premium,
            "seguidores": self.seguidores,
            "playlists": self.playlists,
            "cancion_actual": self.cancion_actual,
        }
        return json.dumps(datos, indent=4, ensure_ascii=False)
