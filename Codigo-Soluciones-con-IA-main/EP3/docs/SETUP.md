# SETUP.md - Guía de Configuración EP3

## Configuración Inicial Rápida

### 1. Requisitos Previos

- Python 3.8 o superior
- pip o conda
- Git
- ~5GB de espacio en disco (incluye dependencias y logs)

### 2. Instalación del Proyecto

#### Opción A: Instalación Local

```bash
# Clonar repositorio
git clone <URL-del-repositorio>
cd Codigo-Soluciones-con-IA-main/EP3

# Crear entorno virtual
python -m venv venv

# Activar entorno
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

#### Opción B: Instalación con Docker

```bash
# Construir imagen
docker build -t ep3-observability .

# Ejecutar contenedor
docker run -p 8501:8501 -v $(pwd)/results:/app/results ep3-observability
```

### 3. Configuración Inicial

```bash
# Copiar configuración de ejemplo
cp config.example.yaml config.yaml

# Editar configuración (según necesidad)
# Cambios comunes:
# - metrics.collection_interval: ajustar según carga
# - tracing.log_level: DEBUG para desarrollo
# - dashboard.framework: elegir herramienta preferida
```

### 4. Inicializar Base de Datos (Opcional)

```bash
python src/utils/init_db.py
```

### 5. Ejecutar Pruebas

```bash
pytest tests/ -v --cov=src
```

## Verificación de Instalación

```bash
# Verificar que todo está correctamente instalado
python -c "import metrics, tracing, security; print('✓ Instalación correcta')"

# Ver versión
python -c "import ep3; print(ep3.__version__)"
```

## Estructuras de Datos Clave

### Formato de Métricas

```json
{
  "timestamp": "2025-06-09T10:30:00Z",
  "agent_id": "metro_agent_v1",
  "metrics": {
    "precision": 0.95,
    "latency_ms": 245,
    "consistency": 0.98,
    "error_rate": 0.02,
    "cpu_usage": 35.5,
    "memory_mb": 512
  },
  "status": "success"
}
```

### Formato de Logs

```json
{
  "timestamp": "2025-06-09T10:30:00Z",
  "level": "INFO",
  "component": "agent.process",
  "message": "Procesando solicitud",
  "request_id": "req_12345",
  "duration_ms": 245
}
```

## Troubleshooting

### Problema: ImportError en módulos locales

**Solución:**
```bash
# Asegurar que EP3 está en PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Problema: Puerto 8501 en uso

**Solución:**
```bash
streamlit run dashboards/main_dashboard.py --server.port 8502
```

### Problema: Permisos insuficientes para escribir logs

**Solución:**
```bash
chmod -R 755 results/
```

### Problema: Dependencias conflictivas

**Solución:**
```bash
# Limpiar e reinstalar
pip install --upgrade --force-reinstall -r requirements.txt
```

## Ambiente de Desarrollo vs Producción

### Desarrollo

```yaml
# config.yaml
tracing:
  log_level: "DEBUG"
  
security:
  privacy:
    encrypt_logs: false
```

```bash
# Ejecutar con recarga automática
pytest tests/ --watch
```

### Producción

```yaml
# config.yaml
tracing:
  log_level: "WARNING"
  
security:
  privacy:
    encrypt_logs: true
    anonymize_data: true
```

```bash
# Ejecutar con gunicorn
gunicorn -w 4 dashboards.main_dashboard:app
```

## Integración Continua

### GitHub Actions

```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r EP3/requirements.txt
      - run: pytest EP3/tests/ -v
```

## Actualizar Dependencias

```bash
# Ver dependencias desactualizadas
pip list --outdated

# Actualizar todas
pip install --upgrade -r requirements.txt

# Generar nuevo archivo de dependencias
pip freeze > requirements.txt
```

## Monitoreo en Producción

```bash
# Ver logs en tiempo real
tail -f results/logs/execution.log

# Análisis de logs
grep "ERROR" results/logs/execution.log | wc -l

# Usar herramientas avanzadas
# - ELK Stack (Elasticsearch, Logstash, Kibana)
# - Prometheus + Grafana
# - Jaeger para trazas distribuidas
```

## Variables de Entorno

```bash
# .env (crear archivo)
OPENAI_API_KEY=sk-...
MONGO_URI=mongodb://localhost:27017
LOG_LEVEL=INFO
DEBUG_MODE=false
```

## Recursos Adicionales

- [Documentación de Arquitetura](ARCHITECTURE.md)
- [Análisis de Resultados](FINDINGS.md)
- [Referencias](REFERENCES.md)

---

**Última actualización:** Junio 2025
