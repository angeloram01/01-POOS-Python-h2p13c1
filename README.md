# EcoTech Solutions – Sistema de Gestión de Empleados

## Descripción del proyecto

EcoTech Solutions es un sistema desarrollado en Python que permite administrar información de empleados mediante una base de datos SQLite.

El proyecto incorpora autenticación de usuarios, validación de datos, manejo de errores y conexión a servicios externos mediante APIs para consultar información meteorológica y tipos de cambio de monedas internacionales.

Además, permite convertir los sueldos de los empleados desde pesos chilenos (CLP) a dólares estadounidenses (USD) y euros (EUR).

Este sistema fue desarrollado como parte de la Evaluación Sumativa 3 (ES3) de la asignatura Programación Orientada a Objeto Seguro de INACAP.

## Funcionalidades

### 1. Inicio de sesión

- Autenticación mediante usuario y contraseña.
- Contraseñas protegidas mediante PBKDF2-HMAC-SHA256.
- Generación de salt aleatorio para proteger las contraseñas.
- Visualización de asteriscos al ingresar la contraseña.
- Validación de credenciales.
- Límite de tres intentos de inicio de sesión.
- Comparación segura de credenciales mediante `hmac.compare_digest`.
- Acceso a las funcionalidades únicamente después de iniciar sesión correctamente.

### 2. Gestión de empleados

- Registrar empleados.
- Buscar empleados mediante RUT.
- Actualizar información de empleados.
- Eliminar empleados.
- Mostrar todos los empleados registrados.
- Almacenar la información mediante SQLite.

Se utilizan consultas SQL parametrizadas para reducir el riesgo de inyección SQL.

### 3. Consulta del clima

- Conexión a la API Open-Meteo.
- Consulta de información meteorológica de Chillán, Chile.
- Obtención de temperatura, humedad y estado del tiempo.
- Procesamiento de respuestas JSON.
- Uso de conexiones HTTPS.
- Manejo de errores de conexión y procesamiento.
- Control de respuestas HTTP incorrectas.

### 4. Consulta de tipos de cambio

- Conexión a ExchangeRate-API.
- Consulta de tipos de cambio internacionales.
- Obtención de valores del dólar estadounidense (USD), euro (EUR) y peso argentino (ARS).
- Procesamiento de respuestas JSON.
- Validación de los datos recibidos.
- Manejo de errores de conexión.

Los tipos de cambio se obtienen desde el servicio externo y pueden variar según su actualización.

### 5. Conversión de sueldos

El sistema permite realizar conversiones monetarias mediante dos funcionalidades:

**Conversión manual:**
- Ingresar un sueldo en pesos chilenos.
- Seleccionar dólares o euros.
- Consultar el tipo de cambio mediante una API.
- Mostrar el sueldo convertido.

**Conversión de empleados registrados:**
- Buscar un empleado mediante su RUT.
- Obtener automáticamente su sueldo desde SQLite.
- Seleccionar la moneda de destino.
- Convertir el sueldo utilizando el tipo de cambio consultado.

### 6. Validación de datos

- Control de opciones inválidas del menú.
- Validación de entradas numéricas.
- Validación de edades mínimas de 18 años.
- Validación de sueldos no negativos y valores numéricos finitos.
- Validación de cargos permitidos.
- Validación de RUT chileno mediante cálculo del dígito verificador.
- Aceptación de RUT con y sin puntos.
- Normalización de RUT para mantener un formato consistente.
- Control de campos obligatorios.

### 7. Manejo de errores

Se implementaron estructuras `try/except` para controlar:

- Errores de conexión a internet.
- Fallos de servicios externos.
- Respuestas HTTP incorrectas.
- Datos JSON inválidos o incompletos.
- Entradas incorrectas del usuario.
- Errores de operaciones con SQLite.
- Problemas de autenticación.

Los errores controlados se muestran mediante mensajes comprensibles para evitar interrupciones innecesarias y reducir la exposición de información interna.

## Tecnologías utilizadas

- Python 3.
- SQLite.
- JSON.
- `urllib.request` y `urllib.error`.
- Open-Meteo API.
- ExchangeRate-API.
- `hashlib`, `hmac` y `secrets`.
- `pwinput`.
- Git y GitHub.
- GitHub Codespaces.
- Bandit para análisis estático de seguridad.

## Acceso al sistema

Para ingresar al sistema EcoTech Solutions, se dispone de las siguientes credenciales de demostración:

**Usuario:** `admin`

**Contraseña:** `admin1234567`

La cuenta de demostración se genera automáticamente cuando no existe el archivo de usuarios.

Las contraseñas no se almacenan directamente en texto plano dentro del archivo JSON, sino mediante un hash derivado con PBKDF2-HMAC-SHA256 y salt aleatorio.

**Nota de seguridad:** Estas credenciales son exclusivamente académicas. La contraseña predeterminada está definida en el código fuente, por lo que debe reemplazarse antes de utilizar el sistema en un entorno real.

## Estructura del proyecto

```text
EcoTech-Solutions/
├── main.py
├── login.py
├── crear_usuario.py
├── clima.py
├── monedas.py
├── validar_rut.py
├── basedatos.py
├── empleado.py
├── departamento.py
├── paciente.py
├── ecotech.db
├── README.md
└── .gitignore
```

El archivo `usuarios.json` almacena localmente los datos de autenticación y debe mantenerse excluido del repositorio mediante `.gitignore`.

## Instalación y ejecución

