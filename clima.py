
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def mostrar_clima():
    print("\n--- Clima actual de Chillán ---")

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-36.6066&longitude=-72.1034"
        "&current=temperature_2m,relative_humidity_2m,weather_code"
        "&timezone=America%2FSantiago"
    )

    estados = {
        0: "Despejado",
        1: "Principalmente despejado",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Niebla",
        48: "Niebla con escarcha",
        51: "Llovizna ligera",
        53: "Llovizna moderada",
        55: "Llovizna intensa",
        61: "Lluvia ligera",
        63: "Lluvia moderada",
        65: "Lluvia intensa",
        71: "Nieve ligera",
        73: "Nieve moderada",
        75: "Nieve intensa",
        80: "Chubascos ligeros",
        81: "Chubascos moderados",
        82: "Chubascos intensos",
        95: "Tormenta"
    }

    try:
        with urlopen(url, timeout=10) as respuesta:
            if respuesta.status != 200:
                print("Error: Respuesta inesperada del servicio.")
                return

            datos = json.load(respuesta)

        clima = datos["current"]

        temperatura = clima["temperature_2m"]
        humedad = clima["relative_humidity_2m"]
        codigo = clima["weather_code"]

        estado = estados.get(codigo, "Estado no disponible")

        print(f"Temperatura: {temperatura} °C")
        print(f"Humedad: {humedad} %")
        print(f"Estado del tiempo: {estado}")

        print("\nConsulta realizada correctamente.")

    except HTTPError:
        print("Error: El servicio del clima no está disponible.")

    except (URLError, TimeoutError):
        print("Error: No se pudo conectar con el servicio.")

    except (ValueError, KeyError, TypeError):
        print("Error: Los datos del clima no son válidos.")
