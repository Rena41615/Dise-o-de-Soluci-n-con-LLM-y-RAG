# 🚇 MetroGPT: Asistente Inteligente de Movilidad
> **Ingeniería de Soluciones con IA** | *Evolución hacia arquitecturas RAG*

![Python](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991.svg?style=for-the-badge&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-IL1.3_Implemented-green?style=for-the-badge)

Este repositorio documenta la evolución técnica de un asistente virtual diseñado para optimizar la experiencia de los pasajeros en el **Metro de Santiago**. El proyecto escala desde una simple conexión de API hasta un sistema complejo de **Recuperación Aumentada por Generación (RAG)**.

---

## 📈 Hoja de Ruta Técnica (Hitos)

El proyecto se divide en fases incrementales de inteligencia y robustez:

### 🔹 IL 1.1: Conectividad y Fluidez
* **Core:** Integración con GitHub Models API.
* **UX:** Implementación de **Streaming** para respuestas en tiempo real.
* **Lógica:** Gestión de memoria conversacional para mantener el contexto del viaje.

### 🔹 IL 1.2: Extracción y Metacognición
* **Prompt Engineering:** Uso de **Few-Shot Prompting** para estandarizar la salida.
* **Estructura:** Generación de respuestas en **JSON puro** para integración con bases de datos.
* **Razonamiento:** Implementación de **Chain-of-Thought (CoT)** mediante una llave de `metacognicion`.

### 🔹 IL 1.3: Arquitectura RAG (Vectores)
* **Semántica:** Uso de **Embeddings** (`text-embedding-3-small`) para entender el significado real de las consultas.
* **Búsqueda:** Motor de búsqueda por **Similitud de Coseno** sobre una base de conocimientos técnica.
* **Precisión:** El modelo ya no "alucina"; recupera datos exactos de tarifas y líneas antes de generar la respuesta.

---

## 🏗️ Arquitectura del Sistema


1.  **Input:** Consulta en lenguaje natural del pasajero.
2.  **Retrieval:** Búsqueda vectorial en la base de conocimientos (Tarifas/Líneas).
3.  **Augmentation:** Inyección de los fragmentos recuperados en el Prompt.
4.  **Generation:** GPT-4o procesa el contexto y genera un JSON validado.

---

## 🚀 Instalación y Despliegue

Garantizamos la portabilidad mediante **Docker**, permitiendo que el entorno de Jupyter sea idéntico en cualquier computador.

1.  **Clonar y configurar:**
    ```bash
    git clone [https://github.com/tu-usuario/nombre-repo.git](https://github.com/tu-usuario/nombre-repo.git)
    cd nombre-repo
    # Configurar .env con tu GITHUB_TOKEN
    ```

2.  **Levantar con Docker Compose:**
    ```bash
    docker-compose up -d
    ```

3.  **Verificar servidor:**
    ```bash
    docker-compose ps
    ```
    *Acceda al enlace con el token generado en la terminal.*

---

## 💎 Ejemplo de Output (JSON Pro)

```json
{
    "metacognicion": "Usuario consulta por horario tarde (18:30). Se identifica bloque PUNTA.",
    "respuesta": "La tarifa es de $840. Debes tomar L4 en Plaza Puente Alto y combinar en Tobalaba con L1.",
    "fuentes_usadas": ["Horario Punta (18:00-19:59): $840", "Línea 4 combina con L1 en Tobalaba"]
}