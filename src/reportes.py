# src/reportes.py

class ReportadorFinanciero:
    def imprimir_resumen(self, portafolio):
        print("=== Resumen del Portafolio ===")
        for posicion in portafolio.posiciones:
            print(posicion)