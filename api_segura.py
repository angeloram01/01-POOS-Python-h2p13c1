
import json
from urllib.request import (
    Request,
    build_opener,
    HTTPSHandler,
    HTTPRedirectHandler
)
from urllib.parse import urlsplit


HOSTS_PERMITIDOS = {
    "api.open-meteo.com",
    "open.er-api.com"
}


class SinRedirecciones(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def consultar_api(url):
    partes = urlsplit(url)

    if (
        partes.scheme != "https"
        or partes.hostname not in HOSTS_PERMITIDOS
        or partes.username is not None
        or partes.password is not None
        or partes.port not in (None, 443)
    ):
        raise ValueError("La URL de la API no está permitida.")

    solicitud = Request(url, headers={
        "User-Agent": "EcoTech-Solutions/1.0"
    })

    cliente = build_opener(
        HTTPSHandler(),
        SinRedirecciones()
    )

    with cliente.open(solicitud, timeout=10) as respuesta:
        if respuesta.status != 200:
            raise ValueError("Respuesta inesperada de la API.")

        return json.load(respuesta)
