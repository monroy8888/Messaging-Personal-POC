# Proyecto de Procesamiento de Datos con FastAPI, RabbitMQ, Flask API, y MySQL

## Descripción
Este proyecto demuestra cómo crear una herramienta de procesamiento de datos utilizando los siguientes componentes:

- **FastAPI:** Utilizado como el motor principal para recibir y procesar solicitudes HTTP.
- **RabbitMQ:** Actúa como un intermediario para la comunicación asíncrona entre diferentes partes del sistema.
- **Flask API:** Ofrece endpoints para enviar datos al sistema.
- **MySQL:** Base de datos relacional utilizada para almacenar y recuperar datos.

## Configuración del Entorno
Asegúrate de tener Docker y Docker Compose instalados. Luego, ejecuta:

```bash docker-compose up -d```

## Proceso de Prueba de Concepto

### 1. Consumir Mensajes de RabbitMQ con FastAPI

#### Endpoint en FastAPI
- **Descripción:** Consume mensajes desde RabbitMQ y procesa los datos utilizando Pandas o PySpark.
- **Endpoint:** `/consume-data`
- **Cómo Probar:**
  1. Envía mensajes a la cola de RabbitMQ desde Flask API.
  2. Accede al endpoint FastAPI para consumir y procesar esos mensajes.

### 2. Envío de Datos a RabbitMQ desde API Flask

#### Endpoint en Flask API
- **Descripción:** Envia datos a la cola de RabbitMQ.
- **Endpoint:** `/send-data`
- **Cómo Probar:**
  1. Envía datos a través de este endpoint.
  2. Verifica que los datos lleguen a la cola de RabbitMQ.

### 3. Procesamiento de Datos en FastAPI

#### Endpoint en FastAPI
- **Descripción:** Procesa datos utilizando Pandas o PySpark.
- **Endpoint:** `/process-data`
- **Cómo Probar:**
  1. Consume datos desde RabbitMQ o envía datos directamente al endpoint.
  2. Realiza operaciones de procesamiento con Pandas o PySpark.

### 4. Interacción con la Base de Datos MySQL

#### Conexión y Operaciones
- **Descripción:** Conéctate a MySQL desde Flask o FastAPI y realiza operaciones CRUD.
- **Cómo Probar:**
  1. Conéctate a la base de datos desde Flask o FastAPI.
  2. Recupera y almacena datos en la base de datos.

### 5. Ejecución de PySpark en Contenedor

#### Contenedor Adicional con PySpark
- **Descripción:** Ejecuta tareas de procesamiento de datos distribuido utilizando PySpark.
- **Cómo Probar:**
  1. Crea un contenedor adicional con PySpark.
  2. Utiliza el contenedor para ejecutar tareas de procesamiento de datos distribuido.

### 6. Flujo de Procesamiento Completo

- **Descripción:** Diseña un flujo completo que abarque todos los componentes.
- **Cómo Probar:**
  1. Genera datos o recíbelos desde Flask API.
  2. Envía los datos a RabbitMQ.
  3. Consume y procesa los datos con FastAPI.
  4. Almacena o envía los resultados según sea necesario.


