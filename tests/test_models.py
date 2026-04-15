import pytest
from src.modelos import Instrumento, Posicion, CantidadInvalidaError
from src.portafolio import Portafolio, PosicionNoExisteError

# ─── A) Tests parametrizados de PnL ───────────────────────────────────────────
@pytest.mark.parametrize(
    "precio_entrada, precio_actual, cantidad, esperado",
    [
        (100, 150, 10, 500),
        (200, 180, 5, -100),
        (50,  50,  7,   0),
    ],
)
def test_calculo_pnl(precio_entrada, precio_actual, cantidad, esperado, instrumento_test):
    posicion = Posicion(
        instrumento=instrumento_test,
        cantidad=cantidad,
        precio_entrada=precio_entrada,
    )
    pnl = posicion.calcular_ganancia_no_realizada(precio_actual=precio_actual)
    assert pnl == pytest.approx(esperado)

# ─── B) Unhappy path: cantidad negativa ───────────────────────────────────────
def test_crear_posicion_negativa_lanza_error(instrumento_test):
    posicion = Posicion(instrumento=instrumento_test, cantidad=10, precio_entrada=100)
    with pytest.raises(CantidadInvalidaError):
        posicion.cantidad = -10

# ─── C) Unhappy path: remover ticker inexistente ──────────────────────────────
def test_remover_activo_inexistente_lanza_error(portafolio_vacio):
    with pytest.raises(PosicionNoExisteError):
        portafolio_vacio.remover_posicion(ticker="NFLX")

# ─── D) Test de cambio de estado del portafolio ───────────────────────────────
def test_agregar_posicion_cambia_estado(portafolio_vacio, posicion_aapl):
    assert len(portafolio_vacio.posiciones) == 0
    portafolio_vacio.agregar_posicion(posicion_aapl)
    assert len(portafolio_vacio.posiciones) == 1
    assert portafolio_vacio.posiciones[0].instrumento.ticker == "AAPL"

# ─── E) Test de remover posición existente ────────────────────────────────────
def test_remover_posicion_existente(portafolio_vacio, posicion_aapl):
    portafolio_vacio.agregar_posicion(posicion_aapl)
    portafolio_vacio.remover_posicion(ticker="AAPL")
    assert len(portafolio_vacio.posiciones) == 0

# ─── F) Tests de métodos adicionales de Posicion ─────────────────────────────
def test_calcular_valor_actual(instrumento_test):
    posicion = Posicion(instrumento=instrumento_test, cantidad=10, precio_entrada=100)
    assert posicion.calcular_valor_actual(precio_mercado=200) == pytest.approx(2000)

def test_cantidad_getter(instrumento_test):
    posicion = Posicion(instrumento=instrumento_test, cantidad=5, precio_entrada=50)
    assert posicion.cantidad == 5

def test_cantidad_setter_valido(instrumento_test):
    posicion = Posicion(instrumento=instrumento_test, cantidad=5, precio_entrada=50)
    posicion.cantidad = 10
    assert posicion.cantidad == 10

def test_repr_posicion(instrumento_test):
    posicion = Posicion(instrumento=instrumento_test, cantidad=5, precio_entrada=50)
    assert "TSLA" in repr(posicion)
