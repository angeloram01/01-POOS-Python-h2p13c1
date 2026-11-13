# EcoTech Solutions – Sistema de Gestión de Empleados

## Descripción del proyecto

EcoTech Solutions es un sistema desarrollado en Python que permite administrar información de empleados mediante una base de datos SQLite.

El proyecto incorpora autenticación de usuarios, validación de datos y conexión a una API externa para consultar información meteorológica de Santiago de Chile.

Este sistema fue desarrollado como parte de una actividad académica de INACAP.

## Funcionalidades

### 1. Inicio de sesión
- Autenticación mediante usuario y contraseña.
- Contraseñas protegidas mediante hash PBKDF2 con SHA-256.
- Visualización de asteriscos al ingresar la contraseña.
- Validación de credenciales.
- Límite de intentos de inicio de sesión.

### 2. Gestión de empleados
- Registrar empleados.
- Buscar empleados mediante RUT.
- Actualizar información de empleados.
- Eliminar empleados.
- Mostrar todos los empleados registrados.

Los datos se almacenan en una base de datos SQLite.

### 3. Consulta del clima
- Conexión a la API Open-Meteo.
- Consulta de temperatura y humedad de Santiago.
- Procesamiento de respuestas JSON.
- Uso de conexiones HTTPS.
- Manejo de errores de conexión y procesamiento.

### 4. Validación de datos
- Control de opciones inválidas del menú.
- Validación de entradas numéricas.
- Control de errores durante la ejecución.

## Tecnologías utilizadas

- Python 3
- SQLite
- JSON
- Open-Meteo API
- Git y GitHub
- GitHub Codespaces
- Bandit para análisis de seguridad

## Acceso al sistema

Para ingresar al sistema de gestión EcoTech Solutions, utiliza las siguientes credenciales de demostración:

**Usuario:** `admin`

**Contraseña:** `admin1234567`

El sistema dispone de autenticación de usuarios y almacenamiento seguro de contraseñas mediante hash PBKDF2.

La cuenta de demostración se genera automáticamente durante la configuración inicial del sistema.

**Nota:** Estas credenciales son exclusivamente para fines académicos y deben cambiarse antes de utilizar el sistema en un entorno real.

## Estructura del proyecto

```text
EcoTech-Solutions/
├── main.py
├── login.py
├── crear_usuario.py
├── clima.py
├── basedatos.py
├── empleado.py
├── departamento.py
├── paciente.py
├── ecotech.db
├── README.md
└── .gitignore
```

El archivo `usuarios.json` se genera localmente para almacenar los datos de autenticación y está excluido de Git.

## Instalación y ejecución

### 1. Obtener el proyecto

Clonar el repositorio desde GitHub o abrirlo mediante GitHub Codespaces.

### 2. Instalar la dependencia

```bash
python -m pip install pwinput
```

### 3. Crear un usuario

Si todavía no existe el archivo de usuarios, ejecutar:

```bash
python crear_usuario.py
```

Seguir las instrucciones de la terminal para crear las credenciales.

### 4. Ejecutar el sistema

```bash
python main.py
```

Ingresar el usuario y la contraseña registrados.

## Menú principal

```text
1.- Registrar empleado
2.- Buscar empleado por RUT
3.- Actualizar empleado
4.- Eliminar empleado
5.- Mostrar todos los empleados
6.- Mostrar el clima
0.- Salir
```

## Seguridad

El sistema incorpora las siguientes medidas:

- Contraseñas almacenadas mediante hash y salt.
- Archivo de usuarios excluido mediante `.gitignore`.
- Validación de entradas.
- Conexión HTTPS para consultar la API.
- Manejo de excepciones.
- Análisis estático de seguridad con Bandit.

El análisis de Bandit identificó una advertencia B310 relacionada con `urlopen()`, pendiente de revisión adicional respecto de las redirecciones.

## Autor

Proyecto académico desarrollado para INACAP.

## Estado del proyecto

Las funcionalidades principales fueron implementadas y probadas mediante la terminal de Python.
