# MetroGPT: Agente Inteligente de Movilidad (EP2)

> **Ingenieria de Soluciones con IA** | *LangChain Agent con herramientas, memoria y planificacion*

[![Python](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-339933?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Status](https://img.shields.io/badge/Status-EP2_Implementado-green?style=for-the-badge)](#)

---

## Tabla de Contenidos

1. [Descripcion del Proyecto](#descripcion-del-proyecto)
2. [Arquitectura del Agente](#arquitectura-del-agente)
3. [Diagrama de Orquestacion](#diagrama-de-orquestacion)
4. [Componentes del Sistema](#componentes-del-sistema)
5. [Herramientas del Agente (IE1)](#herramientas-del-agente-ie1)
6. [Framework (IE2)](#framework-ie2)
7. [Memoria y Contexto (IE3 + IE4)](#memoria-y-contexto-ie3--ie4)
8. [Planificacion y Decisiones (IE5 + IE6)](#planificacion-y-decisiones-ie5--ie6)
9. [Instalacion y Ejecucion](#instalacion-y-ejecucion)
10. [Estructura del Repositorio](#estructura-del-repositorio)
11. [Referencias (APA)](#referencias-apa)

---

## Descripcion del Proyecto

Este proyecto implementa un **agente conversacional autonomo** para el Metro de Santiago utilizando **LangChain Agents** con GPT-4o. El agente integra herramientas de consulta, escritura y razonamiento, configuracion de memoria de corto y largo plazo, y estrategias de planificacion para resolver consultas complejas de movilidad urbana.

### Indicadores de Logro Cubiertos

| IE | Descripcion | Estado |
|----|-------------|--------|
| IE1 | Configuracion de herramientas del agente | 4 herramientas funcionales |
| IE2 | Integracion de frameworks escalables | LangChain + OpenAI Functions |
| IE3 | Memoria de contenido (corto plazo) | ConversationBufferMemory |
| IE4 | Recuperacion semantica (largo plazo) | Embeddings + busqueda por similitud |
| IE5 | Planificacion de tareas | ReAct + prompt de planificacion |
| IE6 | Toma de decisiones adaptativa | 5 escenarios demostrados |
| IE7 | README + diagrama de orquestacion | Documentacion completa |
| IE8 | Justificacion de componentes | Seccion de justificacion tecnica |
| IE9 | Informe tecnico con diagramas | README + diagramas Mermaid |
| IE10 | Lenguaje tecnico y evidencias | Argumentacion con ejemplos |

---

## Arquitectura del Agente

### Diagrama de Orquestacion (IE7)

```mermaid
graph TD
    subgraph "Usuario"
        U[Pasajero] -->|Consulta en lenguaje natural| AG[Agente LangChain]
    end

    subgraph "Capa de Memoria"
        CP[Memoria Corto Plazo<br/>ConversationBufferMemory<br/>IE3] --> AG
        LP[Memoria Largo Plazo<br/>MemoriaSemantica<br/>Embeddings + Similitud<br/>IE4] --> AG
    end

    subgraph "Agente (ReAct)"
        AG -->|Planifica| PLAN[Plan de Accion<br/>IE5]
        PLAN -->|Selecciona| SEL[Seleccion de Herramienta<br/>IE6]
        SEL -->|Ejecuta| TOOL[Herramienta]
        TOOL -->|Resultado| EVAL[Evaluacion]
        EVAL -->|Requiere mas pasos| PLAN
        EVAL -->|Respuesta final| AG
    end

    subgraph "Herramientas (IE1)"
        T1[consultar_tarifa<br/>Consulta] -.-> TOOL
        T2[consultar_ruta<br/>Consulta] -.-> TOOL
        T3[generar_plan_viaje<br/>Escritura] -.-> TOOL
        T4[razonar_viaje<br/>Razonamiento] -.-> TOOL
    end

    subgraph "Base de Conocimientos"
        KB[(Documentos<br/>Tarifas, Rutas,<br/>Combinaciones)] -->|Embeddings| T4
        KB -->|Consulta| T1
        KB -->|Consulta| T2
        KB -->|Contexto| T3
    end

    subgraph "LLM"
        LLM[GPT-4o<br/>GitHub Models API] -->|Procesa| AG
        KB -->|Indexacion| EMB[text-embedding-3-small]
        EMB -->|Vectores| KB
    end

    AG -->|Respuesta| U
```

### Flujo de Trabajo del Agente

```
1. INPUT:  Consulta en lenguaje natural del pasajero
      |
2. MEMORIA: Recupera contexto relevante
      |-- Corto plazo: ultimos mensajes (IE3)
      |-- Largo plazo: interacciones semanticamente similares (IE4)
      |
3. PLANIFICACION: El agente analiza y descompone la tarea (IE5)
      |-- Determina si es consulta, escritura o razonamiento
      |-- Decide el orden optimo de herramientas
      |
4. EJECUCION: Selecciona y ejecuta herramientas (IE1, IE6)
      |-- consultar_tarifa: para precios
      |-- consultar_ruta: para recorridos
      |-- generar_plan_viaje: para documentos estructurados
      |-- razonar_viaje: para analisis complejos
      |
5. EVALUACION: Verifica si la respuesta esta completa
      |-- Si falta informacion: vuelve al paso 3
      |-- Si esta completa: genera respuesta final
      |
6. OUTPUT: Respuesta al usuario con recomendaciones
```

---

## Componentes del Sistema

### Tabla de Componentes y Justificacion (IE8)

| Componente | Tecnologia | Justificacion |
|------------|-----------|---------------|
| **Framework de Agentes** | LangChain 0.3 | Framework maduro con soporte nativo para OpenAI Functions, memoria conversacional, y herramientas modulares. Permite escalar a agentes multi-paso sin cambiar la arquitectura base. |
| **Modelo de Lenguaje** | GPT-4o (via GitHub Models) | Balance optimo entre costo y capacidad de razonamiento. Soporta OpenAI Functions para integracion nativa con LangChain. GitHub Models provee el endpoint sin necesidad de suscripcion directa a OpenAI. |
| **Embeddings** | text-embedding-3-small | Modelo de embeddings de alta calidad con relacion costo-rendimiento favorable. Produce vectores de 1536 dimensiones optimizados para similitud coseno. |
| **Memoria Corto Plazo** | ConversationBufferMemory | Retiene el historial inmediato de la conversacion. Configurado con limite de 3000 tokens para evitar desbordamiento de contexto. |
| **Memoria Largo Plazo** | MemoriaSemantica (custom) | Implementacion propia que almacena resumenes de interacciones como embeddings. Recupera las semanticamente mas similares a la consulta actual, asegurando continuidad en flujos prolongados. |
| **Almacenamiento** | Estructuras en memoria (listas + numpy) | Evita dependencias externas (bases de datos vectoriales) manteniendo la funcionalidad completa de busqueda semantica. Escalable a Chroma/FAISS si se requiere persistencia. |
| **Contenedorizacion** | Docker + docker-compose | Entorno reproducible y portable. Configurado con Jupyter Lab para ejecucion interactiva. |
| **Autenticacion** | Variables de entorno (.env) | GITHUB_TOKEN y GITHUB_URL cargados desde .env. Seguro para repositorios publicos (incluido en .gitignore). |

---

## Herramientas del Agente (IE1)

El agente cuenta con 5 herramientas que cubren las categorias de consulta, escritura y razonamiento:

### 1. `consultar_tarifa(hora: str) -> str`
- **Tipo:** Consulta
- **Proposito:** Determina la tarifa aplicable segun el horario
- **Logica interna:** Calcula el bloque horario usando algebra de minutos:
  - 07:00-08:59 y 18:00-19:59 -> Punta ($840)
  - 09:00-17:59 y 20:00-20:44 -> Valle ($760)
  - 06:00-06:59 y 20:45-23:00 -> Bajo ($680)
- **Autonomia:** Funcion completa sin necesidad de LLM

### 2. `consultar_ruta(origen: str, destino: str) -> str`
- **Tipo:** Consulta
- **Proposito:** Obtiene la ruta optima entre dos estaciones
- **Logica interna:** Busca en tabla de rutas predefinidas; si no encuentra, usa busqueda semantica en la base de conocimientos
- **Autonomia:** Funcion completa, usa embeddings como respaldo

### 3. `generar_plan_viaje(origen: str, destino: str, hora: str) -> str`
- **Tipo:** Escritura
- **Proposito:** Produce un plan de viaje estructurado en formato JSON
- **Logica interna:** Orquesta las herramientas de consulta (tarifa + ruta) y estructura la salida como documento JSON
- **Autonomia:** Funcion completa, produce output estructurado listo para integracion con sistemas externos

### 4. `razonar_viaje(pregunta: str) -> str`
- **Tipo:** Razonamiento
- **Proposito:** Resuelve consultas complejas multi-paso
- **Logica interna:** Recupera contexto via embeddings, estructura el razonamiento en 4 pasos (horario -> ruta -> costo -> recomendacion), usa GPT-4o para integrar la respuesta
- **Autonomia:** Funcion completa con analisis avanzado

### 5. `enviar_correo(destinatario: str, asunto: str, cuerpo: str) -> str`
- **Tipo:** Escritura
- **Proposito:** Envia automaticamente un plan de viaje por correo electronico
- **Logica interna:** Usa SMTP con configuracion desde variables de entorno. Si no hay configuracion SMTP, guarda el correo como archivo `.eml` local.
- **Autonomia:** Funcion completa. Configuracion via `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS` en `.env`

---

## Framework (IE2)

Se utiliza **LangChain Agents** con arquitectura **OpenAI Functions** por las siguientes razones:

1. **Escalabilidad:** LangChain permite anadir nuevas herramientas sin modificar la logica del agente. La arquitectura de funciones permite que el LLM decida que herramienta usar segun el contexto.
2. **Compatibilidad:** Compatible con OpenAI, GitHub Models, Azure OpenAI, y cualquier API compatible. El agente funciona con `GITHUB_BASE_URL` sin cambios en el codigo.
3. **Modularidad:** Separacion clara entre herramientas, memoria, y logica del agente. Cada componente es independiente y reemplazable.
4. **Ecosistema:** Amplia documentacion, comunidad activa, y soporte para memoria conversacional, prompts personalizados, y manejo de errores.

---

## Memoria y Contexto (IE3 + IE4)

### Memoria de Corto Plazo (IE3)

Implementada con `ConversationBufferMemory` de LangChain:
- Almacena los ultimos mensajes del historial conversacional
- Configurado con `max_token_limit=3000` para control de costos
- Provee `chat_history` al agente en cada iteracion
- Se actualiza automaticamente via `save_context()` en cada turno

### Memoria de Largo Plazo (IE4)

Implementada como `MemoriaSemantica`, una clase personalizada que:
1. **Almacena:** Cada interaccion se resume como texto y se convierte en embedding via `text-embedding-3-small`
2. **Recupera:** Ante una nueva consulta, calcula similitud coseno contra todas las interacciones previas
3. **Inyecta:** Las 2 interacciones mas similares se agregan al prompt del sistema como contexto historico

**Ejemplo de recuperacion semantica:**
```
Usuario: "Mi abuela quiere viajar, cuanto paga?"
Recupera: "[Interaccion previa] Usuario: Cual es la tarifa para la tercera edad?
           Asistente: La tarifa para adultos mayores es de $240 en todo horario."
```

### Memoria Compuesta

La clase `MemoriaCompuesta` unifica ambos tipos de memoria en una interfaz comun compatible con LangChain:
- `memory_variables`: Retorna `["chat_history", "semantic_context"]`
- `load_memory_variables`: Combina buffer conversacional + recuperacion semantica
- `save_context`: Actualiza ambos sistemas de memoria simultaneamente

---

## Planificacion y Decisiones (IE5 + IE6)

### Planificacion de Tareas (IE5)

El agente utiliza el patron **ReAct (Reasoning + Acting)** implementado por LangChain:

1. **Analisis:** El prompt del sistema instruye al agente a descomponer problemas complejos
2. **Planificacion:** El agente decide que herramientas usar y en que orden
3. **Ejecucion secuencial:** Cada herramienta se ejecuta y su resultado se evalua antes del siguiente paso
4. **Verificacion:** El agente confirma que la respuesta cubre todos los aspectos de la consulta

### Toma de Decisiones (IE6)

El agente implementa un arbol de decision basado en el tipo de consulta:

| Tipo de Consulta | Ejemplo | Decision |
|-----------------|---------|----------|
| Tarifa | "Cuanto vale a las 14:30?" | `consultar_tarifa` |
| Ruta | "Como llego a San Pablo?" | `consultar_ruta` |
| Viaje completo | "Planifica mi viaje desde X a Y" | `generar_plan_viaje` |
| Multi-variable | "Que me conviene si viajo temprano?" | `razonar_viaje` |
| Seguimiento | "Y si voy dos horas despues?" | Memoria + herramienta adecuada |
| Envio por correo | "Envia el plan a juan@correo.cl" | `enviar_correo` |

**Demostracion de adaptabilidad:** En las demos del notebook, el agente:
- Cambia su comportamiento segun el horario (punta/valle/bajo)
- Recupera informacion de interacciones previas (memoria semantica)
- Sugiere alternativas cuando detecta oportunidades de ahorro
- Mantiene coherencia en conversaciones multi-turno

---

## Instalacion y Ejecucion

### Requisitos Previos

- Python 3.10 o superior
- Credenciales de GitHub Models (Token PAT)
- Docker (opcional, para contenedor)

### Instalacion Local

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/Codigo-Soluciones-con-IA.git
cd Codigo-Soluciones-con-IA

# 2. Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar archivo .env
# Crea un archivo .env en la raiz con:
# GITHUB_BASE_URL=https://models.inference.ai.azure.com
# GITHUB_TOKEN=tu_pat_token_aqui
# Opcional (para envio de correos):
# SMTP_HOST=smtp.gmail.com
# SMTP_PORT=587
# SMTP_USER=tu_correo@gmail.com
# SMTP_PASS=tu_contraseña_app
# SMTP_FROM=tu_correo@gmail.com

# 5. Ejecutar el notebook
jupyter lab EP2_Metro_Agent.ipynb
```

### Instalacion con Docker

```bash
docker-compose up -d
# Acceder a http://localhost:8888 con token: duoc2026
```

---

## Estructura del Repositorio

```
Codigo-Soluciones-con-IA/
├── EP2_Metro_Agent.ipynb      # [EP2] Agente LangChain con herramientas y memoria
├── EP1_Metro.ipynb             # [EP1] Asistente basico IL1.1
├── README.md                   # Documentacion principal
├── requirements.txt            # Dependencias del proyecto
├── .env                        # Variables de entorno (NO subir a git)
├── .gitignore                  # Exclusiones
├── Dockerfile                  # Contenedor Jupyter Lab
├── docker-compose.yml          # Orquestacion Docker
│
├── Dise-o-de-Soluciones-con-IA/    # [EP1] Documentacion de diseno
├── Parcial soluciones con IA/      # [EP1] Versiones de notebooks
└── Ordenadas/                      # [EP1] Notebooks organizados por IL
    └── IL's/
        ├── IL1.1_Metro.ipynb       # Streaming + memoria
        ├── IL1.2_Metro.ipynb       # JSON estructurado + metacognicion
        └── IL1.3_Metro.ipynb       # RAG con embeddings + busqueda semantica
```

---

## Referencias (APA)

1. LangChain. (2024). *LangChain Documentation: Agents*. Recuperado de https://python.langchain.com/docs/modules/agents/
2. OpenAI. (2024). *GPT-4o System Card*. Recuperado de https://openai.com/index/gpt-4o-system-card/
3. OpenAI. (2024). *Embeddings Documentation: text-embedding-3-small*. Recuperado de https://platform.openai.com/docs/guides/embeddings
4. GitHub. (2025). *GitHub Models - AI Model Marketplace*. Recuperado de https://github.com/marketplace/models
5. Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv preprint arXiv:2210.03629.
6. Chase, H. (2024). *Building Production-Ready Agents with LangChain*. En *Proceedings of the LLM Agents Workshop at NeurIPS 2024*.
7. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). *Attention Is All You Need*. Advances in Neural Information Processing Systems, 30.
8. Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems, 33.
