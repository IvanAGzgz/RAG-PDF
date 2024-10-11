# Preguntas y Respuestas sobre la Constitución Española con OpenAI y LangChain

Este proyecto implementa un sistema de **preguntas y respuestas** (Q&A) sobre la **Constitución Española** utilizando un enfoque de **Retrieval-Augmented Generation (RAG)**, mediante la base de datos **ChromaDB** y **OpenAI**. El sistema permite realizar preguntas sobre los artículos y funcionamiento de la Constitución Española, proporcionando respuestas basadas en el contenido de este documento.

### ¿Cómo funciona?
1. **Ingesta de datos**: El script `create_database.py` carga el texto completo de la Constitución Española desde un archivo PDF, lo divide en fragmentos más pequeños (chunks) y crea embeddings utilizando **OpenAI**.
2. **Base de datos de embeddings**: Los fragmentos se almacenan en **ChromaDB**, una base de datos vectorial optimizada para realizar búsquedas semánticas eficientes.
3. **Aplicación de preguntas**: El script `app.py` permite hacer preguntas sobre la Constitución Española. Utiliza un **prompt template** personalizado para garantizar que las respuestas sean claras y estén basadas en el contexto relevante.

## Ejemplos de preguntas

Puedes hacer preguntas como:
- ¿Qué dice el artículo 50?
- ¿Cómo funciona la Constitución Española?
- ¿Qué derechos reconoce la Constitución?

## Capturas de Pantalla

A continuación, se muestran ejemplos de cómo funciona la aplicación:

![Interfaz de Preguntas](./Captura1.PNG)
*Figura 1: Interfaz de la aplicación donde se introducen las preguntas.*

![Respuesta Generada](./Captura2.PNG)
*Figura 2: Ejemplo de una respuesta generada basada en los artículos relevantes de la Constitución Española.*

## Estructura del proyecto

Este repositorio contiene dos scripts principales:

### 1. `create_database.py`
Este script se encarga de crear la base de datos de embeddings a partir del contenido de la Constitución Española.

#### Pasos:
- Carga el PDF de la Constitución.
- Divide el documento en fragmentos utilizando `RecursiveCharacterTextSplitter` de **LangChain**.
- Genera embeddings para cada fragmento utilizando `OpenAIEmbeddings`.
- Guarda los embeddings en **ChromaDB** para su posterior consulta.

#### Uso:
Para ejecutar el script y crear la base de datos, utiliza el siguiente comando en la terminal:

```bash
python create_database.py
