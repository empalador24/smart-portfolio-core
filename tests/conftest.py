import pytest
from src.modelos import Instrumento, Posicion
from src.portafolio import Portafolio

@pytest.fixture
def instrumento_test():
    return Instrumento(ticker="TSLA", tipo="Acción", sector="Tecnología")

@pytest.fixture
def portafolio_vacio():
    return Portafolio()

@pytest.fixture
def posicion_aapl():
    instrumento = Instrumento(ticker="AAPL", tipo="Acción", sector="Tecnología")
    return Posicion(instrumento=instrumento, cantidad=10, precio_entrada=150.0)