### 1. Obtener el proyecto

Clonar el repositorio desde GitHub o abrirlo mediante GitHub Codespaces.

### 2. Instalar la dependencia

```bash
python -m pip install pwinput
```

### 3. Configurar las credenciales

En una instalación nueva, el sistema genera automáticamente una cuenta de demostración al ejecutar `main.py`, siempre que no exista `usuarios.json`.

El archivo `crear_usuario.py` también forma parte del proyecto como herramienta de gestión de credenciales.

### 4. Ejecutar el sistema

```bash
python main.py
```

Ingresar el usuario y la contraseña correspondientes.

El sistema requiere conexión a internet para consultar las APIs externas.

## Menú principal

```text
===== EcoTech Solutions - Gestión =====

1.- Registrar empleado
2.- Buscar empleado por RUT
3.- Actualizar empleado
4.- Eliminar empleado
5.- Mostrar todos los empleados
6.- Mostrar el clima
7.- Consultar tipo de cambio
8.- Convertir sueldo a otra moneda
9.- Convertir sueldo de empleado por RUT
0.- Salir
```

## Seguridad del sistema

Se incorporaron diferentes mecanismos de seguridad para proteger el acceso y procesamiento de información.

### Protección de contraseñas

Se utiliza PBKDF2-HMAC-SHA256 con 600.000 iteraciones y salt aleatorio de 16 bytes.

Esto permite almacenar verificadores de contraseñas sin guardar directamente la contraseña original en el archivo de usuarios.

### Validación de información

Se incorporaron validaciones en la clase `Empleado` para controlar edades, cargos, sueldos y RUT.

La validación del RUT utiliza el algoritmo de módulo 11 para comprobar su dígito verificador.

### Protección de la base de datos

Se utilizan consultas SQL parametrizadas para separar las instrucciones SQL de los datos ingresados por los usuarios.

También se incorporaron controles de errores y tiempos de espera para las conexiones SQLite.

### Seguridad de servicios externos

Las consultas se realizan mediante HTTPS y utilizan tiempos de espera para evitar que el programa permanezca esperando indefinidamente.

Se controlan errores HTTP, fallos de conexión y problemas de procesamiento de respuestas.

### Análisis estático

Se utilizó Bandit como herramienta de apoyo para analizar posibles problemas de seguridad.

Durante una revisión anterior se identificó la advertencia B310 relacionada con el uso de `urlopen()`.

Esta advertencia requiere revisar la validación de las URL y el tratamiento de redirecciones. No se considera automáticamente resuelta por utilizar HTTPS.

## Uso de inteligencia artificial

Durante el desarrollo se utilizó ChatGPT como herramienta de apoyo para analizar, modificar y mejorar el código Python.

Las principales actividades realizadas con apoyo de IA fueron:

1. Integración de la API de tipos de cambio.
2. Implementación de conversiones monetarias.
3. Integración de sueldos almacenados en SQLite con la conversión de monedas.
4. Incorporación del estado del tiempo a la consulta meteorológica.
5. Mejoras en el manejo de errores HTTP y excepciones.
6. Revisión de la autenticación y protección de contraseñas.
7. Implementación de validación del RUT chileno.
8. Incorporación de validaciones adicionales para los empleados.
9. Revisión del manejo de errores de SQLite.

### Análisis y ajustes del código

El código propuesto mediante IA fue revisado e integrado progresivamente al proyecto existente.

Se realizaron pruebas desde la terminal de GitHub Codespaces para comprobar el funcionamiento de las funcionalidades.

Entre las pruebas realizadas se encuentran:

- Inicio de sesión correcto.
- Consulta de tipos de cambio.
- Conversión manual de sueldos.
- Conversión del sueldo de un empleado registrado.
- Consulta de temperatura, humedad y estado del tiempo de Chillán.
- Rechazo de edades inferiores a 18 años.
- Validación de RUT correctos e incorrectos.
- Registro y búsqueda de empleados mediante SQLite.
- Conservación de registros existentes después de modificar la conexión a la base de datos.

### Justificación de las decisiones técnicas

**Uso de SQLite:** Se mantuvo SQLite porque permite almacenar información localmente sin necesidad de configurar un servidor de base de datos adicional.

**Uso de APIs externas:** Se integraron servicios meteorológicos y financieros para proporcionar información útil para la planificación operativa y la gestión de pagos internacionales.

**Protección de contraseñas:** Se mantuvo PBKDF2-HMAC-SHA256 para dificultar la recuperación de contraseñas a partir de los verificadores almacenados.

**Validación del RUT:** Se incorporó el cálculo del dígito verificador para reducir el registro de identificadores incorrectos.

**Manejo de excepciones:** Se mejoraron los mensajes de error para evitar mostrar detalles internos y permitir que el sistema continúe funcionando ante fallos controlados.

**Uso de IA:** Las sugerencias se utilizaron como apoyo al desarrollo, revisando su comportamiento mediante pruebas antes de incorporarlas al proyecto.

## Autor

Proyecto académico desarrollado para INACAP.

Asignatura: Programación Orientada a Objeto Seguro.

Evaluación: Evaluación Sumativa 3 – Unidad 3.

## Estado del proyecto

Las funcionalidades principales de gestión de empleados, autenticación, consulta de APIs y conversión de monedas fueron implementadas y probadas mediante GitHub Codespaces.

El sistema corresponde a un proyecto académico y requiere revisiones adicionales antes de utilizarse en producción.