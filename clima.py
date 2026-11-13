
import json
import ssl
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlsplit


def mostrar_clima():
    print("\n--- Clima actual de Santiago ---")

    
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-33.45&longitude=-70.66"
        "&current=temperature_2m,relative_humidity_2m"
    )

    try:
        partes = urlsplit(url)

        if (
            partes.scheme != "https"
            or partes.hostname != "api.open-meteo.com"
        ):
            raise ValueError("URL de API no permitida")

       
        contexto = ssl.create_default_context()

        with urlopen(
            url,
            timeout=10,
            context=contexto
        ) as respuesta:

            if respuesta.status != 200:
                print("Error: La API no respondió correctamente.")
                return

           
            contenido = respuesta.read().decode("utf-8")

        
        if not contenido.strip():
            print("Error: La API devolvió una respuesta vacía.")
            return

        datos = json.loads(contenido)

        if "current" not in datos:
            print("Error: No se encontraron datos del clima.")
            return

        clima = datos["current"]

        temperatura = clima["temperature_2m"]
        humedad = clima["relative_humidity_2m"]

        
        print(f"Temperatura: {temperatura} °C")
        print(f"Humedad: {humedad} %")

    except HTTPError as error:
        print(f"Error HTTP: {error.code}")

    except URLError as error:
        print(f"Error de conexión: {error.reason}")

    except (json.JSONDecodeError, UnicodeDecodeError):
        print("Error: La API no devolvió un JSON válido.")

    except (KeyError, TypeError, ValueError) as error:
        print(f"Error al procesar el clima: {error}")

    except TimeoutError:
        print("Error: La conexión tardó demasiado.")
