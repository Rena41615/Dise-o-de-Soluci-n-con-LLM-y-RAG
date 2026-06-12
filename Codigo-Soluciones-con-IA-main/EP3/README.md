# EP3 - Implementación de Observabilidad

**Evaluación Parcial N°3** | ISY0101 - Optativo Ingeniería de Soluciones con IA

## Descripción del Proyecto

En esta evaluación parcial, implementamos métricas de observabilidad y herramientas de trazabilidad sobre agentes de IA ya desarrollados. El objetivo es analizar registros de ejecución, visualizar el desempeño mediante dashboards y proponer recomendaciones fundamentadas para la optimización del sistema.

## Indicadores de Logro (IL)

- **IL3.1**: Aplica métricas de observabilidad para medir la precisión, latencia y consistencia de un agente de IA en escenarios con variabilidad de datos.
- **IL3.2**: Analiza registros de ejecución del agente, utilizando herramientas de trazabilidad, para identificar puntos de falla o mejora en flujos automatizados.
- **IL3.3**: Integra protocolos de seguridad y uso responsable en el diseño de agentes, considerando criterios éticos, normativos y de privacidad, en contextos de producción.
- **IL3.4**: Propone mejoras de desempeño o rediseño del agente, basándose en análisis de datos observados, con el fin de aumentar la sostenibilidad y escalabilidad de la solución.

## Estructura del Proyecto

```
EP3/
├── src/                      # Código fuente
│   ├── metrics/             # Módulo de métricas de observabilidad
│   ├── tracing/             # Módulo de trazabilidad
│   ├── security/            # Módulo de seguridad y responsabilidad
│   └── utils/               # Utilidades comunes
├── notebooks/               # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_metrics_analysis.ipynb
│   └── 03_recommendations.ipynb
├── dashboards/              # Dashboards de monitoreo
│   ├── main_dashboard.py   # Dashboard principal (Streamlit/Grafana)
│   └── config.json         # Configuración de dashboards
├── docs/                    # Documentación
│   ├── SETUP.md            # Instrucciones de configuración
│   ├── ARCHITECTURE.md     # Arquitectura del sistema
│   └── FINDINGS.md         # Hallazgos y análisis
├── tests/                   # Pruebas del software
│   ├── test_metrics.py
│   ├── test_tracing.py
│   └── test_security.py
├── results/                 # Resultados de análisis
│   ├── metrics_report.json
│   ├── logs/               # Logs de ejecución
│   └── visualizations/     # Gráficos y visualizaciones
├── requirements.txt         # Dependencias del proyecto
├── config.yaml             # Configuración general
└── main.py                 # Punto de entrada principal
```

## Requisitos

- Python 3.8+
- Jupyter Notebook
- Herramientas de monitoreo (Grafana, Kibana, Streamlit, PowerBI, etc.)

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL-del-repositorio>
cd Codigo-Soluciones-con-IA-main/EP3
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar ambiente

```bash
cp config.example.yaml config.yaml
# Editar config.yaml con tus parámetros
```

## Uso

### Ejecutar el análisis completo

```bash
python main.py --config config.yaml
```

### Ejecutar notebooks

```bash
jupyter notebook notebooks/
```

### Iniciar dashboard

```bash
streamlit run dashboards/main_dashboard.py
# o para Grafana/Kibana, seguir documentación específica
```

### Ejecutar pruebas

```bash
pytest tests/ -v
```

## Apartados Evaluados

### A. Implementación de Métricas de Observabilidad
Se aplican al menos tres métricas relevantes:
- **Precisión**: Medida de exactitud del agente
- **Latencia**: Tiempo de respuesta del agente
- **Consistencia**: Coherencia en las respuestas
- **Frecuencia de errores**: Tasa de fallos
- **Uso de recursos**: CPU, memoria, etc.

Ubicación: `src/metrics/`

### B. Análisis de Registros y Trazabilidad
Examen de logs de ejecución del agente:
- Identificación de puntos críticos de falla
- Áreas de mejora
- Documentación de hallazgos

Ubicación: `src/tracing/` y `docs/FINDINGS.md`

### C. Desarrollo de Dashboards de Monitoreo
Dashboard visual que muestra el comportamiento del agente:
- Gráficos de métricas clave
- Visualización en tiempo real
- Histórico de desempeño

Ubicación: `dashboards/main_dashboard.py`

### D. Propuesta de Recomendaciones
Reporte técnico con:
- Recomendaciones prácticas para optimizar desempeño
- Justificación de cada sugerencia
- Basadas en métricas y trazabilidad

Ubicación: `docs/FINDINGS.md`

### E. Redacción Técnica
Documentación clara, coherente y técnicamente correcta

Ubicación: `docs/`

### F. Visualizaciones
Capturas, gráficos y visualizaciones del dashboard

Ubicación: `results/visualizations/`

### G. Referencias
Todas las fuentes citadas bajo norma APA

Ubicación: `docs/REFERENCES.md`

## Resultados Principales

Ver `docs/FINDINGS.md` para análisis detallado y resultados principales.

## Ejecutando el Código

### Paso 1: Exploración de Datos
```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```

### Paso 2: Análisis de Métricas
```bash
python src/metrics/analyzer.py --input results/logs/ --output results/metrics_report.json
```

### Paso 3: Visualización
```bash
streamlit run dashboards/main_dashboard.py
```

### Paso 4: Generar Reporte
```bash
python src/utils/report_generator.py --metrics results/metrics_report.json --output results/report.pdf
```

## Contribuciones

Para contribuir, por favor:
1. Crea una rama (git checkout -b feature/nueva-metrica)
2. Realiza tus cambios
3. Haz commit (git commit -am 'Agrega nueva métrica')
4. Push a la rama (git push origin feature/nueva-metrica)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo licencia MIT.

## Contacto

Para preguntas o sugerencias, contactar al equipo de desarrollo.

## Notas Importantes

- Los logs se generan automáticamente en `results/logs/`
- Los reportes se guardan en `results/`
- Las visualizaciones se actualizan en tiempo real en el dashboard
- Para ambiente de producción, revisar `docs/ARCHITECTURE.md`

---

**Última actualización**: Junio 2025
