
import hashlib
import hmac
import json
import pwinput
from pathlib import Path

ARCHIVO = Path(__file__).with_name("usuarios.json")


def verificar_login():
    print("\n=== INICIO DE SESION ===")

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        usuario_guardado = datos["usuario"]
        salt = bytes.fromhex(datos["salt"])
        hash_guardado = bytes.fromhex(datos["hash"])

    except (OSError, ValueError, KeyError, TypeError):
        print("Error: No se pudo cargar el usuario.")
        return False

    for intento in range(3):
        usuario = input("Usuario: ").strip()
        clave = pwinput.pwinput(
            prompt="Contraseña: ",
            mask="*"
        )

        if not usuario or not clave:
            print("Debe completar ambos campos.")
            continue

        if len(usuario) > 30 or len(clave) > 128:
            print("Datos demasiado largos.")
            continue

        hash_ingresado = hashlib.pbkdf2_hmac(
            "sha256",
            clave.encode("utf-8"),
            salt,
            600000
        )

        usuario_valido = hmac.compare_digest(
            usuario.encode("utf-8"),
            usuario_guardado.encode("utf-8")
        )

        clave_valida = hmac.compare_digest(
            hash_ingresado,
            hash_guardado
        )

        if usuario_valido and clave_valida:
            print("Acceso autorizado.")
            return True

        print("Credenciales incorrectas.")

    print("Demasiados intentos fallidos.")
    return False
