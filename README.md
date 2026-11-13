# EcoTech Solutions – Sistema de Gestión de Empleados

## Descripción del proyecto

EcoTech Solutions es un sistema desarrollado en Python que permite administrar información de empleados mediante una base de datos SQLite.

El proyecto incorpora autenticación de usuarios, programación orientada a objetos, validación de datos, manejo de errores y conexión segura a servicios externos mediante APIs para consultar información meteorológica y tipos de cambio de monedas internacionales.

Además, permite convertir sueldos desde pesos chilenos (CLP) a dólares estadounidenses (USD) y euros (EUR).

Este sistema fue desarrollado como parte de la **Evaluación Sumativa 3 (ES3)** de la asignatura Programación Orientada a Objeto Seguro de INACAP.

---

## Funcionalidades

### 1. Inicio de sesión

- Autenticación mediante usuario y contraseña.
- Contraseñas protegidas mediante PBKDF2-HMAC-SHA256.
- Generación de salt aleatorio para proteger las contraseñas.
- Visualización de asteriscos al ingresar la contraseña.
- Validación de credenciales.
- Límite de tres intentos de inicio de sesión.
- Comparación segura mediante `hmac.compare_digest`.
- Acceso al sistema únicamente después de iniciar sesión correctamente.

### 2. Gestión de empleados

El sistema permite:

- Registrar nuevos empleados.
- Buscar empleados mediante RUT.
- Actualizar información de empleados.
- Eliminar empleados registrados.
- Mostrar todos los empleados.
- Almacenar y consultar información mediante SQLite.

Se utilizan consultas SQL parametrizadas para reducir el riesgo de inyección SQL.

### 3. Validación del RUT chileno

Se implementó un módulo de validación de RUT que permite:

- Aceptar RUT con y sin puntos.
- Validar el dígito verificador mediante el algoritmo módulo 11.
- Rechazar RUT inválidos.
- Normalizar el formato del RUT.
- Evitar el registro de identificadores incorrectos.

La validación se integra con la clase `Empleado`.

### 4. Consulta del clima

El sistema utiliza la API Open-Meteo para consultar información meteorológica de Chillán, Chile.

La información incluye:

- Temperatura actual en grados Celsius.
- Humedad relativa.
- Estado del tiempo.
- Descripciones meteorológicas en español.

Se implementó procesamiento JSON, manejo de errores y conexión HTTPS.

### 5. Consulta de tipos de cambio

Se utiliza ExchangeRate-API para obtener tipos de cambio internacionales.

El sistema consulta:

- Dólar estadounidense (USD).
- Euro (EUR).
- Peso argentino (ARS).

Los valores se obtienen desde una API externa y pueden variar según su actualización.

### 6. Conversión de sueldos

El sistema incorpora dos modalidades de conversión.

**Conversión manual:**

- Ingresar un sueldo en pesos chilenos.
- Seleccionar dólares o euros.
- Consultar el tipo de cambio.
- Calcular y mostrar el monto convertido.

**Conversión de empleados registrados:**

- Buscar un empleado mediante su RUT.
- Obtener su sueldo desde SQLite.
- Seleccionar la moneda de destino.
- Consultar el tipo de cambio.
- Mostrar el sueldo original y convertido.

### 7. Validación de datos

Se implementaron validaciones para:

- Opciones incorrectas del menú.
- Entradas numéricas inválidas.
- Edades inferiores a 18 años.
- Sueldos negativos.
- Valores numéricos no finitos en las conversiones.
- Campos obligatorios vacíos.
- RUT chilenos incorrectos.
- Registros duplicados en la base de datos.

### 8. Manejo de errores

Se utilizan estructuras `try/except` para controlar:

- Problemas de conexión a internet.
- Fallos de servicios externos.
- Respuestas HTTP incorrectas.
- Datos JSON inválidos.
- Errores de autenticación.
- Errores de operaciones SQLite.
- Entradas incorrectas del usuario.

Los errores controlados se muestran mediante mensajes comprensibles para evitar interrupciones innecesarias.

---

## Tecnologías utilizadas

