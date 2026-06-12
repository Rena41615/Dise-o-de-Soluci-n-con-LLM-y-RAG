# Soluciones con IA - Evaluaciones Parciales (EP1, EP2, EP3)

> **ISY0101** - Optativo Ingeniería de Soluciones con IA
>
> Implementación progresiva de un agente inteligente para el Metro de Santiago con enfoque en observabilidad y responsabilidad en IA

![Status](https://img.shields.io/badge/Status-3_EPs_Implemented-green?style=for-the-badge)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-339933?style=for-the-badge)](https://langchain.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

## 📋 Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Evaluaciones Parciales](#evaluaciones-parciales)
- [Inicio Rápido](#inicio-rápido)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## 📚 Descripción General

Este repositorio contiene la implementación de **tres evaluaciones parciales progresivas** de un curso de Ingeniería de Soluciones con IA. El proyecto desarrolla un **agente inteligente autónomo** para consultas del Sistema Metro de Santiago, evolucionando desde un simple análisis de datos (EP1) a un agente conversacional sofisticado con observabilidad completa (EP3).

### Objetivo General
Implementar un sistema integral de observabilidad para agentes de IA que permita:
- Monitorear métricas de desempeño en tiempo real
- Identificar puntos de falla y áreas de mejora
- Garantizar criterios éticos, privacidad y compliance
- Proponer optimizaciones basadas en datos observados

---

## 📂 Estructura del Proyecto

```
Codigo-Soluciones-con-IA-main/
├── EP1/                          # Evaluación Parcial 1 - Análisis de Datos
│   ├── src/                     # Código fuente
│   ├── docs/                    # Documentación
│   ├── notebooks/               # Jupyter notebooks
│   ├── results/                 # Resultados de análisis
│   └── README.md               # Documentación EP1
│
├── EP2/                          # Evaluación Parcial 2 - Agente Conversacional
│   ├── src/                     # Código del agente LangChain
│   ├── agents/                  # Configuración de agentes
│   ├── docs/                    # Documentación técnica
│   ├── notebooks/               # Jupyter notebooks
│   ├── results/                 # Logs de ejecución
│   └── README.md               # Documentación EP2
│
├── EP3/                          # Evaluación Parcial 3 - Observabilidad
│   ├── src/                     # Módulos de observabilidad
│   │   ├── metrics/            # Colector de métricas
│   │   ├── tracing/            # Logger estructurado
│   │   ├── security/           # Validación ética y compliance
│   │   └── utils/              # Utilidades (storage, análisis)
│   ├── notebooks/               # Análisis de datos
│   ├── dashboards/              # Dashboard Streamlit
│   ├── tests/                   # Pruebas unitarias
│   ├── docs/                    # Documentación
│   │   ├── SETUP.md            # Guía de configuración
│   │   ├── ARCHITECTURE.md     # Arquitectura del sistema
│   │   ├── FINDINGS.md         # Análisis y recomendaciones
│   │   └── REFERENCES.md       # Referencias bibliográficas
│   ├── config.yaml             # Configuración del sistema
│   ├── requirements.txt         # Dependencias
│   ├── main.py                 # Punto de entrada
│   └── README.md               # Documentación EP3
│
├── .github/                      # Configuración de GitHub
│   └── workflows/               # GitHub Actions (CI/CD)
│
├── .gitignore                   # Archivos ignorados
├── requirements.txt             # Dependencias globales
├── docker-compose.yml           # Orquestación de contenedores
├── Dockerfile                   # Imagen Docker
└── README.md                    # Este archivo

```

---

## 🎯 Evaluaciones Parciales

### EP1: Análisis de Datos Metro (Semanas 1-6)

**Objetivo:** Recopilar, limpiar y analizar datos del Sistema Metro

**Indicadores de Logro:**
- IL1.1: Recopilar datos de fuentes de APIs
- IL1.2: Limpiar y normalizar datos
- IL1.3: Análisis exploratorio y visualizaciones

**Tecnologías:** Pandas, Matplotlib, Seaborn, SQL

**Entregables:**
- Notebooks de análisis
- Dataset procesado
- Informe con visualizaciones

[Ver documentación completa de EP1](EP1/README.md)

---

### EP2: Agente Conversacional (Semanas 7-12)

**Objetivo:** Desarrollar un agente autónomo con herramientas, memoria y planificación

**Indicadores de Logro:**
- IL2.1: Integrar herramientas en el agente
- IL2.2: Implementar frameworks escalables (LangChain)
- IL2.3: Configurar memoria (corto y largo plazo)
- IL2.4: Planificación y toma de decisiones

**Tecnologías:** LangChain, OpenAI, ConversationMemory, Embeddings

**Entregables:**
- Agente LangChain funcional
- Herramientas integradas (4+)
- Dashboard de monitoreo
- Diagramas de arquitectura

[Ver documentación completa de EP2](EP2/README.md)

---

### EP3: Observabilidad y Optimización (Semanas 13-15)

**Objetivo:** Implementar sistema integral de observabilidad para agentes de IA

**Indicadores de Logro:**
- IL3.1: Aplicar métricas de observabilidad (precisión, latencia, consistencia)
- IL3.2: Analizar registros y trazabilidad
- IL3.3: Integrar protocolos de seguridad y responsabilidad
- IL3.4: Proponer mejoras basadas en datos observados

**Tecnologías:** Prometheus, Grafana, Streamlit, OpenTelemetry, Jaeger

**Entregables:**
- Colectores de métricas
- Dashboard de observabilidad
- Análisis completo con recomendaciones
- Informe técnico (máx 5 páginas)

[Ver documentación completa de EP3](EP3/README.md)

---

## 🚀 Inicio Rápido

### Prerrequisitos
- Python 3.8+
- Docker y Docker Compose (opcional)
- Git

### Instalación Rápida (EP3)

```bash
# 1. Clonar repositorio
git clone https://github.com/usuario/Codigo-Soluciones-con-IA-main.git
cd Codigo-Soluciones-con-IA-main

# 2. Navegar a EP3
cd EP3

# 3. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o: venv\Scripts\activate  # Windows

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Configurar
cp config.example.yaml config.yaml

# 6. Ejecutar sistema
python main.py

# 7. Abrir dashboard
streamlit run dashboards/main_dashboard.py
```

Acceso: http://localhost:8501

---

## 📦 Instalación

### Opción 1: Local

```bash
# Clonar y configurar
git clone <URL-repositorio>
cd Codigo-Soluciones-con-IA-main

# Instalar todas las dependencias
pip install -r requirements.txt

# Instalar dependencias específicas de cada EP
pip install -r EP1/requirements.txt
pip install -r EP2/requirements.txt
pip install -r EP3/requirements.txt
```

### Opción 2: Docker

```bash
# Construir imagen
docker build -t ia-soluciones .

# Ejecutar contenedor
docker run -p 8888:8888 -p 8501:8501 ia-soluciones

# O usar docker-compose
docker-compose up --build
```

---

## 💻 Uso

### EP1: Análisis de Datos

```bash
cd EP1
jupyter notebook notebooks/
```

Abre `01_data_exploration.ipynb` para comenzar.

### EP2: Agente Conversacional

```bash
cd EP2
jupyter notebook notebooks/

# O ejecutar directamente
python main.py
```

### EP3: Observabilidad

```bash
cd EP3

# Ejecutar análisis
python main.py --config config.yaml

# Ver dashboard
streamlit run dashboards/main_dashboard.py

# Ejecutar pruebas
pytest tests/ -v
```

---

## 📊 Ejemplos de Uso

### Ejemplo 1: Ejecutar Colector de Métricas

```python
from EP3.src.metrics.collector import MetricsCollector

config = {'metrics': {'enabled': True}}
collector = MetricsCollector(config)

metrics = collector.collect()
for metric in metrics:
    print(f"{metric['name']}: {metric['value']} {metric['unit']}")
```

### Ejemplo 2: Usar Logger Estructurado

```python
from EP3.src.tracing.logger import StructuredLogger

logger = StructuredLogger(config)
logger.log_event(
    event_type='request',
    message='Solicitud recibida',
    component='agent',
    context={'user': 'user_123'}
)
```

### Ejemplo 3: Validar Seguridad

```python
from EP3.src.security.security_manager import SecurityManager

security = SecurityManager(config)
checks = security.validate(metrics)
print(f"Verificaciones: {checks}")
```

---

## 🧪 Testing

```bash
# Ejecutar todas las pruebas
pytest tests/ -v

# Pruebas con cobertura
pytest tests/ --cov=src --cov-report=html

# Pruebas específicas
pytest tests/test_metrics.py -v
```

---

## 📖 Documentación

- **EP1**: [Análisis de Datos Metro](EP1/README.md)
- **EP2**: [Agente Conversacional](EP2/README.md)
- **EP3**: [Observabilidad Completa](EP3/README.md)
  - [Setup](EP3/docs/SETUP.md)
  - [Arquitectura](EP3/docs/ARCHITECTURE.md)
  - [Hallazgos](EP3/docs/FINDINGS.md)
  - [Referencias APA](EP3/docs/REFERENCES.md)

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Crea una rama con tu feature (`git checkout -b feature/nueva-feature`)
2. Commit tus cambios (`git commit -am 'Agrega nueva feature'`)
3. Push a la rama (`git push origin feature/nueva-feature`)
4. Abre un Pull Request

### Estándares de Código

- Usar PEP 8
- Documentar funciones con docstrings
- Incluir type hints
- Escribir tests para nuevas funcionalidades
- Mantener cobertura >80%

---

## 📝 Licencia

Este proyecto está bajo licencia **MIT**. Ver [LICENSE](LICENSE) para detalles.

---

## 👥 Equipo

- **Estudiantes:** [Nombres del equipo]
- **Docente:** [Nombre docente]
- **Universidad:** Pontificia Universidad Católica
- **Escuela:** Ingeniería

---

## 📞 Soporte

Para preguntas o problemas:

1. Revisa la documentación específica de cada EP
2. Consulta los [Issues](../../issues) existentes
3. Crea un nuevo [Issue](../../issues/new)
4. Contacta al equipo de desarrollo

---

## 🔗 Enlaces Útiles

- [LangChain Documentation](https://langchain.com)
- [OpenAI API](https://platform.openai.com)
- [Prometheus Docs](https://prometheus.io)
- [Streamlit Docs](https://docs.streamlit.io)
- [GitHub Guides](https://guides.github.com)

---

## 📅 Cronograma

| Etapa | Período | Estado |
|-------|---------|--------|
| EP1 - Análisis de Datos | Semanas 1-6 | ✅ Completado |
| EP2 - Agente IA | Semanas 7-12 | ✅ Completado |
| EP3 - Observabilidad | Semanas 13-15 | 🔄 En Progreso |

---

**Última actualización:** Junio 2025

*Para más información, consulta los READMEs individuales de cada Evaluación Parcial.*
