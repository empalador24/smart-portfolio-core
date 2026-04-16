from src.modelos import Instrumento, Posicion
from src.portafolio import Portafolio
from src.reportes import ReportadorFinanciero

def main():
    # Crear instrumentos
    aapl = Instrumento(ticker="AAPL", tipo="Acción", sector="Tecnología")
    us10y = Instrumento(ticker="US10Y", tipo="Bono", sector="Gobierno")

    # Crear posiciones
    pos1 = Posicion(instrumento=aapl, cantidad=10, precio_entrada=175.50)
    pos2 = Posicion(instrumento=us10y, cantidad=5, precio_entrada=98.00)

    # Armar portafolio
    portafolio = Portafolio()
    portafolio.agregar_posicion(pos1)
    portafolio.agregar_posicion(pos2)

    # Imprimir resumen
    reportador = ReportadorFinanciero()
    reportador.imprimir_resumen(portafolio)

if __name__ == "__main__":
    main()
