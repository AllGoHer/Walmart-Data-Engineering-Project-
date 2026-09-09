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

![image](https://github.com/user-attachments/assets/4b4fee63-669f-4920-8c99-d8c65fa357e0)

2.	Hacemos click seleccionar interprete de python.


![image](https://github.com/user-attachments/assets/097eb697-24b6-4714-822d-83d662031c31)

3.damos click en validar

![image](https://github.com/user-attachments/assets/9a0b4a30-fa3c-4363-9a7d-8d98474c2753)

4.	Luego en validar


![image](https://github.com/user-attachments/assets/33b65171-306c-40a1-ae0a-4a77c9f3582e)

![image](https://github.com/user-attachments/assets/69129647-4521-4fd7-ad11-f296808614bc)

Y listo, solo cerramos la pestaña Get started with dbt power user.

![image](https://github.com/user-attachments/assets/638af083-6521-4eb2-97cb-7c24d4d6c3a5)

Y como ven ahora, se valido todo el código, ósea ya aparece sin subrayar.


Ahora, creamos una carpeta llamada source y dentro de ella un archivo test.sql


![image](https://github.com/user-attachments/assets/4b43dfb6-9e82-4b67-a1d3-0a4ff88b4cc7)

Código:

        SELECT * FROM walmart.bronze.customers


![image](https://github.com/user-attachments/assets/709a58c3-1698-43f4-a185-138659aa8004)

![image](https://github.com/user-attachments/assets/7dbecdb8-19fc-4c9d-902f-c3d178f954f9)

Ahora, en la carpeta models\source creamos un archivo llamado source.yml

Código:

       sources:
         - name: walmart_databricks
           database: walmart
           schema: bronze
           tables:

               - name: orders

               - name: customers

               - name: products

               - name: order_items

               - name: stores

               - name: employees

![image](https://github.com/user-attachments/assets/cc339ae1-b250-4934-9d12-a0bbd3413c39)

Volvemos a test.sql

Código:

        SELECT * FROM {{ source('walmart_databricks', 'orders') }};

![image](https://github.com/user-attachments/assets/56de9282-ba32-4da2-b587-d8078529167c)

_______________________________________________________________________________________________________________________________________________________________________________________________________________

### SILVER LAYER

Ahora, en la carpeta models crearemos una carpeta llamada silver_t y dentro de ella un archivo llamado orders_t.sql.

Y dentro de la carpeta Walmart_project\analyses creamos el archivo scratch.sql


Código:

        SELECT 
            *
        FROM

            {{ source('walmart_databricks', 'orders') }}


Para materializar de forma incremental medianye jinja haremos los siguiente.

Código:

        {{ 
            config(
            materialized='incremental'
            ) 
        }}

        SELECT 
            *
        FROM

            {{ source('walmart_databricks', 'orders') }}


![image](https://github.com/user-attachments/assets/16303901-804f-41dd-8c5b-b64fb298d651)

Ahora si queremos materializar como una mesa, vamos al archivodbt_project.yml y cambiaremos el objeto y el tipo de materialización.


Inicial.

![image](https://github.com/user-attachments/assets/7d128348-1565-426d-9e5c-55366e374123)

Cambio:

![image](https://github.com/user-attachments/assets/90ceaabd-996c-428c-b354-28de7437f8e9)

Luego, en la carpeta silver_t creamos un archivo properties.yml

![image](https://github.com/user-attachments/assets/1bd7d0f1-e14d-4c2d-a3ec-54652dd4591e)

Ahora, al código anterior agregaremos una clave única para evitar en las inserciones las ordenes de pedidos con el mismo id.

Código:

        {{ 
            config(
                materialized='incremental'
                unique_key='order_id'
            ) 
        }}

        SELECT 
            *
        FROM

            {{ source('walmart_databricks', 'orders') }}


![image](https://github.com/user-attachments/assets/e32c70e2-dce1-40df-a6e1-3d831dbf8933)

No queremos pedidos que estén inactivos y los filtraremos.

Código:

       SELECT 
           *,
           current_timestamp() as processed_at
       FROM

           {{ source('walmart_databricks', 'orders') }}

       where
          is_active = 'Y'


![image](https://github.com/user-attachments/assets/6d7ee841-33d1-4a14-80cd-f719a68ce8da)

Ahora, veremos de forma incremental usando jinja, asi es que, volveremos al código anterior y agregaremos mas código al final.

Código:

        {{ 
            config(
                materialized='incremental',
                unique_key='order_id'
            ) 
        }}

        SELECT 
            *,
            current_timestamp() as processed_at
        FROM

            {{ source('walmart_databricks', 'orders') }}

        where
            is_active = 'Y'

        {% if is_incremental() %}

            AND processed_at > (SELECT MAX(processed_at) FROM {{ this }})

        {% endif %}



![image](https://github.com/user-attachments/assets/3cf0c92f-4215-49cc-b709-b543dcb2bd77)

Haremos otra consulta, pero dentro del proyecto, para ello prepararemos el código y luego más adelante lo ejecutaremos.

Código:

        {{ 
            config(
                materialized='incremental',
                unique_key='order_id'
            ) 
        }}

        SELECT 
             *,
            current_timestamp() as processed_at
        FROM

            {{ source('walmart_databricks', 'orders') }}

        where
            is_active = 'Y'

         {% if is_incremental() %}

            AND processed_at > (SELECT COALESE(MAX(updated_timestamp), '1900-01-01') FROM {{ this }})
   
         {% endif %}



Ahora, entraremos al proyecto para ejecutar las siguientes consultas.

Código:

        cd Walmart_project

Codigo:

        dbt debug



![image](https://github.com/user-attachments/assets/beafb7bc-9973-43bd-8880-6bea8a949faa)

![image](https://github.com/user-attachments/assets/e9c81f57-2891-4f5c-bfdc-f5dba1c017d0)

Codigo:

        dbt run

![image](https://github.com/user-attachments/assets/89d7136b-3d57-4142-b1b1-9eeb19bc5052)

![image](https://github.com/user-attachments/assets/19465e85-36ed-4eb3-981b-4689df6112dd)

Ahora verificamos en Databricks que se haya creado.

![image](https://github.com/user-attachments/assets/fa8eceb4-b90c-4ae1-8ae3-7b3fcc0bc991)

Abriremos un cuaderno para verificar si todo esta bien.

Código:

        SELECT COUNT(*) FROM walmart.dbt_schema.orders_t


![image](https://github.com/user-attachments/assets/c28981b5-749f-4763-83e4-89a3c622b6bc)

El código de orders_t.sql deberá quedar asi, para que no tenga errores en la ejecución.

Código:

        {{ 
             config(
                materialized='incremental',
                unique_key='order_id'
            ) 
        }}

         SELECT 
            *,
            current_timestamp() as processed_at
         FROM

            {{ source('walmart_databricks', 'orders') }}

        where
            is_active = 'Y'

        {% if is_incremental() %}

            AND updated_timestamp > (SELECT COALESE(MAX(updated_timestamp), '1900-01-01') FROM {{ this }})
   
        {% endif %}

![image](https://github.com/user-attachments/assets/d815e93d-515a-4dca-950e-17c0c5506be7)

Ahora ejecutamos dbt run.

![image](https://github.com/user-attachments/assets/18e17e23-50d8-40b5-b31e-f4542e1e5d46)

Luego en macros creamos un archivo llamado custom_schema.yml

![image](https://github.com/user-attachments/assets/4865f890-0fa6-4761-a40b-6fe1680a1889)

Código:

        {% macro generate_schema_name(custom_schema_name, node) -%}

            {%- set default_schema = target.schema -%}
            {%- if custom_schema_name is none -%}

                {{ default_schema }}

            {%- else -%}

                {{ default_schema }}_{{ custom_schema_name | trim }}

            {%- endif -%}

        {%- endmacro %}


En este código debemos quitar el esquema predeterminado, el cual quedará así.

Código:

        {% macro generate_schema_name(custom_schema_name, node) -%}

            {%- set default_schema = target.schema -%}
            {%- if custom_schema_name is none -%}

                {{ default_schema }}

            {%- else -%}

                {{ custom_schema_name | trim }}

            {%- endif -%}

        {%- endmacro %}

![image](https://github.com/user-attachments/assets/cf0b23a8-5873-4b1a-88fe-44aeeaaf3fd5)

Ahora, nos vamos a dbt_project y al final del código y agregamos lo siguiente.

Código:

        +schema: silver_t

![image](https://github.com/user-attachments/assets/0dc85066-14bd-4278-8381-b3a0ce780f32)

Luego, vamos a la terminal y ejecutamos.

Codigo:

        dbt run


![image](https://github.com/user-attachments/assets/f2b95659-edee-4c69-b09d-6ef82aa32fd3)

Para confirmar vamos a Databricks catálogo.


![image](https://github.com/user-attachments/assets/ddb60e51-8f22-487d-a872-d17c27dea6cb)

Nos vamos ahora a al VSC a la carpeta model y creamos un archivo llamado products_t.sql con el siguiente codigo.

Codigo:
 
        {{ 
            config(
                materialized='incremental',
                unique_key='product_id'
            ) 
        }}

        SELECT 
            *,
            current_timestamp() as processed_at
        FROM

            {{ source('walmart_databricks', 'products') }}

         where
             is_active = 'Y'

         {% if is_incremental() %}

            AND updated_timestamp > (SELECT COALESCE(MAX(updated_timestamp), '1900-01-01') FROM {{ this }})
   
        {% endif %}

![image](https://github.com/user-attachments/assets/d80f6a99-7b2e-4044-ac75-96cb6319f5d5)

Y ejecutamos la consulta.

![image](https://github.com/user-attachments/assets/bd2e1929-a85c-4c55-adb7-6622cf231a2d)


![image](https://github.com/user-attachments/assets/68879efa-dd57-447a-bff7-14d9dc606d47)

Ahora hay que asegurarse que ninguno de los precios sean negativos.

Entonces creamos un archivo properties.yml en la carpeta models/silvert_t 

Y pasamos le siguiente código.

Código:

        models:
          - name: products_t
            columns:
                - name: product_id
                  data_tests:
                    - not_null
                    - unique
                - name: price
                  data_tests:
                    - greater_than: 0

          - name: orders_t
            columns:
                - name: order_id
                  data_tests:
                    - not_null
                    - unique

![image](https://github.com/user-attachments/assets/ae725af5-6af4-4563-a44d-ec781f0d11d7)

Luego vemos el dbt_project subrayado en rojo, no hay preocuparse solo hay que seguir la ejecución.

Hacemos click en jinja, luego seleccionamos CONFIGURE FILE ASOCIATION. Y ahora seleccionamos jinja YML Current Asociation

También puedes ignorarlo.

![image](https://github.com/user-attachments/assets/84629262-a3ca-4769-82df-02babc455095)


![image](https://github.com/user-attachments/assets/9fd4ef0b-e781-4879-b1d0-a5d0ea8ea44d)

Luego ejecutamos.

Código:

        dbt run

![image](https://github.com/user-attachments/assets/2c2ca84b-b120-430c-906c-f2e35d9e6177)

Ahora, si vamos a Databricks podremos ver que han sido creados.

![image](https://github.com/user-attachments/assets/73fd5a69-fa6f-4a78-b4ec-4fcb2ec8d727)

Ahora, ejecutamos el test.

Código:

        dbt test

![image](https://github.com/user-attachments/assets/dc44123b-cbbc-49af-9e5b-30d5108f49fe)

Toca ahora crear el mismo proceso para los empleados.

Entonces, creamos un archivo llamado employees_t.sql

Código:

        {{ 
            config(
                materialized='incremental',
                unique_key='employee_id'
            ) 
        }}

        SELECT 
            *,
            current_timestamp() as processed_at
        FROM

            {{ source('walmart_databricks', 'employees') }}

        where
            is_active = 'Y'

        {% if is_incremental() %}

            AND updated_timestamp > (SELECT COALESCE(MAX(updated_timestamp), '1900-01-01') FROM {{ this }})
   
        {% endif %}


![image](https://github.com/user-attachments/assets/cf816aef-1108-4b34-a359-a7e3fab25212)

Antes de todo, primero ejecutamos la consulta 


![image](https://github.com/user-attachments/assets/8294aa7d-a7fd-4b8c-adc4-766b21fe7d39)

Crearemos ahora el archivo stores_t.sql

Código:

        {{ 
            config(
                materialized='incremental',
                unique_key='store_id'
            ) 
        }}

        SELECT 
            *,
            current_timestamp() as processed_at
        FROM

            {{ source('walmart_databricks', 'stores') }}

        where
            is_active = 'Y'

        {% if is_incremental() %}

            AND updated_timestamp > (SELECT COALESCE(MAX(updated_timestamp), '1900-01-01') FROM {{ this }})
   
        {% endif %}



![image](https://github.com/user-attachments/assets/2acca224-7849-4d20-91fb-43c942e14283)

Ahora, toca crear el de clientes (customers_t.sql)

Código:

        {{ 
            config(
                materialized='incremental',
                unique_key='customer_id'
            ) 
        }}

        SELECT 
            *,
            current_timestamp() as processed_at
        FROM

            {{ source('walmart_databricks', 'customers') }}

        where
            is_active = 'Y'

        {% if is_incremental() %}

            AND updated_timestamp > (SELECT COALESCE(MAX(updated_timestamp), '1900-01-01') FROM {{ this }})
   
        {% endif %}


Ahora, ejecutamos la consulta.


![image](https://github.com/user-attachments/assets/36b20205-63b5-4ac4-8ac3-80e850ef3b31)

Luego, creamos el archivo order_items_t.sql

Código:

        {{ 
            config(
                materialized='incremental',
                unique_key='order_item_id'
            ) 
        }}

        SELECT 
            *,
            current_timestamp() as processed_at
        FROM

            {{ source('walmart_databricks', 'order_items') }}

        where
            is_active = 'Y'

        {% if is_incremental() %}

            AND updated_timestamp > (SELECT COALESCE(MAX(updated_timestamp), '1900-01-01') FROM {{ this }})
   
        {% endif %}


![image](https://github.com/user-attachments/assets/99500c85-0ec8-4d7d-91ef-70af528622ed)

Por último, haremos la prueba.

Código:

        dbt test

![image](https://github.com/user-attachments/assets/dc44eec0-df8a-4704-96f2-e3b6dab08012)

Código:

        dbt run

![image](https://github.com/user-attachments/assets/a6c4b9aa-a40a-47b0-8090-f0f615f61fb4)

Luego, vamos a Databricks para verificar la creación.

![image](https://github.com/user-attachments/assets/badb4f47-46d3-4e45-9c4a-0c7eae247da6)

Ahora crearemos una nueva carpeta llamada obt_b y dentro de ella un archivo llamado obt_b.sql

![image](https://github.com/user-attachments/assets/49366495-d3fa-4dc6-b858-fc5493fa1a22)

Luego, en los archivos sql que creamos anteriormente borraremos esta sección de código.

![image](https://github.com/user-attachments/assets/49137924-115b-42a2-b342-c829b7e29a3c)

Código:

        where
            is_active = 'Y'


tendría que quedar asi.

ejemplo:


![image](https://github.com/user-attachments/assets/1e4b7182-72f4-4399-bde0-a35f5d5c4330)

Ahora refrescaremos todo a través de la terminal.

Código:

        dbt run --full-refresh


![image](https://github.com/user-attachments/assets/31f0afbb-3e9d-4725-8632-7a189980cb5a)

Luego, creamos en obt_b un rachivo llamado refer.sql con el siguiente código.

Código:

        SELECT
            -- customers_t columns
             c.customer_id,
             c.first_name AS customer_first_name,
             c.last_name AS customer_last_name,
             c.email AS customer_email,
             c.phone AS customer_phone,
             c.city AS customer_city,
             c.province AS customer_province,
             c.country AS customer_country,
             c.created_timestamp AS customer_created_timestamp,
             c.updated_timestamp AS customer_updated_timestamp,
             c.is_active AS customer_is_active,
             c.processed_at AS customer_processed_at,
    
            -- orders_t columns (excluding customer_id which is already included)
   
            o.order_id,
            o.store_id,
            o.order_timestamp,
            o.payment_method,
            o.order_status,
            o.total_amount,
            o.created_timestamp AS order_created_timestamp,
            o.updated_timestamp AS order_updated_timestamp,
            o.processed_at AS order_processed_at,
    
            -- order_items_t columns ()
    
            oi.order_item_id,
            oi.quantity,
            oi.unit_price,
            oi.line_amount,
            oi.created_timestamp AS order_item_created_timestamp,
            oi.updated_timestamp AS order_item_updated_timestamp,
            oi.is_active AS order_item_is_active,
            oi.processed_at AS order_item_processed_at,

            -- products_t columns
            p.product_id,
            p.product_name,
            p.description,
            p.category,
            p.brand,
            p.price,
            p.created_timestamp AS product_created_timestamp,
            p.updated_timestamp AS product_updated_timestamp,   
            p.is_active AS product_is_active,
            p.processed_at AS product_processed_at,
    
            -- stores_t columns (excluding store_id which is already from orders 
    
            s.store_name,
            s.city AS store_city,
            s.province AS store_province,
            s.country AS store_country,
            s.created_timestamp AS store_created_timestamp,
            s.updated_timestamp AS store_updated_timestamp,
            s.is_active AS store_is_active,
            s.processed_at AS store_processed_at,
    
            -- employees_t columns
            e.employee_id,
            e.first_name AS employee_first_name,
            e.last_name AS employee_last_name,
            e.email AS employee_email,
            e.job_title,
            e.salary,
            e.created_timestamp AS employee_created_timestamp,
            e.updated_timestamp AS employee_updated_timestamp,
            e.is_active AS employee_is_active,
            e.processed_at AS employee_processed_at

        FROM walmart.silver_t.orders_t o
        LEFT JOIN walmart.silver_t.customers_t c
            ON o.customer_id = c.customer_id
        LEFT JOIN walmart.silver_t.order_items_t oi
            ON o.order_id = oi.order_id
        LEFT JOIN walmart.silver_t.products_t p
            ON oi.product_id = p.product_id
        LEFT JOIN walmart.silver_t.stores_t s
            ON o.store_id = s.store_id
        LEFT JOIN walmart.silver_t.employees_t e
            ON o.employee_id = e.employee_id


Lo que haremos ahora es escribir el código para el archivo obt_b.sql

Código:

        {% set tables = [
            {
                "table": "walmart.silver_t.orders_t",
                "columns": "o.order_id, o.store_id, o.order_timestamp, o.payment_method, o.order_status, o.total_amount, o.created_timestamp AS order_created_timestamp, o.updated_timestamp AS                order_updated_timestamp, o.is_active AS order_is_active, o.processed_at AS order_processed_at, current_timestamp() AS obt_b_processed_at",

                "alias": "o"
            },
            {
                "table": "walmart.silver_t.order_items_t",
                "columns": "oi.order_item_id, oi.quantity, oi.unit_price, oi.line_amount, oi.created_timestamp AS order_item_created_timestamp, oi.updated_timestamp AS order_item_updated_timestamp,    oi.is_active AS order_item_is_active, oi.processed_at AS order_item_processed_at",
                "alias": "oi",
                "join_condition": "o.order_id = oi.order_id"
            },
            {
                "table": "walmart.silver_t.products_t",
                "columns": "p.product_id, p.product_name, p.category, p.brand, p.price, p.created_timestamp AS product_created_timestamp, p.updated_timestamp AS product_updated_timestamp, p.is_active AS   product_is_active, p.processed_at AS product_processed_at",
                "alias": "p",
                "join_condition": "oi.product_id = p.product_id"
            },
            {
                "table": "walmart.silver_t.stores_t",
                "columns": "s.store_name, s.city AS store_city, s.province AS store_province, s.country AS store_country, s.created_timestamp AS store_created_timestamp, s.updated_timestamp AS store_updated_timestamp, s.is_active AS store_is_active, s.processed_at AS store_processed_at",
                "alias": "s",
                "join_condition": "o.store_id = s.store_id"
            },
            {
                "table": "walmart.silver_t.employees_t",
                "columns": "e.employee_id, e.first_name AS employee_first_name, e.last_name AS employee_last_name, e.email AS employee_email, e.job_title, e.salary, e.created_timestamp AS employee_created_timestamp, e.updated_timestamp AS employee_updated_timestamp, e.is_active AS employee_is_active, e.processed_at AS employee_processed_at",
                "alias": "e",
                "join_condition": "o.store_id = e.store_id"
            },
            {
                "table": "walmart.silver_t.customers_t",
                "columns": "c.customer_id, c.first_name AS customer_first_name, c.last_name AS customer_last_name, c.email AS customer_email, c.phone AS customer_phone, c.city AS customer_city, c.province AS customer_province, c.country AS customer_country, c.created_timestamp AS customer_created_timestamp, c.updated_timestamp AS customer_updated_timestamp, c.is_active AS customer_is_active, c.processed_at AS customer_processed_at",
                "alias": "c",
                "join_condition": "o.customer_id = c.customer_id"
            }
        ] %}

        SELECT
        {% for t in tables %}
            {{ t["columns"] }}{% if not loop.last %},{% endif %}
        {% endfor %}

        FROM
        {% for t in tables %}
            {% if loop.first %}
                {{ t["table"] }} AS {{ t["alias"] }}
            {% else %}
                LEFT JOIN {{ t["table"] }} AS {{ t["alias"] }}
                ON {{ t["join_condition"] }}
            {% endif %}
        {% endfor %}


Luego ejecutamos la consulta.

![image](https://github.com/user-attachments/assets/3af62218-833b-41b2-93f1-13597c975788)

Ahora, crearemos un caso de prueba personalizado.

Vamos a crear una prueba que no devuelva nada, asi es que, crearemos en test, un archivo llamado test_obt.sql 

Código:

        {{ config(severity='warn')}}

        SELECT 1
        FROM
            {{ ref('obt_b') }} AS obt
        WHERE
            obt.order_id IS NULL
            OR obt.store_id IS NULL
            OR obt.product_id IS NULL
            OR obt.customer_id IS NULL
            OR obt.employee_id IS NULL
            OR obt.order_item_id IS NULL

Ahora, vamos a modificar el código de los archivoS de plata para que no nos de error, donde cambiarenos el termino AND del código de cada archivo por WHERE.

EJEMPLO:

Cambiar AND

![image](https://github.com/user-attachments/assets/f12953bc-3be2-42ea-98e3-b10080bbfcc4)

Por WHERE

![image](https://github.com/user-attachments/assets/c91e55ed-8f73-47c0-8a89-7e3006cc150d)

Ahora, nos vamos al archivo dbt_project y agregamos el código para el archivo silver_b

Código:

        silver_b:
              +materialized: table
              +schema: silver_b


![image](https://github.com/user-attachments/assets/f14f5d1d-17e5-4c7b-bdbd-b1caf80f30ec)

NOTA: Podemos eliminar el archivo refer.sql, puesto que ya no lo utilizares en el proyecto.


Luego, iremos a terminal y ejecutaremos el siguiente código.

Código:

        dbt run --full-refresh 


![image](https://github.com/user-attachments/assets/adc25830-cf44-4e8f-8db3-388c3b3f87e0)

Verificamos en Databricks que se haya creado la carpeta silver_b/obt_b

![image](https://github.com/user-attachments/assets/0a2d3065-7881-435f-ae34-3aa0455f3e81)

Ahora aplicaremos la prueba.

Codigo:

        dbt test

![image](https://github.com/user-attachments/assets/78c884fc-d583-40bf-a72c-fb1533918b2e)

Ahora nos vamos a Databricks a verificar. 
 creamos un notebook y hacemos la siguiente consulta.

Código:

        SELECT * FROM walmart.silver_b.obt_b


![image](https://github.com/user-attachments/assets/e3cac65a-92e3-4cd8-a8e7-a79637e70875)

_______________________________________________________________________________________________________________________________________________________________________________________________________________

### GOLD LAYER

Luego, nos vamos al archivo dbt_project.yml y agregamos al proyecto la capa gold.

Código:

       gold:
         +materialized: table
         +schema: gold 
      


![image](https://github.com/user-attachments/assets/8398e614-6737-442a-b3b0-83876cf8b6d3)

Crearemos ahora la carepta gold y dentro de ella los siguientes archivos.

- eph_customer.sql

Código:

        {{ config(materialized='view') }}

        SELECT
            DISTINCT
            customer_id,
            customer_first_name,
            customer_last_name,
            customer_email,
            customer_phone,
            customer_city,
            customer_province,
            customer_country,
            customer_created_timestamp,
            customer_updated_timestamp,
            customer_is_active,
            customer_processed_at,
            CURRENT_TIMESTAMP() AS customers_gold_processed_at
        FROM
            {{ ref('obt_b') }}


Ahora, regresamos al archivo eph_customers.sql y escribiremos el codigo.

Código:

        SELECT
            DISTINCT
            customer_id,
            customer_first_name,
            customer_last_name,
            customer_email,
            customer_phone,
            customer_city,
            customer_province,
            customer_country,
            customer_created_timestamp,
            customer_updated_timestamp,
            customer_is_active,
            customer_processed_at,
            CURRENT_TIMESTAMP() AS customers_gold_processed_at
        FROM
            {{ ref('obt_b') }}


- eph_employees.sql

Código:

        {{ config(materialized='view') }}

        SELECT
            DISTINCT 
            employee_id,
            employee_first_name,
            employee_last_name,
            employee_email,
            salary,
            job_title,
            store_id,
            employee_created_timestamp,
            employee_updated_timestamp,
            employee_is_active,
            employee_processed_at,
            CURRENT_TIMESTAMP() AS employee_gold_processed_at
        FROM
            {{ ref('obt_b') }}


- eph_orders.sql
 
Código:

        {{ config(materialized='view') }}

        SELECT
            DISTINCT 
            order_id,
            order_item_id,
            payment_method,
            order_status,
            order_timestamp,
            order_created_timestamp,
            order_updated_timestamp,
            order_is_active,
            order_processed_at,
            CURRENT_TIMESTAMP() AS order_gold_processed_at
        FROM
            {{ ref('obt_b') }}



- eph_products.sql

Código:

        {{ config(materialized='view') }}

        SELECT
            DISTINCT 
            product_id,
            product_name,
            category,
            brand,
            price,
            product_created_timestamp,
            product_updated_timestamp,
            product_is_active,
            product_processed_at,
            CURRENT_TIMESTAMP() AS products_gold_processed_at
        FROM
            {{ ref('obt_b') }}



- eph_stores.sql

Código:

        {{ config(materialized='view') }}

        SELECT
            DISTINCT 
            store_id,
            store_name,
            store_city,
            store_province,
            store_country,
            store_created_timestamp,
            store_updated_timestamp,
            store_is_active,
            store_processed_at,
            CURRENT_TIMESTAMP() AS stores_gold_processed_at
        FROM
            {{ ref('obt_b') }}


Antes de correr los modelos de gold, haremos una limpieza de caché

Código:

        dbt clean

![image](https://github.com/user-attachments/assets/55c973ef-94da-4612-849d-91a4f5fc54d8)

Luego, verificamos que los modelos sean reconocidos.

Código:

        dbt ls --resource-type model | Select-String "eph"

![image](https://github.com/user-attachments/assets/3940bba4-c46a-48ed-95ad-963d12a8344a)

Ejecuta los modelos (crea las vistas)

Código:

         dbt run --select "eph_*"


![image](https://github.com/user-attachments/assets/b8880921-8018-4485-9911-12fb59f4b6d2)

Luego, verificamos que haya ejecutado correctamente en Databricks.

![image](https://github.com/user-attachments/assets/5d66d465-65b0-462f-9b04-8d73d007dd63)

Ahora, en snapshots creamos los siguientes archivos. 

- dim_customers.yml

Código:

        snapshots:
            - name: dim_customers
              relation: ref('eph_customers')
              config:
                schema: gold
                database: walmart    
                unique_key: customer_id
                strategy: timestamp
                updated_at: customer_updated_timestamp
                dbt_valid_to_current: "to_date('9999-12-31')"


- dim_products.yml

Código:

        snapshots:
          - name: dim_products
            relation: ref('eph_products')
            config:
                schema: gold
                database: walmart    
                unique_key: product_id
                strategy: timestamp
                updated_at: product_updated_timestamp
                dbt_valid_to_current: "to_date('9999-12-31')"



- dim_store.yml

Código:

        snapshots:
          - name: dim_stores
            relation: ref('eph_stores')
            config:
            schema: gold
                database: walmart    
                unique_key: store_id
                strategy: timestamp
                updated_at: store_updated_timestamp
                dbt_valid_to_current: "to_date('9999-12-31')"


-dim_employees.yml

Código:

        snapshots:
          - name: dim_employees
            relation: ref('eph_employees')
            config:
                schema: gold
                database: walmart    
                unique_key: employee_id
                strategy: timestamp
                updated_at: employee_updated_timestamp
                dbt_valid_to_current: "to_date('9999-12-31')"


-dim_orders.yml

Código:

        snapshots:
          - name: dim_orders
            relation: ref('eph_orders')
            config:
                schema: gold
                database: walmart    
                unique_key: order_id
                strategy: timestamp
                updated_at: order_updated_timestamp
                dbt_valid_to_current: "to_date('9999-12-31')"






Ahora, nos vamos a la terminal y ejecutamos los siguiente.

Código:

        dbt snapshot  

![image](https://github.com/user-attachments/assets/51c96592-551f-4e5f-a65c-f68b48f4e623)

Luego verificamos que todo este bien y, hacemos una consulta en Databricks.

Código:

        SELECT * FROM walmart.gold.dim_customers

![image](https://github.com/user-attachments/assets/ee8d36f8-7197-413e-8e1c-e9d253e6a164)

Ahora, creamos la carpeta de hechos (fact) en la carpeta gold

Código:

        SELECT
            order_id,
            order_item_id,
            product_id,
            store_id,
            employee_id,
            customer_id,
            total_amount,
            quantity,
            unit_price,
           line_amount
        FROM
            {{ ref('obt_b') }} 

![image](https://github.com/user-attachments/assets/3de18630-da5c-4099-b86c-588c6cfcd9c6)

Luego, ejecutamos dbt.

Código:

        dbt run

![image](https://github.com/user-attachments/assets/224c9d73-67c3-45d4-8b87-c297382cf7fa)

Verificamos en Databricks.

Código:

        SELECT * FROM walmart.gold.fact_orders


![image](https://github.com/user-attachments/assets/3ee32761-619b-4a15-ab8a-8af84f8c8d73)

_______________________________________________________________________________________________________________________________________________________________________________________________________________

![image](https://github.com/user-attachments/assets/87cf2efc-6a99-4cfd-bd22-17336317c933)

Para esta etapa, trabajaremos con dos herramientas más, Airflow y docker, para lo cual, es necesario cumplir con dos requisitos.

1.	Tener instalado docker desktop y mantenerlo abierto.

2.	Descargar Airflow docker compose e instalarlo en Visual Studio Code (ver en el siguiente paso). 

Ahora, vamos a crear una carpeta llamada Airflow en la raíz del proyecto.

![image](https://github.com/user-attachments/assets/f213b097-1a48-47e0-ad21-67c767d53059)

Luego, dentro de el creamos el archivo docker-compose.yml

Código:

        # Licensed to the Apache Software Foundation (ASF) under one
        # or more contributor license agreements.  See the NOTICE file
        # distributed with this work for additional information
        # regarding copyright ownership.  The ASF licenses this file
        # to you under the Apache License, Version 2.0 (the
        # "License"); you may not use this file except in compliance
        # with the License.  You may obtain a copy of the License at
        #
        #   http://www.apache.org/licenses/LICENSE-2.0
        #
        # Unless required by applicable law or agreed to in writing,
        # software distributed under the License is distributed on an
        # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
        # KIND, either express or implied.  See the License for the
        # specific language governing permissions and limitations
        # under the License.
        #

        # Basic Airflow cluster configuration for CeleryExecutor with Redis and PostgreSQL.
        #
        # WARNING: This configuration is for local development. Do not use it in a production deployment.
        #
        # This configuration supports basic configuration using environment variables or an .env file
        # The following variables are supported:
        #
        # AIRFLOW_IMAGE_NAME           - Docker image name used to run Airflow.
        #                                Default: apache/airflow:3.3.1
        # AIRFLOW_UID                  - User ID in Airflow containers
        #                                Default: 50000
        # AIRFLOW_PROJ_DIR             - Base path to which all the files will be volumed.
        #                                Default: .
        # Those configurations are useful mostly in case of standalone testing/running Airflow in test/try-out mode
        #
        # _AIRFLOW_WWW_USER_USERNAME   - Username for the administrator account (if requested).
        #                                Default: airflow
        # _AIRFLOW_WWW_USER_PASSWORD   - Password for the administrator account (if requested).
        #                                Default: airflow
        # _PIP_ADDITIONAL_REQUIREMENTS - Additional PIP requirements to add when starting all containers.
        #                                Use this option ONLY for quick checks. Installing requirements at container
        #                                startup is done EVERY TIME the service is started.
        #                                A better way is to build a custom image or extend the official image
        #                                as described in https://airflow.apache.org/docs/docker-stack/build.html.
        #                                Default: ''
        #
        # Feel free to modify this file to suit your needs.
         ---
        x-airflow-common:
        &airflow-common
        # In order to add custom dependencies or upgrade provider distributions you can use your extended image.
        # Comment the image line, place your Dockerfile in the directory where you placed the docker-compose.yaml
        # and uncomment the "build" line below, Then run `docker-compose build` to build the images.
        image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:3.3.1}
        # build: .
        env_file:
          - ${ENV_FILE_PATH:-.env}
        environment:
          &airflow-common-env
          AIRFLOW__CORE__EXECUTOR: CeleryExecutor
          AIRFLOW__CORE__AUTH_MANAGER: airflow.providers.fab.auth_manager.fab_auth_manager.FabAuthManager
          AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
          AIRFLOW__CELERY__RESULT_BACKEND: db+postgresql+psycopg2://airflow:airflow@postgres/airflow
          AIRFLOW__CELERY__BROKER_URL: redis://:@redis:6379/0
          AIRFLOW__CORE__FERNET_KEY: ${FERNET_KEY}
          AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION: 'true'
          AIRFLOW__CORE__LOAD_EXAMPLES: 'true'
          AIRFLOW__CORE__EXECUTION_API_SERVER_URL: 'http://airflow-apiserver:8080/execution/'
          AIRFLOW__API_AUTH__JWT_SECRET: ${AIRFLOW__API_AUTH__JWT_SECRET:-airflow_jwt_secret}
          AIRFLOW__API_AUTH__JWT_ISSUER: ${AIRFLOW__API_AUTH__JWT_ISSUER:-airflow}
         # yamllint disable rule:line-length
         # Use simple http server on scheduler for health checks
         # See https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/check-health.html#scheduler-health-check-server
         # yamllint enable rule:line-length
         AIRFLOW__SCHEDULER__ENABLE_HEALTH_CHECK: 'true'
         # WARNING: Use _PIP_ADDITIONAL_REQUIREMENTS option ONLY for a quick checks
         # for other purpose (development, test and especially production usage) build/extend Airflow image.
         _PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:-}
         # The following line can be used to set a custom config file, stored in the local config folder
         AIRFLOW_CONFIG: '/opt/airflow/config/airflow.cfg'
       volumes:
         - ${AIRFLOW_PROJ_DIR:-.}/dags:/opt/airflow/dags
         - ${AIRFLOW_PROJ_DIR:-.}/logs:/opt/airflow/logs
         - ${AIRFLOW_PROJ_DIR:-.}/config:/opt/airflow/config
         - ${AIRFLOW_PROJ_DIR:-.}/plugins:/opt/airflow/plugins
       user: "${AIRFLOW_UID:-50000}:0"
       depends_on:
         &airflow-common-depends-on
         redis:
           condition: service_healthy
         postgres:
           condition: service_healthy

      services:
        postgres:
         image: postgres:16
         environment:
           POSTGRES_USER: airflow
           POSTGRES_PASSWORD: airflow
           POSTGRES_DB: airflow
         volumes:
           - postgres-db-volume:/var/lib/postgresql/data
         healthcheck:
           test: ["CMD", "pg_isready", "-U", "airflow"]
           interval: 10s
           retries: 5
           start_period: 5s
         restart: always

       redis:
         # Redis is limited to 7.2-bookworm due to licencing change
         # https://redis.io/blog/redis-adopts-dual-source-available-licensing/
         image: redis:7.2-bookworm
         expose:
           - 6379
         healthcheck:
           test: ["CMD", "redis-cli", "ping"]
           interval: 10s
           timeout: 30s
           retries: 50
           start_period: 30s
           restart: always

       airflow-apiserver:
         <<: *airflow-common
         command: api-server
         ports:
           - "8080:8080"
         healthcheck:
           test: ["CMD", "curl", "--fail", "http://localhost:8080/api/v2/monitor/health"]
           interval: 30s
           timeout: 10s
           retries: 5
           start_period: 30s
         restart: always
         depends_on:
           <<: *airflow-common-depends-on
           airflow-init:
             condition: service_completed_successfully

       airflow-scheduler:
         <<: *airflow-common
         command: scheduler
         healthcheck:
           test: ["CMD-SHELL", 'airflow jobs check --job-type SchedulerJob --hostname "$${HOSTNAME}"']
           interval: 30s
           timeout: 10s
           retries: 5
           start_period: 30s
         restart: always
         depends_on:
           <<: *airflow-common-depends-on
           airflow-init:
             condition: service_completed_successfully

        airflow-dag-processor:
         <<: *airflow-common
         command: dag-processor
         healthcheck:
           test: ["CMD-SHELL", 'airflow jobs check --job-type DagProcessorJob --hostname "$${HOSTNAME}"']
           interval: 30s
           timeout: 10s
           retries: 5
           start_period: 30s
         restart: always
         depends_on:
           <<: *airflow-common-depends-on
           airflow-init:
             condition: service_completed_successfully

       airflow-worker:
         <<: *airflow-common
         command: celery worker
         healthcheck:
           # yamllint disable rule:line-length
           test: ["CMD-SHELL", 'celery --app airflow.providers.celery.executors.celery_executor.app inspect ping -d "celery@$${HOSTNAME}" || celery --app airflow.executors.celery_executor.app inspect ping -d "celery@$${HOSTNAME}"']
           interval: 30s
           timeout: 10s
           retries: 5
           start_period: 30s
         environment:
           <<: *airflow-common-env
           # Required to handle warm shutdown of the celery workers properly
           # See https://airflow.apache.org/docs/docker-stack/entrypoint.html#signal-propagation
          DUMB_INIT_SETSID: "0"
         restart: always
         depends_on:
           <<: *airflow-common-depends-on
           airflow-apiserver:
             condition: service_healthy
           airflow-init:
             condition: service_completed_successfully

       airflow-triggerer:
         <<: *airflow-common
         command: triggerer
         healthcheck:
           test: ["CMD-SHELL", 'airflow jobs check --job-type TriggererJob --hostname "$${HOSTNAME}"']
           interval: 30s
           timeout: 10s
           retries: 5
           start_period: 30s
         restart: always
         depends_on:
           <<: *airflow-common-depends-on
           airflow-init:
             condition: service_completed_successfully

       airflow-init:
         <<: *airflow-common
         entrypoint: /bin/bash
         # yamllint disable rule:line-length
          command:
           - -c
           - |
             if [[ -z "${AIRFLOW_UID}" ]]; then
               echo
               echo -e "\033[1;33mWARNING!!!: AIRFLOW_UID not set!\e[0m"
               echo "If you are on Linux, you SHOULD follow the instructions below to set "
               echo "AIRFLOW_UID environment variable, otherwise files will be owned by root."
               echo "For other operating systems you can get rid of the warning with manually created .env file:"
               echo "    See: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#setting-the-right-airflow-user"
               echo
               export AIRFLOW_UID=$$(id -u)
             fi
             one_meg=1048576
             mem_available=$$(($$(getconf _PHYS_PAGES) * $$(getconf PAGE_SIZE) / one_meg))
             cpus_available=$$(grep -cE 'cpu[0-9]+' /proc/stat)
             disk_available=$$(df / | tail -1 | awk '{print $$4}')
             warning_resources="false"
             if (( mem_available < 4000 )) ; then
               echo
               echo -e "\033[1;33mWARNING!!!: Not enough memory available for Docker.\e[0m"
               echo "At least 4GB of memory required. You have $$(numfmt --to iec $$((mem_available * one_meg)))"
               echo
               warning_resources="true"
             fi
             if (( cpus_available < 2 )); then
               echo
               echo -e "\033[1;33mWARNING!!!: Not enough CPUS available for Docker.\e[0m"
               echo "At least 2 CPUs recommended. You have $${cpus_available}"
               echo
               warning_resources="true"
             fi
             if (( disk_available < one_meg * 10 )); then
               echo
               echo -e "\033[1;33mWARNING!!!: Not enough Disk space available for Docker.\e[0m"
               echo "At least 10 GBs recommended. You have $$(numfmt --to iec $$((disk_available * 1024 )))"
               echo
               warning_resources="true"
             fi
             if [[ $${warning_resources} == "true" ]]; then
               echo
               echo -e "\033[1;33mWARNING!!!: You have not enough resources to run Airflow (see above)!\e[0m"
               echo "Please follow the instructions to increase amount of resources available:"
               echo "   https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#before-you-begin"
               echo
             fi
             echo
             echo "Creating missing opt dirs if missing:"
             echo
             mkdir -v -p /opt/airflow/{logs,dags,plugins,config}
             echo
             echo "Airflow version:"
             /entrypoint airflow version
             echo
             echo "Files in shared volumes:"
             echo
             ls -la /opt/airflow/{logs,dags,plugins,config}
             echo
             echo "Running airflow config list to create default config file if missing."
             echo
             /entrypoint airflow config list >/dev/null
             echo
             echo "Files in shared volumes:"
             echo
             ls -la /opt/airflow/{logs,dags,plugins,config}
             echo
             echo "Change ownership of files in /opt/airflow to ${AIRFLOW_UID:-50000}:0"
             echo
             chown -R "${AIRFLOW_UID:-50000}:0" /opt/airflow/
             echo
             echo "Change ownership of files in shared volumes to ${AIRFLOW_UID:-50000}:0"
             echo
             chown -v -R "${AIRFLOW_UID:-50000}:0" /opt/airflow/{logs,dags,plugins,config}
             echo
             echo "Files in shared volumes:"
             echo
             ls -la /opt/airflow/{logs,dags,plugins,config}

         # yamllint enable rule:line-length
         environment:
           <<: *airflow-common-env
           _AIRFLOW_DB_MIGRATE: 'true'
           _AIRFLOW_WWW_USER_CREATE: 'true'
           _AIRFLOW_WWW_USER_USERNAME: ${_AIRFLOW_WWW_USER_USERNAME:-airflow}
           _AIRFLOW_WWW_USER_PASSWORD: ${_AIRFLOW_WWW_USER_PASSWORD:-airflow}
           _PIP_ADDITIONAL_REQUIREMENTS: ''
         user: "0:0"

       airflow-cli:
         <<: *airflow-common
         profiles:
          - debug
         environment:
          <<: *airflow-common-env
           CONNECTION_CHECK_MAX_COUNT: "0"
         # Workaround for entrypoint issue. See: https://github.com/apache/airflow/issues/16252
         command:
           - bash
           - -c
           - airflow
         depends_on:
           <<: *airflow-common-depends-on

       # You can enable flower by adding "--profile flower" option e.g. docker-compose --profile flower up
       # or by explicitly targeted on the command line e.g. docker-compose up flower.
       # See: https://docs.docker.com/compose/profiles/
       flower:
         <<: *airflow-common
         command: celery flower
         profiles:
           - flower
         ports:
           - "5555:5555"
         healthcheck:
           test: ["CMD", "curl", "--fail", "http://localhost:5555/"]
           interval: 30s
           timeout: 10s
           retries: 5
           start_period: 30s
         restart: always
         depends_on:
           <<: *airflow-common-depends-on
           airflow-init:
             condition: service_completed_successfully

     volumes:
       postgres-db-volume:


![image](https://github.com/user-attachments/assets/f6de7b0b-b30a-44dd-85fe-14a8ec817de9)

Luego, en la terminal entramos a la carpeta de Airflow. Pero primero salimos de walmart_project a la carpeta principal dbt_project.

Código:

       cd ..

Código:

        cd Airflow

y creamos las siguientes carpetas en el directorio.

Código:

        mkdir dags, plugins, logs, config


![image](https://github.com/user-attachments/assets/bee78e1d-5e89-41fd-b23e-ad00969f18de)

Luego, creamos el archivo .env

Código:

 ============================================
 Configuración de Airflow
 ============================================
FERNET_KEY=46BKJoQYlPPOexq0OhDZnIlNepKFf87WFwLbfzqDDho=

 ============================================
 Credenciales de Airflow
 ============================================
_AIRFLOW_WWW_USER_USERNAME=airflow
_AIRFLOW_WWW_USER_PASSWORD=airflow

 ============================================
 Directorios del proyecto
 ============================================
AIRFLOW_PROJ_DIR=.

 ============================================
 Configuración de la base de datos
 ============================================
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
AIRFLOW__CELERY__RESULT_BACKEND=db+postgresql+psycopg2://airflow:airflow@postgres/airflow
AIRFLOW__CELERY__BROKER_URL=redis://:@redis:6379/0

 ============================================
 Configuración adicional
 ============================================
AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=true
AIRFLOW__CORE__LOAD_EXAMPLES=false

 Para Windows (opcional)
AIRFLOW_UID=50000

_______________________________________________________________________________________________________________________________________________________________________________________________________________
![image](https://github.com/user-attachments/assets/8690d0e9-e537-4289-bee2-1224b7963915)

Ahora, hacemos una copia de la carpeta Walmart_project y lo pegamos dentro de la carpeta de Airflow.

![image](https://github.com/user-attachments/assets/b46ed8ac-7da4-458e-a4ef-17ede5f19648)

Ahora, agregamos Airflow Project Dir dentro de docker-compose en la configuración de volumes.

Código:

- ${AIRFLOW_PROJ_DIR:-.}/walmart_project:/opt/airflow/walmart_project

![image](https://github.com/user-attachments/assets/9302b803-493b-4615-8d6b-2b55ccf9469d)

Luego en la parte de desarrollo (enviroment), cambiamos AIRFLOW__CORE__LOAD_EXAMPLES: 'true' por AIRFLOW__CORE__LOAD_EXAMPLES: 'false'


![image](https://github.com/user-attachments/assets/5b228785-36c2-4887-9904-2c0500330b36)

OJO: No olvidar guardar los cambios

Ahora, levantamos docker compose desde la terminal.

Código:
 
        docker compose up -d

![image](https://github.com/user-attachments/assets/c9d49ee7-3eeb-4e7f-978d-68c727fc396e)

Verificamos en docker desktop la creación del container Airflow.

![image](https://github.com/user-attachments/assets/f925cae6-61e1-40e7-8bf7-87e5607b3668)

Ahora, abriremos en nuestro navegador el localhost:8080/dags de Airflow para ir monitoreando el desarrollo.


![image](https://github.com/user-attachments/assets/527761a3-b513-4603-b9c3-53c94dfc90b7)

Luego, vamos a la carpeta Airflow/dags y creamos el archivo llamado orchestrate.py

![image](https://github.com/user-attachments/assets/db7e8bfb-de28-4dde-be91-78cc767bde99)

Primero vamos a la terminal y en la carpeta raíz ejecutamos código.

Código:

        cd ..

código:

        uv add apache-airflow

![image](https://github.com/user-attachments/assets/fd68a43f-3637-4460-b091-04bfbb39ee98)

Ahora, volvemos al archivo orchestrate.py y escribimos el siguiente código.

Código:

        from airflow.sdk import dag, task

        @dag
        def orchestrate():

            @task
            def ingest_cdc():
                return "CDC data ingested"

            @task.bash
            def source_freshness():
                return "dbt source freshness"

 
Y en la terminal ejecutamos

Código:

        cd Walmart_project


código:

        dbt source freshness

![image](https://github.com/user-attachments/assets/59f4f7e7-03ef-4e44-9310-9e3f0802dec2)

Ahora, estableceremos manualmente el trabajo de directorio usando el comando “cd” antes de ejecutar. Así es que, pasaremos a la carpeta raíz y, entraremos a la carpeta Airflow\dags 

Código:

        cd ..

Código:

        cd airflow


Código:

        cd dags

![image](https://github.com/user-attachments/assets/e9748273-e6ab-4c94-9a05-968e273b4695)

Y ahora modificamos el código del archivo orchestrate.py

Código:

        from airflow.sdk import dag, task
        from airflow.providers.standard.operators.bash import BashOperator
        from datetime import datetime

        @dag(
            dag_id='orchestrate',
            schedule='@daily',
            start_date=datetime(2024, 1, 1),
            catchup=False,
            tags=['walmart', 'dbt']
        )
        def orchestrate():

            @task
            def ingest_cdc():
                return "CDC data ingested"

            clean_target = BashOperator(
                task_id='clean_target',
                bash_command='rm -rf /opt/airflow/walmart_project/target && rm -rf /opt/airflow/walmart_project/logs',
                cwd='/opt/airflow/walmart_project'
            )

            source_freshness = BashOperator(
                task_id='source_freshness',
                bash_command='dbt source freshness',
                cwd='/opt/airflow/walmart_project'
            )

            silver_technical = BashOperator(
                task_id='silver_technical',
                cwd='/opt/airflow/walmart_project',
                bash_command='dbt run --select silver_t'
            )

            silver_technical_tests = BashOperator(
                task_id='silver_technical_tests',
                cwd='/opt/airflow/walmart_project',
                bash_command='dbt test --select silver_t'
            )

            silver_business = BashOperator(
                task_id='silver_business',
                cwd='/opt/airflow/walmart_project',
                bash_command='dbt run --select silver_b'
            )

            silver_business_tests = BashOperator(
                task_id='silver_business_tests',
                cwd='/opt/airflow/walmart_project',
                bash_command='dbt test --select silver_b'
            )

            gold_eph = BashOperator(
                task_id='gold_ephemeral',
                cwd='/opt/airflow/walmart_project',
                bash_command='dbt run --select gold'
            )

            gold_dimensions = BashOperator(
                task_id='gold_dimensions',
                cwd='/opt/airflow/walmart_project',
                bash_command='dbt snapshot'
            )

            gold_facts = BashOperator(
                task_id='gold_facts',
                cwd='/opt/airflow/walmart_project',
                bash_command='dbt run --select gold/fact'
            )

            # Definir la dependencia
            ingest_cdc_task = ingest_cdc()
    
            # Cadena de ejecución
            ingest_cdc_task >> clean_target >> source_freshness >> silver_technical >> silver_technical_tests >> silver_business >> silver_business_tests >> gold_eph >> gold_dimensions >> gold_facts

        orchestrate_dag = orchestrate()


![image](https://github.com/user-attachments/assets/b0da7675-4c64-468a-b6e3-491d0620f082)

Para eliminar esa linea bajo airflow.operator y evitar problema en la ejecucion, agregaremos el siguiente paquete desde la terminal.

Código:

        uv add airflow-operators

![image](https://github.com/user-attachments/assets/7632aafc-4d2b-4f55-9b2b-461ad2599e53)

Luego, creamos un Dockerfile en la carpeta de Airflow.

![image](https://github.com/user-attachments/assets/58e6e60c-4b5a-41db-87e7-e29a40fb0f8c)

Código:

        FROM apache/airflow:3.3.1

![image](https://github.com/user-attachments/assets/6c5d5769-2922-42bf-9838-29fcc92b3ae8)

Luego, en la terminal, en la carpeta raíz ejecutamos

Código:

        python3 -m pip freeze > requirements.txt

y se creará el archivo requirements.txt, el cual limpiaremos todo y pasaremos el siguiente código.

Código:

        airflow-operators>=0.11.0
        apache-airflow>=3.3.1
        dbt-core>=1.12.3
        dbt-databricks>=1.10.9

![image](https://github.com/user-attachments/assets/2e277dff-5f4e-4c80-98cc-3cbffe6d28fe)

Luego, corremos el siguiente código.

Código:

        uv pip install -r requirements.txt

![image](https://github.com/user-attachments/assets/5a6505db-b44f-43f0-9c9c-27b32656c9dc)

ahora, regresamos a Dockerfile y completamos el código.

Código:

        FROM apache/airflow:3.3.1

        USER root

        RUN apt-get update && apt-get install -y gcc && apt-get clean

        USER airflow

        COPY ./requirements.txt .

        RUN pip install --no-cache-dir -r requirements.txt


Luego, en la terminal desinstalamos el docker compose para cargar o levantar otra versión mejorada. Para ello, entraremos primero en la carpeta Airflow.

Código:

        cd airflow


Código:

        Docker compose down

![image](https://github.com/user-attachments/assets/a91037ab-bff9-4e3d-a439-c52a46fb0f01)

Verificamos en docker desktop que este vacío.

![image](https://github.com/user-attachments/assets/79f6321e-4719-4176-8f52-4832f10da6e9)

Ahora, levantamos la infraestructura con docker compose

Código:

        Docker compose build


Código:

        Docker compose up -d

![image](https://github.com/user-attachments/assets/a153cdd4-40df-4c47-839b-97fc4d4d4cda)

![image](https://github.com/user-attachments/assets/c3bdf3e1-7da9-493d-bc25-554a8e41925c)

* Verificar que los contenedores estén corriendo:

Código:

        docker ps

Deberías ver:
 
             - airflow-apiserver
             - airflow-scheduler
             - airflow-worker
             - airflow-dag-processor
             - airflow-triggerer
             - postgres
             - redis

* Verificar que dbt está instalado en los contenedores:

1. Verificar en el scheduler

codigo:

        docker-compose exec airflow-scheduler dbt --version

2. Verificar en el worker (IMPORTANTE)

codigo:

        docker-compose exec airflow-worker dbt --version


* Copiar el archivo profiles.yml a los contenedores:

- Crear directorio .dbt en cada contenedor

Código:

        docker-compose exec airflow-scheduler mkdir -p /home/airflow/.dbt
        docker-compose exec airflow-dag-processor mkdir -p /home/airflow/.dbt
        docker-compose exec airflow-worker mkdir -p /home/airflow/.dbt


- Copiar profiles.yml a cada contenedor

Código:

        docker cp C:\Users\User\.dbt\profiles.yml airflow-airflow-scheduler-1:/home/airflow/.dbt/profiles.yml
        docker cp C:\Users\User\.dbt\profiles.yml airflow-airflow-dag-processor-1:/home/airflow/.dbt/profiles.yml
        docker cp C:\Users\User\.dbt\profiles.yml airflow-airflow-worker-1:/home/airflow/.dbt/profiles.yml

- Verificar que se copió correctamente

Código:

        docker-compose exec airflow-worker cat /home/airflow/.dbt/profiles.yml


Verificar la conexión a Databricks:

- Entrar al worker

Código:

        docker-compose exec airflow-worker bash

- Ir al proyecto dbt

Código:

        cd /opt/airflow/walmart_project

- Probar la conexión

Código:

        dbt debug

** Deberías ver "All checks passed!"

- Salir

Código:

        exit

_______________________________________________________________________________________________________________________________________________________________________________________________________________

### 🚀 PASO 8: Ejecutar el DAG

1.	Despausar el DAG.

Código:

        docker-compose exec airflow-scheduler airflow dags unpause orchestrate

2.	 Ejecutar el DAG manualmente:

Código:

        docker-compose exec airflow-scheduler airflow dags trigger orchestrate

3.	 Monitorear la ejecución

- Ver logs del worker en tiempo real

Código:

        docker-compose logs -f airflow-worker


-  Ver logs del scheduler

Código:

        docker-compose logs -f airflow-scheduler


4.	Ver el estado del DAG


- Ver el estado


Código:
                  
       docker-compose exec airflow-scheduler airflow dags state orchestrate

                 
- Ver todas las ejecuciones.

Código:
         
        docker-compose exec airflow-scheduler airflow dags list-runs --dag-id orchestrate


-  Ver el estado de las tareas

Código:

        docker-compose exec airflow-scheduler airflow tasks states-dag-run --dag-id orchestrate --run-id manual__YYYY-MM-DDTHH:MM:SS

_______________________________________________________________________________________________________________________________________________________________________________________________________________
### 🧹 PASO 9: Comandos de limpieza

9.1 Limpiar ejecuciones específicas (si es necesario)


-  Ver los run_ids disponibles.

Código:

        docker-compose exec airflow-scheduler airflow dags list-runs --dag-id orchestrate

-  Limpiar una ejecución específica.

codigo:

        docker-compose exec airflow-scheduler airflow dags clear --run-id manual__2026-09-08T00:22:33.028726+00:00 orchestrate


9.2 Limpiar por fecha

Código:

        docker-compose exec airflow-scheduler airflow dags clear --partition-date-start 2024-01-01 orchestrate


9.3 Reiniciar todo (desde cero)

- Detener y eliminar contenedores.

Código:

        docker-compose down -v

- Reconstruir

Código:

        docker-compose build


- Iniciar

Código:

        docker-compose up -d


- Ver logs

Código:

        docker-compose logs -f


_______________________________________________________________________________________________________________________________________________________________________________________________________________
### 🔍 PASO 10: Comandos de diagnóstico

**10.1 Verificar que el DAG está cargado**

Código:

        docker-compose exec airflow-scheduler airflow dags list | grep orchestrate

**10.2 Ver errores de importación:**

Código:

        docker-compose exec airflow-scheduler airflow dags list-import-errors

**10.3 Ver logs de una tarea específica**

Código:

        docker-compose exec airflow-scheduler airflow tasks logs orchestrate source_freshness 2026-09-08


**10.4 Ver el contenido del archivo de DAG**

Código:

        docker-compose exec airflow-scheduler cat /opt/airflow/dags/orchestrate.py


**10.5 Ver el estado de todos los contenedores:**


Código:

        docker ps
        docker stats



**✅ Verificación final**

Después de seguir todos los pasos, deberías ver:

1.	✅ Todos los contenedores corriendo (docker ps).
2.	✅ dbt instalado en el worker (docker-compose exec airflow-worker dbt --version).
3.	✅ profiles.yml en el worker (docker-compose exec airflow-worker cat /home/airflow/.dbt/profiles.yml).
4.	✅ El DAG visible en http://localhost:8080
5.	✅ Todas las tareas ejecutándose sin errores.


_______________________________________________________________________________________________________________________________________________________________________________________________________________

### 🐛 Solución de problemas comunes


Error: "dbt: command not found"

- Instalar dbt en el worker

Código:

        docker-compose exec -u 0 airflow-worker python -m pip install dbt-core dbt-databricks


Error: "profiles.yml not found"

- Crear directorio y copiar archivo

Código:

        docker-compose exec airflow-worker mkdir -p /home/airflow/.dbt
        docker cp C:\Users\User\.dbt\profiles.yml airflow-airflow-worker-1:/home/airflow/.dbt/profiles.yml


Error: "Connection test failed"

- Entrar al worker y verificar manualmente

Código:

        docker-compose exec airflow-worker bash
        cd /opt/airflow/walmart_project
        dbt debug


El DAG no aparece en la UI

- Ver errores de importación

Código:

        docker-compose exec airflow-scheduler airflow dags list-import-errors


- Forzar recarga

Código:

        docker-compose restart airflow-dag-processor
        docker-compose restart airflow-scheduler


**¡¡FELICITACIONES! 🎉 Has configurado exitosamente un pipeline completo con Airflow, dbt y Databricks!**



![image](https://github.com/user-attachments/assets/4a0f68c0-d665-4085-8a37-b61d63cedfd8)

![image](https://github.com/user-attachments/assets/2022e6d6-0e57-4473-81b7-a19277aac195)

![image](https://github.com/user-attachments/assets/7ffa8b7e-e86f-4d85-8c8a-7b68588a1108)

![image](https://github.com/user-attachments/assets/ee137dd7-0cde-42f1-8219-fe821804ba8a)

