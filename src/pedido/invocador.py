from .comando import Comando


class Invocador:
    def __init__(self, comando: Comando) -> None:
        self.comando = comando

    def executar(self):
        self.comando.aplicar()
