
import sqlite3


class BaseDatos:
    def __init__(self, nombre_db="ecotech.db"):
        self.nombre_db = nombre_db
        self.inicializar_base_datos()

    def conectar(self):
        try:
            conexion = sqlite3.connect(
                self.nombre_db,
                timeout=10
            )

            conexion.execute("PRAGMA busy_timeout = 10000")

            return conexion

        except sqlite3.Error:
            print("Error: No se pudo conectar con la base de datos.")
            return None

    def inicializar_base_datos(self):
        conexion = self.conectar()

        if conexion is None:
            return

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleados (
                    rut TEXT PRIMARY KEY NOT NULL,
                    nombre TEXT NOT NULL,
                    edad INTEGER NOT NULL CHECK(edad >= 18),
                    cargo TEXT NOT NULL,
                    sueldo REAL NOT NULL CHECK(sueldo >= 0)
                )
            """)

            conexion.commit()

        except sqlite3.Error:
            print("Error: No se pudo inicializar la base de datos.")

        finally:
            conexion.close()
