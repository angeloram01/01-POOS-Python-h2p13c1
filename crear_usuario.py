
import hashlib
import secrets
import getpass
import json
from pathlib import Path

ARCHIVO = Path(__file__).with_name("usuarios.json")

usuario = input("Nuevo usuario: ").strip()
clave = getpass.getpass("Nueva contraseña: ")

if not usuario or len(usuario) > 30:
    print("Usuario inválido.")
elif len(clave) < 12:
    print("La contraseña debe tener al menos 12 caracteres.")
elif ARCHIVO.exists():
    print("Ya existe un usuario configurado.")
else:
    salt = secrets.token_bytes(16)

    hash_clave = hashlib.pbkdf2_hmac(
        "sha256",
        clave.encode("utf-8"),
        salt,
        600000
    )

    datos = {
        "usuario": usuario,
        "salt": salt.hex(),
        "hash": hash_clave.hex()
    }

    with open(ARCHIVO, "x", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

    print("Usuario creado correctamente.")
