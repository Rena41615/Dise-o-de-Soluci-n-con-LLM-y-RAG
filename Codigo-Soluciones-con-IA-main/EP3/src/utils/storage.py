"""
Módulo de Utilidades - Gestor de almacenamiento
"""

import json
import logging
import os
from typing import Dict, List, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class StorageManager:
    """Gestor de almacenamiento de datos de observabilidad"""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.metrics_path = self.config.get('storage', {}).get('metrics_path', 'results/metrics_report.json')
        self.logs_path = self.config.get('storage', {}).get('logs_path', 'results/logs/')
        self.viz_path = self.config.get('storage', {}).get('visualizations_path', 'results/visualizations/')
        
        self._ensure_directories()
        logger.info("StorageManager inicializado")
    
    def _ensure_directories(self):
        """Asegurar que los directorios existen"""
        for path in [self.metrics_path, self.logs_path, self.viz_path]:
            dir_path = os.path.dirname(path) if '.' in os.path.basename(path) else path
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)
    
    def save_metrics(self, metrics: List[Dict]) -> bool:
        """Guardar métricas en archivo JSON"""
        try:
            # Añadir timestamp
            report = {
                'timestamp': datetime.now().isoformat(),
                'metrics': metrics,
                'count': len(metrics)
            }
            
            with open(self.metrics_path, 'w') as f:
                json.dump(report, f, indent=2)
            
            logger.info(f"Métricas guardadas en {self.metrics_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error guardando métricas: {str(e)}")
            return False
    
    def load_metrics(self) -> List[Dict]:
        """Cargar métricas desde archivo"""
        try:
            with open(self.metrics_path, 'r') as f:
                report = json.load(f)
            
            logger.info(f"Métricas cargadas desde {self.metrics_path}")
            return report.get('metrics', [])
            
        except Exception as e:
            logger.error(f"Error cargando métricas: {str(e)}")
            return []
    
    def save_analysis_results(self, results: Dict) -> bool:
        """Guardar resultados de análisis"""
        try:
            filename = f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            filepath = os.path.join(self.viz_path, filename)
            
            with open(filepath, 'w') as f:
                json.dump(results, f, indent=2)
            
            logger.info(f"Resultados de análisis guardados en {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Error guardando análisis: {str(e)}")
            return False
    
    def save_visualization(self, viz_name: str, content: str) -> bool:
        """Guardar visualización (HTML, PNG, etc.)"""
        try:
            filepath = os.path.join(self.viz_path, viz_name)
            
            with open(filepath, 'w') as f:
                f.write(content)
            
            logger.info(f"Visualización guardada en {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Error guardando visualización: {str(e)}")
            return False
    
    def is_healthy(self) -> bool:
        """Verificar salud del almacenamiento"""
        try:
            # Intentar crear un archivo de prueba en cada directorio
            test_file = os.path.join(self.logs_path, '.health_check')
            with open(test_file, 'w') as f:
                f.write("health_check")
            os.remove(test_file)
            
            return True
        except Exception as e:
            logger.error(f"Storage health check failed: {str(e)}")
            return False
