
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def consultar_monedas():
    print("\n--- Tipos de cambio ---")

    url = "https://open.er-api.com/v6/latest/CLP"

    try:
        with urlopen(url, timeout=10) as respuesta:
            datos = json.load(respuesta)

        if datos.get("result") != "success":
            print("No se pudieron obtener los tipos de cambio.")
            return

        monedas = datos["rates"]

        print("1 peso chileno equivale a:")
        print(f"Dólar (USD): {monedas['USD']:.6f}")
        print(f"Euro (EUR): {monedas['EUR']:.6f}")
        print(f"Peso argentino (ARS): {monedas['ARS']:.6f}")

        print("\nConsulta realizada correctamente.")

    except (URLError, HTTPError, TimeoutError):
        print("Error: No se pudo conectar con la API.")

    except (ValueError, KeyError, TypeError):
        print("Error: La API entregó datos inválidos.")

def convertir_sueldo():
    print("\n--- CONVERSIÓN DE SUELDOS ---")

    try:
        sueldo = float(input("Ingrese sueldo en pesos chilenos: "))

        if sueldo <= 0:
            print("Error: El sueldo debe ser mayor a cero.")
            return

        print("1.- Dólar (USD)")
        print("2.- Euro (EUR)")

        opcion = input("Seleccione moneda: ").strip()

        monedas = {"1": "USD", "2": "EUR"}

        if opcion not in monedas:
            print("Error: Moneda no válida.")
            return

        moneda = monedas[opcion]

        with urlopen("https://open.er-api.com/v6/latest/CLP", timeout=10) as respuesta:
            datos = json.load(respuesta)

        if datos.get("result") != "success":
            print("Error al consultar el tipo de cambio.")
            return

        tasa = datos["rates"][moneda]
        convertido = sueldo * tasa

        print(f"\nSueldo original: ${sueldo:,.0f} CLP")
        print(f"Sueldo convertido: {convertido:,.2f} {moneda}")

    except ValueError:
        print("Error: Ingrese un sueldo numérico válido.")
    except (URLError, HTTPError, TimeoutError):
        print("Error de conexión con la API.")
    except (KeyError, TypeError):
        print("Error: No se pudo procesar el tipo de cambio.")


def convertir_monto(sueldo):
    print("\nSeleccione moneda:")
    print("1.- Dólar (USD)")
    print("2.- Euro (EUR)")

    opcion = input("Ingrese opción: ").strip()

    monedas = {"1": "USD", "2": "EUR"}

    if opcion not in monedas:
        print("Error: Moneda no válida.")
        return

    try:
        with urlopen(
            "https://open.er-api.com/v6/latest/CLP",
            timeout=10
        ) as respuesta:
            datos = json.load(respuesta)

        if datos.get("result") != "success":
            print("Error al consultar la API.")
            return

        moneda = monedas[opcion]
        tasa = datos["rates"][moneda]

        resultado = sueldo * tasa

        print(f"\nSueldo original: ${sueldo:,.0f} CLP")
        print(f"Sueldo convertido: {resultado:,.2f} {moneda}")

    except (URLError, HTTPError, TimeoutError):
        print("Error: No se pudo conectar con la API.")
    except (ValueError, KeyError, TypeError):
        print("Error: No se pudo procesar la conversión.")
