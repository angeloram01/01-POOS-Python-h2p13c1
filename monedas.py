
import math
from urllib.error import URLError, HTTPError
from api_segura import consultar_api


URL_MONEDAS = "https://open.er-api.com/v6/latest/CLP"


def obtener_tasas():
    datos = consultar_api(URL_MONEDAS)

    if datos.get("result") != "success":
        raise ValueError("La API no entregó datos válidos.")

    tasas = datos["rates"]

    if not isinstance(tasas, dict):
        raise ValueError("Formato de tasas inválido.")

    return tasas


def obtener_tasa(tasas, moneda):
    tasa = float(tasas[moneda])

    if not math.isfinite(tasa) or tasa <= 0:
        raise ValueError("Tipo de cambio inválido.")

    return tasa


def consultar_monedas():
    print("\n--- Tipos de cambio ---")

    try:
        tasas = obtener_tasas()

        print("1 peso chileno equivale a:")
        print(f"Dólar (USD): {obtener_tasa(tasas, 'USD'):.6f}")
        print(f"Euro (EUR): {obtener_tasa(tasas, 'EUR'):.6f}")
        print(f"Peso argentino (ARS): {obtener_tasa(tasas, 'ARS'):.6f}")

        print("\nConsulta realizada correctamente.")

    except (HTTPError, URLError, TimeoutError):
        print("Error: No se pudo conectar con la API.")

    except (ValueError, KeyError, TypeError, OverflowError):
        print("Error: La API entregó datos inválidos.")


def convertir_sueldo():
    print("\n--- CONVERSIÓN DE SUELDOS ---")

    try:
        sueldo = float(input("Ingrese sueldo en pesos chilenos: "))

        if not math.isfinite(sueldo) or sueldo <= 0:
            print("Error: El sueldo debe ser un número positivo y finito.")
            return

    except (ValueError, OverflowError):
        print("Error: Ingrese un sueldo numérico válido.")
        return

    convertir_monto(sueldo)


def convertir_monto(sueldo):
    print("\nSeleccione moneda:")
    print("1.- Dólar (USD)")
    print("2.- Euro (EUR)")

    opcion = input("Ingrese opción: ").strip()

    monedas = {
        "1": "USD",
        "2": "EUR"
    }

    if opcion not in monedas:
        print("Error: Moneda no válida.")
        return

    moneda = monedas[opcion]

    try:
        sueldo = float(sueldo)

        if not math.isfinite(sueldo) or sueldo < 0:
            print("Error: El sueldo no es válido.")
            return

        tasas = obtener_tasas()
        tasa = obtener_tasa(tasas, moneda)

        resultado = sueldo * tasa

        if not math.isfinite(resultado):
            print("Error: El resultado de la conversión no es válido.")
            return

        print(f"\nSueldo original: ${sueldo:,.0f} CLP")
        print(f"Sueldo convertido: {resultado:,.2f} {moneda}")

    except (HTTPError, URLError, TimeoutError):
        print("Error: No se pudo conectar con la API.")

    except (ValueError, KeyError, TypeError, OverflowError):
        print("Error: No se pudo procesar la conversión.")
