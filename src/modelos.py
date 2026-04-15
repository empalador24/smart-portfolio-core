from dataclasses import dataclass
from typing import List

class CantidadInvalidaError(ValueError):
    """Error lanzado cuando la cantidad no es válida."""
    pass

@dataclass(frozen=True)
class Instrumento:
    ticker: str
    tipo: str
    sector: str

class Posicion:
    def __init__(self, instrumento: Instrumento, cantidad: float, precio_entrada: float):
        self.instrumento = instrumento
        self._cantidad = cantidad
        self.precio_entrada = precio_entrada

    @property
    def cantidad(self) -> float:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: float):
        if valor < 0:
            raise CantidadInvalidaError("La cantidad no puede ser negativa")
        self._cantidad = valor

    def calcular_valor_actual(self, precio_mercado: float) -> float:
        return self._cantidad * precio_mercado

    def calcular_ganancia_no_realizada(self, precio_actual: float) -> float:
        return (precio_actual - self.precio_entrada) * self._cantidad

    def __repr__(self):
        return f"Posicion({self.instrumento.ticker}, {self._cantidad} uds @ {self.precio_entrada})"
