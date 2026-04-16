from src.portafolio import Portafolio

class ReportadorFinanciero:
    def imprimir_resumen(self, portafolio: Portafolio) -> None:
        print("=" * 40)
        print("   RESUMEN DEL PORTAFOLIO SmartPortfolio")
        print("=" * 40)
        for pos in portafolio.posiciones:
            print(f"  {pos.instrumento.ticker} | {pos.instrumento.tipo} | {pos.instrumento.sector}")
            print(f"    Cantidad: {pos.cantidad} | Precio entrada: ${pos.precio_entrada}")
        print("=" * 40)
