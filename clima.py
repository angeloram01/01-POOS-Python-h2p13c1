import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def mostrar_clima():
    print("\n--- Clima actual de Chillán ---")

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-36.6066&longitude=-72.1034"
        "&current=temperature_2m,relative_humidity_2m"
        "&timezone=America%2FSantiago"
    )

    try:
        with urlopen(url, timeout=10) as respuesta:
            datos = json.load(respuesta)

        clima = datos["current"]

        temperatura = clima["temperature_2m"]
        humedad = clima["relative_humidity_2m"]

        print(f"Temperatura: {temperatura} °C")
        print(f"Humedad: {humedad} %")

    except (URLError, HTTPError, ValueError, KeyError) as error:
        print(f"Error al consultar el clima: {error}")