- Python 3.
- Programación Orientada a Objetos (POO).
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

---

## Acceso al sistema

Para ingresar al sistema EcoTech Solutions se dispone de las siguientes credenciales de demostración:

**Usuario:** `admin`

**Contraseña:** `admin1234567`

La cuenta de demostración se genera automáticamente cuando no existe el archivo `usuarios.json`.

Las contraseñas no se almacenan directamente en texto plano dentro del archivo JSON. Se utiliza PBKDF2-HMAC-SHA256 con salt aleatorio.

**Nota de seguridad:** Estas credenciales son exclusivamente académicas. La contraseña predeterminada está definida en el código fuente y debe reemplazarse antes de utilizar el sistema en un entorno real.

---

## Estructura del proyecto

```text
EcoTech-Solutions/
├── main.py
├── login.py
├── crear_usuario.py
├── empleado.py
├── basedatos.py
├── validar_rut.py
├── clima.py
├── monedas.py
├── api_segura.py
├── departamento.py
├── paciente.py
├── README.md
└── .gitignore
```

**Archivos generados localmente:**

- `ecotech.db`: base de datos SQLite de empleados.
- `usuarios.json`: datos de autenticación.
- `usuarios_respaldo.json`: archivo de respaldo de usuarios, cuando corresponda.

Estos archivos se mantienen excluidos del repositorio mediante `.gitignore`.

---

## Instalación y ejecución

### 1. Obtener el proyecto

Clonar el repositorio desde GitHub o abrirlo mediante GitHub Codespaces.

### 2. Instalar las dependencias

Ejecutar en la terminal:

```bash
python -m pip install pwinput
```

Para ejecutar el análisis estático de seguridad, instalar Bandit:

