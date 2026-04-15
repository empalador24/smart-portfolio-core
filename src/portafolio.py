from typing import List
from src.modelos import Posicion

class PosicionNoExisteError(Exception):
    """Error lanzado cuando se intenta operar sobre un ticker que no existe."""
    pass

class Portafolio:
    def __init__(self):
        self.posiciones: List[Posicion] = []

    def agregar_posicion(self, posicion: Posicion) -> None:
        self.posiciones.append(posicion)

    def remover_posicion(self, ticker: str) -> None:
        for pos in self.posiciones:
            if pos.instrumento.ticker == ticker:
                self.posiciones.remove(pos)
                return
        raise PosicionNoExisteError(f"El ticker '{ticker}' no existe en el portafolio")
