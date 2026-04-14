class Instrumento:
    def __init__(self, ticker: str, nombre: str):
        self.ticker = ticker
        self.nombre = nombre

    def __repr__(self):
        return f"Instrumento({self.ticker})"


class Posicion:
    def __init__(self, instrumento: Instrumento, cantidad: float, precio_compra: float):
        self.instrumento = instrumento
        self.cantidad = cantidad
        self.precio_compra = precio_compra

    def valor_total(self) -> float:
        return self.cantidad * self.precio_compra

    def __repr__(self):
        return f"Posicion({self.instrumento.ticker}, {self.cantidad} unidades @ {self.precio_compra})"
