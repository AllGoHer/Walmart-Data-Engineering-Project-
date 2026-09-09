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

      git clone https://github.com/tuusuario/walmart-data-engineering.git

      cd walmart-data-engineering

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

- ! [Documentación de Apache Airflow](https://airflow.apache.org/docs/)

- ! [Documentación de dbt](https://docs.getdbt.com/?version=2)

- ! [Documentación de Databricks](https://docs.databricks.com/aws/en)

____________________________________________________________________________________________________________________________________________________________________________________________________________________________

### 🚀 DESARROLLO WALMART PROJECT

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
