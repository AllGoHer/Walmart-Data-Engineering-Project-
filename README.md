# Walmart-Data-Engineering-Project-
________________________________________________________________________________________________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/56a9f21e-ef95-4f25-a48e-ff13e14e8ac9)

________________________________________________________________________________________________________________________________________________________________________________________________________________
## 🛒 Proyecto End-to-End de Ingeniería de Datos - Walmart

![image](https://img.shields.io/badge/Airflow-2.7.3-blue?logo=apache-airflow) ![image](https://img.shields.io/badge/dbt-1.12.3-orange?logo=dbt) ![image](https://img.shields.io/badge/Databricks-Lakehouse-red?logo=databricks) ![image](https://img.shields.io/badge/AWS-S3-yellow?logo=amazon-aws) ![image](https://img.shields.io/badge/Docker-Containers-blue?logo=docker) ![image](https://img.shields.io/badge/PostgreSQL-OLTP-blue?logo=postgresql)

### 🎯 Descripción General

Este es un proyecto completo de Ingeniería de Datos que simula un pipeline de datos real de Walmart. Cubre todo el ciclo de vida de los datos, desde la ingesta incremental hasta la transformación, pruebas y orquestación, utilizando herramientas modernas y mejores prácticas de la industria.

**¿Qué vamos a construir?**

- Una base de datos OLTP (PostgreSQL) que simula los datos operacionales de Walmart

- Pipelines de ingesta incremental hacia un Lakehouse en Databricks

- Modelos dbt para capas Silver (depurada) y Gold (lista para negocio)

- Dimensiones de Cambio Lento (SCD Tipo 2) para seguimiento histórico

- Pipelines basados en metadatos para escalabilidad

- Orquestación con Apache Airflow y Docker

- Integración con AWS S3 para fuentes de datos externas




**¿Qué vas a aprender?**

✅ Ingesta incremental de datos

✅ Pipelines basados en metadatos

✅ Dimensiones de Cambio Lento (SCD Tipo 2)

✅ Esquema en Estrella (Star Schema)

✅ Pruebas de calidad con dbt

✅ Modelos efímeros (Ephemeral) en dbt

✅ Orquestación con Airflow

✅ Integración continua con Databricks

✅ Despliegue en contenedores Docker.

_______________________________________________________________________________________________________________________________________________________________________________________________________________

### 🏗️ Arquitectura del Proyecto


![image](https://github.com/user-attachments/assets/0c5c058a-bec5-4cde-8af4-8fcf5df366d2)


________________________________________________________________________________________________________________________________________________________________________________________________________________

### 🧰 Stack Tecnológico


![image](https://github.com/user-attachments/assets/769401e5-29e6-4f0c-9e47-eab7ce7cd32c)

________________________________________________________________________________________________________________________________________________________________________________________________________________

### 📁 Estructura del Proyecto


![image](https://github.com/user-attachments/assets/2ba76c5b-40bd-4df2-9d5a-19d760d0c3b1)

______________________________________________________________________________________________________________________________________________________________________________________________________________

### 🔄 Flujo de Datos

![image](https://github.com/user-attachments/assets/dc835456-479e-49b2-8166-e631e6009c4f)

__________________________________________________________________________________________________________________________________________________________________________________________________________________________

### 🌟 Características Principales

✅ Ingesta Incremental - Solo se cargan datos nuevos o modificados.

✅ Pipelines Basados en Metadatos - Configuración impulsada por metadatos, no código duro.

✅ Dimensiones de Cambio Lento (SCD Tipo 2) - Seguimiento histórico completo.

✅ Esquema en Estrella - Hechos y dimensiones listos para negocio.

✅ Pruebas en dbt - Calidad de datos en cada etapa.

✅ Modelos Efímeros - CTEs optimizados para transformaciones.

✅ Orquestación con Airflow - Automatización completa del pipeline.

✅ Entorno Dockerizado - Reproducible y portable.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

### 📋 Requisitos Previos

- Docker y Docker Compose

- Python 3.10+

- Git

- Workspace de Databricks (versión comunitaria gratuita funciona)

- Cuenta de AWS (para S3, opcional)

- Memoria RAM: 8GB+ (16GB recomendado)

- Disco: 20GB+ de espacio libre

____________________________________________________________________________________________________________________________________________________________________________________________________________________________
### 🚀 Guía de Instalación

**1. Clonar el Repositorio**

bash:

      git clone https://github.com/AllGoHer/Walmart-Data-Engineering-Project.git

      cd walmart_project

**2. Configurar el Entorno**

Crea un archivo .env en el directorio airflow/:

bash:

      cd airflow

      cp .env.example .env


Edita .env con tus credenciales:

env:

     # Databricks
     DATABRICKS_HOST=dbc-xxxxxxx.cloud.databricks.com
     DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/xxxxx
     DATABRICKS_TOKEN=dapi_xxxxxxxxxxxxx
     DATABRICKS_CATALOG=walmart
     DATABRICKS_SCHEMA=dbt_schema

     # Airflow
     FERNET_KEY=tu_fernet_key
     _AIRFLOW_WWW_USER_USERNAME=airflow
     _AIRFLOW_WWW_USER_PASSWORD=airflow

     # AWS (opcional)
     AWS_ACCESS_KEY_ID=AKIAXXXXXX
     AWS_SECRET_ACCESS_KEY=xxxxxx
     AWS_S3_BUCKET=tu-bucket

**3. Construir y Ejecutar Airflow**

bash:

     # Construir la imagen personalizada con dbt
     docker-compose build

     # Iniciar todos los servicios
     docker-compose up -d

     # Verificar que los contenedores están corriendo
     docker ps

___________________________________________________________________________________________________________________________________________________________________________________________________________________________     
Acceder a la UI de Airflow: http://localhost:8080

Usuario: airflow | Contraseña: airflow

___________________________________________________________________________________________________________________________________________________________________________________________________________________________

**4. Configurar dbt**

bash:

     # Verificar que dbt está instalado en el worker
     docker-compose exec airflow-worker dbt --version

     # Copiar profiles.yml a los contenedores
     docker cp ~/.dbt/profiles.yml airflow-airflow-worker-1:/home/airflow/.dbt/profiles.yml
     docker cp ~/.dbt/profiles.yml airflow-airflow-scheduler-1:/home/airflow/.dbt/profiles.yml

     # Probar la conexión
     docker-compose exec airflow-worker bash -c "cd /opt/airflow/dbt_project && dbt debug"


     
**5. Ejecutar el Pipeline**

bash:

     # Despausar el DAG
     docker-compose exec airflow-scheduler airflow dags unpause orchestrate

     # Ejecutar manualmente
     docker-compose exec airflow-scheduler airflow dags trigger orchestrate

     # Monitorear la ejecución
     docker-compose logs -f airflow-worker

____________________________________________________________________________________________________________________________________________________________________________________________________________________________
### 🔬 Etapas del Pipeline


**1. Ingesta Incremental de Datos**

- Utiliza Databricks Auto Loader

- Solo carga registros nuevos o modificados

- Almacena en formato Delta en la capa Bronze


**2. Capa Silver Técnica (dbt)**

- Limpieza y deduplicación

- Estandarización de tipos de datos

- Manejo de nulos

- Modelos incrementales


**3. Capa Silver Business (dbt)**

- Transformaciones de lógica de negocio

- Joins entre tablas

- Columnas derivadas (cálculos, banderas)

- Configuración basada en metadatos


**4. Capa Gold (Esquema en Estrella)**

- Dimensiones: SCD Tipo 2 (snapshots de dbt)

- Hechos: Datos transaccionales/métricas

- Modelos Efímeros: CTEs optimizados

**5. Pruebas y Calidad**

- Pruebas de dbt (unique, not-null, accepted values)

- Pruebas de frescura en fuentes

- Pruebas de lógica de negocio personalizadas

**6. Orquestación (Airflow)**

- DAG end-to-end

- Dependencias y reintentos de tareas

- Manejo de fallos y alertas

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

### 📋 Comandos Útiles

**Gestión de Contenedores**

bash:

     # Ver logs de todos los servicios
     docker-compose logs -f

     # Ver logs específicos del worker
     docker-compose logs -f airflow-worker

     # Reiniciar servicios
     docker-compose restart

     # Detener todo
     docker-compose down

     # Detener y eliminar volúmenes (limpieza total)
     docker-compose down -v



**Gestión del DAG**

bash:

     # Listar DAGs
     docker-compose exec airflow-scheduler airflow dags list

     # Ver errores de importación
     docker-compose exec airflow-scheduler airflow dags list-import-errors

     # Ver estado del DAG
     docker-compose exec airflow-scheduler airflow dags state orchestrate

     # Limpiar ejecuciones
     docker-compose exec airflow-scheduler airflow dags clear --run-id [RUN_ID] orchestrate

     # Ver logs de una tarea específica
     docker-compose exec airflow-scheduler airflow tasks logs orchestrate silver_technical 2026-09-07


**Diagnóstico**

bash:

     # Verificar instalación de dbt
     docker-compose exec airflow-worker dbt --version

     # Entrar al contenedor del worker
     docker-compose exec airflow-worker bash

     # Probar conexión a Databricks
     cd /opt/airflow/dbt_project && dbt debug

     # Ver contenido de profiles.yml
     docker-compose exec airflow-worker cat /home/airflow/.dbt/profiles.yml

___________________________________________________________________________________________________________________________________________________________________________________________________________________________
### 🔧 Solución de Problemas Comunes

| Problema	| Solución |
|-----------|----------|
| dbt: command not found | docker-compose exec -u 0 airflow-worker pip install dbt-core dbt-databricks |
| profiles.yml not found |	Re-copiar profiles.yml a todos los contenedores (scheduler, worker, dag-processor) |
| Connection test failed |	Ejecutar docker-compose exec airflow-worker bash → cd /opt/airflow/dbt_project → dbt debug |
| El DAG no aparece en la UI | docker-compose restart airflow-dag-processor airflow-scheduler |
| Errores de permisos en Windows | Ejecutar PowerShell como Administrador o configurar AIRFLOW_UID=50000 |
| Puerto 8080 ya está en uso | Cambiar ports: - "8081:8080" en docker-compose.yaml |
| Error de memoria insuficiente |	Aumentar memoria en Docker Desktop a 8GB+ |
| Databricks token expirado |	Generar nuevo token en Databricks y actualizar .env |

___________________________________________________________________________________________________________________________________________________________________________________________________________________________

### 📧 Contacto

* Tu Nombre - tu.email@ejemplo.com

* GitHub: @tuusuario

* LinkedIn: Tu Perfil

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

### ⭐ Apoya este Proyecto

Si este proyecto te ayudó, ¡dale una ⭐ en GitHub!

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

### 🔗 Enlaces Rápidos

- [Documentación de Apache Airflow](https://airflow.apache.org/docs/)

- [Documentación de dbt](https://docs.getdbt.com/?version=2)

- [Documentación de Databricks](https://docs.databricks.com/aws/en)

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

### 🚀 DESARROLLO WALMART PROJECT

Primero, creamos una carpeta y la vinculamos a Visual Studio Code.

Luego hacemos click en el icono de copilot para vincular con visual studio code y tu github.


![image](https://github.com/user-attachments/assets/7dabb3b7-e141-46b5-8337-9b69dc7eb3b6)

Luego, autorizamos

![image](https://github.com/user-attachments/assets/d49f4feb-54a0-4b20-aa7e-93e794dc0bcf)

Luego, colocamos nuestro password para confirmar.

![image](https://github.com/user-attachments/assets/33c4d434-0223-493d-a5b9-24c757996824)

Y permitimos abra el vínculo asociado.

Ahora, instalamos ghost desde la terminal de VSC.

Código:

       irm https://install.ghost.build/install.ps1 | iex

![image](https://github.com/user-attachments/assets/786ae046-b8d3-41cf-ada6-e63553d0163c)

Luego, solo presionamos enter a las siguientes consultas de autenticación y MCP.

![image](https://github.com/user-attachments/assets/e927d6f5-3d2e-4aaf-9deb-0c38a2ddbbea)

![image](https://github.com/user-attachments/assets/05001f33-b519-4ae3-836e-9b5af1f7da5e)

Luego, instalamos python UV.

Codigo:

       Pip install uv

Ahora, lo iniciamos.

Código: 

       uv init

![image](https://github.com/user-attachments/assets/81b16cba-8c43-450c-9c14-7c9039696a28)

Al ejecutar aparecerá todo esto en tu carpeta de proyecto.

![image](https://github.com/user-attachments/assets/5e51a1cf-3d61-4d40-af19-b3b348df9d70)


Creamos el entorno virtual del proyecto.

Código:

       python -m venv .venv


Código:

        .venv\Scripts\activate
   

![image](https://github.com/user-attachments/assets/c29bdf90-6858-4a72-95a6-c617d205408f)

Ahora, cargamos la carpeta walmart_dataset (disponible en el repositorio) a VSC.

![image](https://github.com/user-attachments/assets/bd8dd5d4-f5b0-4456-b06a-37bea0f7e963)

Crearemos nuestra base de datos walmart_db

Código:

        ghost create walmart_db

![image](https://github.com/user-attachments/assets/74bc95ab-090c-475c-abe2-d329aaf51bc4)

Ahora, en el proyecto creamos un archivo llamado .env con el siguiente código

Código:

        POSTGRES_CONN = postgresql://tsdbadmin:vzugx5qioc2sfhaj@iz0kkxxbbp.guhpu8gjll.db.ghost.build:5432/tsdb?sslmode=require

En la terminal creamos el api-key.

Código:

        ghost api-key create --name allgoher_api_walmart



![image](https://github.com/user-attachments/assets/f76da472-672b-4919-a784-adbe0d0469e3)

Para ver ahora que todo marcha bien, le hare una pregunta al IA Agent por el chat.

Consulta: 

          ¿Cuántas bases de datos tengo en mi fantasma? (ghost)

![image](https://github.com/user-attachments/assets/1411ead5-363a-4a64-adfe-e49652d6c358)

![image](https://github.com/user-attachments/assets/50ab64c4-f71a-46a9-83ff-8bddead7f6c2)

Si deseo ver la lista de archivos fantasmas creados lo haré con el siguiente código.

Código:

        ghost list

![image](https://github.com/user-attachments/assets/531cd6ef-7816-45fe-8737-72ab19e69342)


Solo hay uno.

Ahora, le daré una orden a mi IA Agent para que me cree un esquema y sus tablas.

Chat IA Agent:

               quiero que me crees tablas dentro de ghost walmart_db y, tambien quiero que me crees un esquema llamado "raw" dentro de mi walmart_db y crea tablas dentro de ese esquema usando mi script guardado en ddl (Walmart_schema.sql)

![image](https://github.com/user-attachments/assets/02c90554-790c-45a8-8c3d-3468d91c6ecf)

Chat IA Agent:

               quiero que insertes los datos csv dentro de cada tabla, tengo archivos almacenados en walmart_dataset. necesitas insertar los datos csv usando '\copy' o 'copy_expert' metodo.

![image](https://github.com/user-attachments/assets/050bf252-08a0-4281-b0fd-fefcfd77ac1a)

![image](https://github.com/user-attachments/assets/c1f005f8-88c4-4577-bf5c-7877f7ed47f2)

![image](https://github.com/user-attachments/assets/ca37f53f-db2b-4008-aa2b-a1643013bd69)

Chat IA Agent:

               quiero crear un fork de mi ghost walmart_db


![image](https://github.com/user-attachments/assets/b534c22b-3b13-41a4-9e71-5b910c601f04)

Para confirmar vamos al terminal y vemos las lista de fantasmas.

Código:

        ghost list

![image](https://github.com/user-attachments/assets/94503961-c7b5-40b3-b24d-43412ec64e2b)

Ahora haremos una consulta para elwalmart_db_fork

Consulta:

          ¿cuál es el primary key en la tabla store dentro de walmart_db_fork?

![image](https://github.com/user-attachments/assets/38e58ab7-19e4-4948-8c0f-63d1ccf2823c)

Consulta:

          cuantos productos tengo en mi tabla productos dentro de mi raw schema en mi walmart_db

![image](https://github.com/user-attachments/assets/905d3966-da08-4bd0-b195-518a8379e4ee)

Ahora, en Databricks crearé un catálogo llamado Walmart.

![image](https://github.com/user-attachments/assets/0a96f6c4-bfc0-4d71-ac11-af16507caa72)

Luego nos dirigimos a workspace y crearé un notebook.

![image](https://github.com/user-attachments/assets/e970f184-610c-44cf-be6f-97bd0df2179d)
____________________________________________________________________________________________________________________________________________________________________________________________________________________________

## STAR SCHEMA


### BRONZE LAYER
___________________________________________________________________________________________________________________________________________________________________________________________________________________________
Ahora, creamos el esquema bronce.

![image](https://github.com/user-attachments/assets/68509cbd-e6dc-4fe6-83ee-702b4b709533)

![image](https://github.com/user-attachments/assets/99b9303a-9e84-4fbb-9371-b1208cd4d5d9)

Ahora, haremos la ingestión de datos con Databricks de modo CDC y con tablas delta en la capa bronce.

![image](https://github.com/user-attachments/assets/5f0d9efc-3d35-461c-87ed-d0bec3cdb3b3)

Regresamos a VSC para conectar nuestra base de datos.

Código:

       ghost connect waltmart_db


![image](https://github.com/user-attachments/assets/3712b834-5729-4f98-a348-d5411205f77c)

Ahora, creamos la carpeta una carpeta llamada connection en el proyecto y pasamos el código de conexión postgresql.

![image](https://github.com/user-attachments/assets/3876bdf1-c1d3-49ea-a773-ff4d83bdb93c)

Y guardamos.

Luego, nos dirigimos a Databricks en la sección de Data Ingestion y seleccionamos PostgreSQL 

![image](https://github.com/user-attachments/assets/14a9be3c-2fa3-4d27-a0b7-caf36b26d6cd)

Ahora creamos una conexión.

![image](https://github.com/user-attachments/assets/6bbe9a75-1476-48f6-aae6-80584fae2ad8)

Los demás datos provienen de esta contraseña.

![image](https://github.com/user-attachments/assets/af87c85d-a1bc-415c-83f2-3a33f10de606)

Luego, damos check o seleccionamos Trust server certificate y por ultimo crear

![image](https://github.com/user-attachments/assets/215e0788-dccf-47d2-8b6b-dd846572ae83)

![image](https://github.com/user-attachments/assets/dcabccdf-2747-4441-ae8b-214b8da8a3a7)

![image](https://github.com/user-attachments/assets/e78be1d8-b4dd-4bac-afde-61d136f89a17)

Luego, le damos click a next ubicado en la esquina inferior derecha.

![image](https://github.com/user-attachments/assets/d0257856-56e8-4968-a785-5a54e7f83b81)

Llenamos los datos requeridos de la siguiente manera.

![image](https://github.com/user-attachments/assets/30a97bcf-47f9-4ac7-9c87-3f10fd8d8fb6)

En la ventana emergente escribimos la base: tsdb y luego, damos click en más + y desplegamos raw y seleccionamos nuestras tablas.

![image](https://github.com/user-attachments/assets/8c84f8de-5c30-468c-a6dd-eab6822d1fdd)

Ahora, configuramos los ajustes o settings.

Seleccionamos una de las tablas, ejemplo customer.

- En cursor column seleccionamos Updated_timestamp

- primary key: customer_id

Y asi, de la misma forma para todas las tablas.


![image](https://github.com/user-attachments/assets/28224862-fe59-4289-83f3-3893857bacd3)

Después de hacer lo mismo con todas las tablas de raw. Damos click a next.


![image](https://github.com/user-attachments/assets/1b8f6c2c-7544-4460-b99d-16ed1e1eb2e1)

Luego, haz click en siguiente y luego en guardar y ejecutar pipeline.

![image](https://github.com/user-attachments/assets/94516e46-4035-4dc7-910f-1409c719603a)

Ahora, para verificar que todo está bien, haremos la siguiente consulta.

Código:

SELECT COUNT(*) FROM walmart.bronze.order_items

![image](https://github.com/user-attachments/assets/fb9a29ab-9c26-4164-8aac-91fa810059f6)

Ahora, vamos a trabajar con dbt y necesitaremos configurarlo.

Crearemos una nueva carpeta llamada DBT_Project y lo abriremos en VSC 

![image](https://github.com/user-attachments/assets/efa7b068-5faf-41ce-88c8-b4df80a70077)

Primero comprobamos que tengamos instalado git. Así es que, en la terminal escribimos esto.

Código:

        Git –-version

![image](https://github.com/user-attachments/assets/8a62dd09-6a90-469f-ba55-24db9e5c1fb2)

También debes tener instalado python para dbt. Aquí muestro un cuadro de compatibilidad de versiones.

![image](https://github.com/user-attachments/assets/057a1c02-6745-4e9f-8c6a-6212414b446b)

Luego, instalamos UV para python.

Código:

       Python -m pip install uv



![image](https://github.com/user-attachments/assets/6a18b1f4-e042-4bae-b2b7-268f7a136e40)

Ahora, iniciamos uv.

Código:

       uv init

y se creara automáticamente los siguientes archivos.


![image](https://github.com/user-attachments/assets/bf0aa975-4852-4e74-b76d-5aab8a069e03)

Ahora, sincronizamos uv.

Código:

        uv sync

![image](https://github.com/user-attachments/assets/40dbe6c9-af13-4d2d-90e1-b17e52d3d5e9)

Luego, activamos el entorno virtual.

Código:

        .venv/Scripts/activate


![image](https://github.com/user-attachments/assets/dc4c182e-f52d-4058-b9a3-036426da240e)

Ahora, descargaremos dbt.

Código: 

        uv add dbt-core

![image](https://github.com/user-attachments/assets/d9d9ccb1-6530-4b15-86c4-27282ad04767)

Ahora, lo conectaremos con una fuente en este caso Databricks

Código:

        uv add dbt-databricks


![image](https://github.com/user-attachments/assets/a1745285-e2dc-414a-a698-87b8e157193a)

Iniciares ahora el dbt.

Código:

        dbt init

luego, te hará las siguientes preguntas y completarlas.


![image](https://github.com/user-attachments/assets/ac800e5c-ddbe-4e98-8cba-48e53355d719)

Ahora, para contestar las siguientes preguntas, debes ir a Databricks e ir a compute, luego, seleccionar serverless starter warehouse y luego seleccionamos connection details.

![image](https://github.com/user-attachments/assets/83de5d90-bc5a-40e8-83b0-58cc41b300fd)

![image](https://github.com/user-attachments/assets/44654581-ecb3-4059-a0b2-8e0a68d23a48)

Donde copiaras y pegaras los datos que te solicitan.

Ahora crearemos un token, para ello, nos dirigimos a la esquina superior derecha y seleccionamos settings

![image](https://github.com/user-attachments/assets/68870ee6-9f98-46c0-aa55-4f0554d79648)

Luego a deployment

![image](https://github.com/user-attachments/assets/1fe6d701-83cf-4de0-b094-5c423237619d)

Luego, a manage

![image](https://github.com/user-attachments/assets/2067ea72-3d12-4d45-91c4-429eb3cb3be0)

De ahí, generar un nuevo token

![image](https://github.com/user-attachments/assets/07dbbef1-9eb6-44c3-a99c-835c16946678)

![image](https://github.com/user-attachments/assets/c54da9fc-4eb6-4007-9125-cd9f5d1ff9d0)

Y finalmente, damos click en generar

![image](https://github.com/user-attachments/assets/865a0f93-79fe-45a5-a1e1-801956ecb3fd)

![image](https://github.com/user-attachments/assets/df333613-36a8-44be-969d-9562dc264777)


![image](https://github.com/user-attachments/assets/251cd279-535f-4294-9ac6-99934308ecad)

Ahora, en el archivo de dbt_project.yml el código se encuentra con líneas rojas, para vamos establecer las configuraciones de dbt.

1. Vamos a la parte inferior de VSC y ubicamos “dbt core is not installed” y, hacemos click ahí, luego seleccionamos Troubleshooting Setup the extensión.

![image](https://github.com/user-attachments/assets/85dd1d62-53e3-4b52-806b-a11a76132037)

![image](https://github.com/user-attachments/assets/965e90b5-02ac-4e87-859e-5fedbf538d4b)

Y veremos esto.

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()