```bash
python -m pip install bandit
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

---

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

---

## Seguridad del sistema

Se implementaron diferentes mecanismos de seguridad para proteger el acceso, procesamiento y almacenamiento de información.

### 1. Protección de contraseñas

Se utiliza PBKDF2-HMAC-SHA256 con:

- 600.000 iteraciones.
- Salt aleatorio de 16 bytes.
- Comparación mediante `hmac.compare_digest`.
- Límite de tres intentos de autenticación.

Los verificadores de contraseñas se almacenan en `usuarios.json`, excluido del repositorio.

### 2. Validación de información

La clase `Empleado` incorpora propiedades y métodos de validación para controlar los datos ingresados.

Se verifica:

- RUT válido.
- Nombre obligatorio.
- Edad mínima.
- Sueldo no negativo.

El RUT se comprueba mediante el algoritmo módulo 11.

### 3. Protección de la base de datos

Se utiliza SQLite con consultas SQL parametrizadas.

Esto permite separar las instrucciones SQL de los valores ingresados por los usuarios, reduciendo el riesgo de inyección SQL.

También se implementa manejo de excepciones para las operaciones de base de datos.

### 4. Seguridad de servicios externos

Las conexiones a APIs se centralizan mediante el módulo `api_segura.py`.

Este módulo incorpora:

- Uso obligatorio de HTTPS.
- Restricción de dominios permitidos.
- Validación de las URL utilizadas.
- Rechazo de redirecciones automáticas.
- Tiempo máximo de espera de 10 segundos.
- Comprobación de respuestas HTTP.
- Procesamiento de respuestas JSON.

Los dominios autorizados son:

- `api.open-meteo.com`
- `open.er-api.com`

Estas medidas reducen riesgos asociados con conexiones a destinos no autorizados.

### 5. Análisis estático con Bandit

Se utilizó Bandit para detectar posibles problemas de seguridad en el código Python.

Durante una revisión inicial se identificaron cuatro advertencias B310 relacionadas con el uso de `urlopen()`.

Para solucionarlas se implementó el módulo `api_segura.py`, que centraliza las consultas HTTPS y restringe los destinos permitidos.

Después de aplicar las correcciones se ejecutó nuevamente Bandit.

**Comando utilizado:**

```bash
python -m bandit -r . -x ./.venv,./venv,./__pycache__
```

**Resultados finales:**

| Indicador | Resultado |
|---|---|
| Líneas de código analizadas | 673 |
| Advertencias de gravedad baja | 0 |
| Advertencias de gravedad media | 0 |
| Advertencias de gravedad alta | 0 |
| Archivos omitidos | 0 |

**Resultado: No issues identified.**

Bandit no detectó problemas mediante sus reglas de análisis estático. Este resultado no garantiza la ausencia absoluta de vulnerabilidades.

---

## Uso de inteligencia artificial

Durante el desarrollo del proyecto se utilizó ChatGPT como herramienta de apoyo para analizar, modificar, mejorar y revisar el código Python.

### Actividades realizadas con apoyo de IA

1. Integración de la API de tipos de cambio.
2. Implementación de conversiones monetarias.
3. Integración de sueldos almacenados en SQLite con las conversiones.
4. Incorporación del estado del tiempo en la consulta meteorológica.
5. Mejoras en el manejo de errores HTTP y excepciones.
6. Revisión de la autenticación y protección de contraseñas.
7. Implementación de validación del RUT chileno.
8. Incorporación de validaciones adicionales para los empleados.
9. Revisión del manejo de errores de SQLite.
10. Implementación del módulo `api_segura.py`.
11. Corrección de advertencias detectadas mediante Bandit.
12. Actualización de la documentación del proyecto.

### Análisis y ajustes del código

El código propuesto mediante inteligencia artificial fue revisado e integrado progresivamente al proyecto existente.

Se realizaron pruebas mediante la terminal de GitHub Codespaces para comprobar el funcionamiento de las funcionalidades.

Entre las pruebas realizadas se encuentran:

- Inicio de sesión correcto.
- Registro y búsqueda de empleados.
- Actualización y eliminación de empleados.
- Validación de RUT correctos e incorrectos.
- Rechazo de edades inferiores a 18 años.
- Consulta de tipos de cambio.
- Conversión manual de sueldos.
- Conversión del sueldo de un empleado registrado.
- Consulta de temperatura, humedad y estado del tiempo de Chillán.
- Comprobación de persistencia de información mediante SQLite.
- Análisis de seguridad mediante Bandit.

### Justificación de decisiones técnicas

**Uso de SQLite:** Se mantuvo SQLite porque permite almacenar información localmente sin configurar un servidor adicional.

**Uso de APIs externas:** Se integraron servicios meteorológicos y financieros para proporcionar información útil en la gestión operativa y la conversión de sueldos.

**Protección de contraseñas:** Se utilizó PBKDF2-HMAC-SHA256 para dificultar la recuperación de contraseñas a partir de los verificadores almacenados.

**Validación del RUT:** Se incorporó el cálculo del dígito verificador para reducir el registro de identificadores incorrectos.

**Seguridad de APIs:** Se centralizaron las conexiones mediante `api_segura.py` para restringir destinos y controlar redirecciones.

**Manejo de excepciones:** Se mejoraron los mensajes de error y la recuperación ante fallos controlados.

**Uso de IA:** Las sugerencias se utilizaron como apoyo al desarrollo, comprobando su comportamiento mediante pruebas antes de incorporarlas al proyecto.

---

## Autor

Proyecto académico desarrollado para INACAP.

**Asignatura:** Programación Orientada a Objeto Seguro.

**Evaluación:** Evaluación Sumativa 3 – Unidad 3.

---

## Estado del proyecto

Las funcionalidades principales del sistema fueron implementadas y probadas mediante GitHub Codespaces.

El proyecto incluye:

- Gestión de empleados mediante SQLite.
- Autenticación segura de usuarios.
- Validación de RUT chileno.
- Consulta de información meteorológica.
- Consulta de tipos de cambio.
- Conversión de sueldos.
- Conexiones HTTPS con destinos restringidos.
- Manejo de excepciones.
- Análisis estático con Bandit sin advertencias detectadas.

**Estado: Funcionalidades principales implementadas y revisadas.**

El sistema corresponde a un proyecto académico y requiere revisiones adicionales antes de utilizarse en un entorno de producción.