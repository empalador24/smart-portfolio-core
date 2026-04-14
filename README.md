# SmartPortfolio Core

Core bancario simulado de una fintech. Proyecto integrador del Seminario de Programación Backend para Ciencia de Datos — Maestría en Inteligencia de Negocios, Universidad Externado de Colombia.

## Integrantes

| Rol | Nombre |
|-----|--------|
| Arquitecto (Repository Owner) | Cristian Javier Oyola Tovar |
| Dev (Contributor) | Luis Torregroza |

## Requisitos

- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation)

## Setup

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd smart-portfolio-core

# 2. Instalar dependencias
poetry install

# 3. Configurar variables de entorno
cp .env.example .env
# Editar .env con los valores correspondientes

# 4. Ejecutar tests
poetry run pytest
```

## Estructura

```
smart-portfolio-core/
├── src/
│   ├── modelos.py          # Instrumento, Posicion
│   ├── portafolio.py       # Portafolio
│   ├── reportes.py         # ReportadorFinanciero
│   ├── providers.py        # MarketDataProvider, YahooFinanceClient
│   ├── value_objects.py    # Ticker, Quantity, Money
│   ├── dto.py              # OrdenCompraDTO
│   ├── config.py           # Settings
│   └── async_client.py     # AsyncHttpClient
└── tests/
    ├── conftest.py
    └── test_models.py
```

## Referencia

https://wilmerpineda.github.io/seminario-backend-mine/
