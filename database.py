import sqlite3
from paciente import Paciente

def inicializar_base_datos():
    """Crea la tabla de pacientes si no existe."""
    conexion = sqlite3.connect("clinica.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            rut TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            prevision TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

def obtener_todos_los_pacientes() -> list[Paciente]:
    """Retorna una lista de objetos Paciente desde la base de datos."""
    conexion = sqlite3.connect("clinica.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT rut, nombre, edad, prevision FROM pacientes")
    filas = cursor.fetchall()
    conexion.close()
    
    lista_pacientes = []
    for fila in filas:
        # Reconstruimos el objeto Paciente usando las validaciones que ya tienes
        paciente = Paciente(fila[0], fila[1], fila[2], fila[3])
        lista_pacientes.append(paciente)
    return lista_pacientes

def insertar_paciente(paciente: Paciente):
    """Guarda un nuevo paciente en la base de datos."""
    conexion = sqlite3.connect("clinica.db")
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO pacientes (rut, nombre, edad, prevision)
        VALUES (?, ?, ?, ?)
    """, (paciente.rut, paciente.nombre, paciente.edad, paciente.prevision))
    conexion.commit()
    conexion.close()

def buscar_paciente_por_rut(rut: str) -> Paciente | None:
    """Busca un paciente por su RUT en la base de datos."""
    conexion = sqlite3.connect("clinica.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT rut, nombre, edad, prevision FROM pacientes WHERE rut = ?", (rut,))
    fila = cursor.fetchone()
    conexion.close()
    
    if fila:
        return Paciente(fila[0], fila[1], fila[2], fila[3])
    return None

def eliminar_paciente_db(rut: str):
    """Elimina un paciente de la base de datos por su RUT."""
    conexion = sqlite3.connect("clinica.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM pacientes WHERE rut = ?", (rut,))
    conexion.commit()
    conexion.close()