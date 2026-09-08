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

┌─────────────────────────────────────────────────────────────────────────┐
│                         FUENTES DE DATOS                                │
├─────────────────┬────────────────────┬──────────────────────────────────┤
│   BD OLTP       │   Data Lake S3     │       Tablas de Metadatos        │
│   (PostgreSQL)  │   (Datos Externos) │       (Configuración)            │
└────────┬────────┴─────────┬──────────┴──────────┬───────────────────────┘
         │                  │                     │
         ▼                  ▼                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    INGESTA INCREMENTAL                                  │
│                   (Databricks / Spark)                                  │
└─────────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     LAKEHOUSE EN DATABRICKS                             │
├─────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │
│  │  Capa Silver    │  │  Capa Business  │  │  Capa Gold (Star Schema)│  │
│  │  (Técnica)      │→ │  (Enriquecida)  │→ │  Hechos y Dimensiones   │  │
│  │  - Modelos dbt  │  │  - Modelos dbt  │  │  - SCD Tipo 2           │  │
│  │  - Incremental  │  │  - Pruebas      │  │  - Modelos Efímeros     │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      ORQUESTACIÓN Y MONITOREO                           │
│                      (Apache Airflow + Docker)                          │
└─────────────────────────────────────────────────────────────────────────┘


![image](https://github.com/user-attachments/assets/0c5c058a-bec5-4cde-8af4-8fcf5df366d2)

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()

![image]()
