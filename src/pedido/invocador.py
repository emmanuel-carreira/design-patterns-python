from .comando import Comando


class Invocador:
    def __init__(self, comando: Comando):
        self.comando = comando

    def executar(self):
        self.comando.aplicar()
