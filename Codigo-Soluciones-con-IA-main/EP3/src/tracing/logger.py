"""
Módulo de Trazabilidad - Logger estructurado
"""

import logging
import json
from datetime import datetime
from typing import Dict, Any
import sys

logger = logging.getLogger(__name__)


class StructuredLogger:
    """Logger estructurado para trazabilidad"""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.enabled = self.config.get('tracing', {}).get('enabled', True)
        self.log_level = self.config.get('tracing', {}).get('log_level', 'INFO')
        self.log_format = self.config.get('tracing', {}).get('log_format', 'json')
        self.log_file = self.config.get('tracing', {}).get('log_file', 'results/logs/execution.log')
        
        self._setup_logging()
        logger.info("StructuredLogger inicializado")
    
    def _setup_logging(self):
        """Configurar el sistema de logging"""
        # Crear archivo de log si no existe
        import os
        os.makedirs(os.path.dirname(self.log_file) or '.', exist_ok=True)
        
        # Configurar handler para archivo
        handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter(
            '%(message)s' if self.log_format == 'json' else 
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        root_logger = logging.getLogger()
        root_logger.addHandler(handler)
        root_logger.setLevel(getattr(logging, self.log_level))
    
    def log_event(self, event_type: str, message: str, 
                  component: str = "", severity: str = "INFO", 
                  context: Dict = None):
        """Registrar evento estructurado"""
        if not self.enabled:
            return
        
        event = {
            'timestamp': datetime.now().isoformat(),
            'type': event_type,
            'component': component,
            'message': message,
            'severity': severity,
            'context': context or {}
        }
        
        log_message = json.dumps(event) if self.log_format == 'json' else str(event)
        
        level = getattr(logging, severity, logging.INFO)
        logger.log(level, log_message)
    
    def log_request(self, request_id: str, request_data: Dict):
        """Registrar solicitud"""
        self.log_event(
            event_type='request',
            message=f"Solicitud recibida: {request_id}",
            component='agent.request',
            context={'request_id': request_id, 'data': request_data}
        )
    
    def log_response(self, request_id: str, response_data: Dict, duration_ms: float):
        """Registrar respuesta"""
        self.log_event(
            event_type='response',
            message=f"Respuesta generada: {request_id}",
            component='agent.response',
            context={
                'request_id': request_id,
                'data': response_data,
                'duration_ms': duration_ms
            }
        )
    
    def log_error(self, error_msg: str, component: str, 
                  error_type: str = "", stack_trace: str = ""):
        """Registrar error"""
        self.log_event(
            event_type='error',
            message=error_msg,
            component=component,
            severity='ERROR',
            context={
                'error_type': error_type,
                'stack_trace': stack_trace
            }
        )
    
    def log_metric(self, metric_name: str, value: float, unit: str = ""):
        """Registrar métrica"""
        self.log_event(
            event_type='metric',
            message=f"Métrica: {metric_name}",
            component='metrics.collector',
            context={
                'metric_name': metric_name,
                'value': value,
                'unit': unit
            }
        )
    
    def is_healthy(self) -> bool:
        """Verificar salud del logger"""
        try:
            # Intentar escribir un mensaje de prueba
            with open(self.log_file, 'a') as f:
                f.write("health_check\n")
            return True
        except Exception as e:
            logger.error(f"Logger health check failed: {str(e)}")
            return False
