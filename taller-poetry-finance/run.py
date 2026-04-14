from taller_poetry_finance import convertir_usd_a_cop

precios_internacionales = [100, 50, 25.5, 10]
precios_locales = convertir_usd_a_cop(precios_internacionales)

print(f"Precios en USD: {precios_internacionales}")
print(f"Precios en COP: {precios_locales}")
