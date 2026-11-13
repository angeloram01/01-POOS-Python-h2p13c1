
import re


def validar_rut(rut):
    rut = rut.strip().upper()

    # Aceptar RUT con o sin puntos
    patron = r"^(?:\d{1,2}\.\d{3}\.\d{3}|\d{7,8})-[0-9K]$"

    if not re.fullmatch(patron, rut):
        return False

    # Eliminar puntos y guion
    rut_limpio = rut.replace(".", "").replace("-", "")

    numero = rut_limpio[:-1]
    digito = rut_limpio[-1]

    # Calcular digito verificador
    suma = 0
    multiplicador = 2

    for cifra in reversed(numero):
        suma += int(cifra) * multiplicador
        multiplicador += 1

        if multiplicador > 7:
            multiplicador = 2

    resto = 11 - (suma % 11)

    if resto == 11:
        digito_correcto = "0"
    elif resto == 10:
        digito_correcto = "K"
    else:
        digito_correcto = str(resto)

    return digito == digito_correcto


def normalizar_rut(rut):
    return rut.strip().upper().replace(".", "")
