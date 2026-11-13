
import hashlib
import hmac
import json
import secrets
import pwinput
from pathlib import Path

ARCHIVO = Path(__file__).with_name("usuarios.json")

USUARIO_DEMO = "admin"
CLAVE_DEMO = "admin1234567"


def crear_admin_demo():
    
    if ARCHIVO.exists():
        return

    salt = secrets.token_bytes(16)

    hash_clave = hashlib.pbkdf2_hmac(
        "sha256",
        CLAVE_DEMO.encode("utf-8"),
        salt,
        600000
    )

    datos = {
        "usuario": USUARIO_DEMO,
        "salt": salt.hex(),
        "hash": hash_clave.hex()
    }

    try:
        with open(ARCHIVO, "x", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)
    except FileExistsError:
        return

    print("Cuenta de demostración configurada.")


def verificar_login():
    print("\n=== INICIO DE SESION ===")

    try:
        crear_admin_demo()

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        usuario_guardado = datos["usuario"]
        salt = bytes.fromhex(datos["salt"])
        hash_guardado = bytes.fromhex(datos["hash"])

    except (OSError, ValueError, KeyError, TypeError):
        print("Error al cargar las credenciales.")
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
