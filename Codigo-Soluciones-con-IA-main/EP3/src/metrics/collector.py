"""
Módulo de Métricas - Collector principal
"""

import logging
import time
import psutil
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List, Any

logger = logging.getLogger(__name__)


class Metric:
    """Clase base para representar una métrica"""
    
    def __init__(self, name: str, value: float, unit: str = "", tags: Dict = None):
        self.name = name
        self.value = value
        self.unit = unit
        self.tags = tags or {}
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'value': self.value,
            'unit': self.unit,
            'tags': self.tags,
            'timestamp': self.timestamp
        }


class MetricCollector(ABC):
    """Clase abstracta para colectores de métricas"""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.enabled = self.config.get('enabled', True)
    
    @abstractmethod
    def collect(self) -> Metric:
        """Recolectar métrica específica"""
        pass
    
    def is_healthy(self) -> bool:
        """Verificar salud del colector"""
        return self.enabled


class PrecisionCollector(MetricCollector):
    """Colector de métrica de precisión"""
    
    def collect(self) -> Metric:
        # Implementación simulada
        # En producción, conectar con el agente real
        precision_value = 0.94
        return Metric(
            name='precision',
            value=precision_value,
            unit='%',
            tags={'agent': 'metro', 'version': '1.0'}
        )


class LatencyCollector(MetricCollector):
    """Colector de métrica de latencia"""
    
    def collect(self) -> Metric:
        # Implementación simulada
        latency_ms = 342
        return Metric(
            name='latency',
            value=latency_ms,
            unit='ms',
            tags={'agent': 'metro', 'p50': 245, 'p95': 1240}
        )


class ConsistencyCollector(MetricCollector):
    """Colector de métrica de consistencia"""
    
    def collect(self) -> Metric:
        # Implementación simulada
        consistency_value = 0.96
        return Metric(
            name='consistency',
            value=consistency_value,
            unit='%',
            tags={'agent': 'metro'}
        )


class ErrorRateCollector(MetricCollector):
    """Colector de tasa de errores"""
    
    def collect(self) -> Metric:
        # Implementación simulada
        error_rate = 2.05
        return Metric(
            name='error_rate',
            value=error_rate,
            unit='%',
            tags={'agent': 'metro', 'period': '24h'}
        )


class ResourceUsageCollector(MetricCollector):
    """Colector de uso de recursos (CPU, Memoria)"""
    
    def collect(self) -> List[Metric]:
        metrics = []
        
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=0.1)
        metrics.append(Metric(
            name='cpu_usage',
            value=cpu_percent,
            unit='%',
            tags={'type': 'system'}
        ))
        
        # Memory usage
        memory_info = psutil.virtual_memory()
        metrics.append(Metric(
            name='memory_usage',
            value=memory_info.percent,
            unit='%',
            tags={'type': 'system'}
        ))
        
        # Disk usage
        disk_info = psutil.disk_usage('/')
        metrics.append(Metric(
            name='disk_usage',
            value=disk_info.percent,
            unit='%',
            tags={'type': 'system'}
        ))
        
        return metrics


class MetricsCollector:
    """Colector principal que orquesta todos los colectores"""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.collectors = self._initialize_collectors()
        logger.info("MetricsCollector inicializado")
    
    def _initialize_collectors(self) -> List[MetricCollector]:
        """Inicializar todos los colectores de métricas"""
        collectors = [
            PrecisionCollector(self.config.get('metrics', {}).get('precision', {})),
            LatencyCollector(self.config.get('metrics', {}).get('latency', {})),
            ConsistencyCollector(self.config.get('metrics', {}).get('consistency', {})),
            ErrorRateCollector(self.config.get('metrics', {}).get('error_frequency', {})),
            ResourceUsageCollector(self.config.get('metrics', {}).get('resource_usage', {})),
        ]
        return collectors
    
    def collect(self) -> List[Dict]:
        """Recolectar todas las métricas"""
        all_metrics = []
        
        for collector in self.collectors:
            try:
                result = collector.collect()
                
                # Manejar collectors que retornan listas
                if isinstance(result, list):
                    all_metrics.extend([m.to_dict() for m in result])
                else:
                    all_metrics.append(result.to_dict())
                    
            except Exception as e:
                logger.error(f"Error colectando {collector.__class__.__name__}: {str(e)}")
        
        logger.info(f"Total de {len(all_metrics)} métricas recolectadas")
        return all_metrics
    
    def is_healthy(self) -> bool:
        """Verificar salud de todos los colectores"""
        return all(c.is_healthy() for c in self.collectors)
