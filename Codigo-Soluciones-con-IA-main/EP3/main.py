"""
EP3 - Observabilidad en Agentes de IA
Punto de entrada principal del sistema
"""

import logging
import yaml
import sys
from pathlib import Path
from datetime import datetime

from src.metrics.collector import MetricsCollector
from src.tracing.logger import StructuredLogger
from src.security.security_manager import SecurityManager
from src.utils.storage import StorageManager
from src.utils.analyzer import DataAnalyzer

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ObservabilitySystem:
    """Sistema principal de observabilidad"""
    
    def __init__(self, config_path: str = "config.yaml"):
        """Inicializar el sistema de observabilidad"""
        self.config_path = config_path
        self.config = self._load_config()
        
        # Inicializar componentes
        self.metrics_collector = MetricsCollector(self.config)
        self.logger = StructuredLogger(self.config)
        self.security_manager = SecurityManager(self.config)
        self.storage = StorageManager(self.config)
        self.analyzer = DataAnalyzer(self.config)
        
        logger.info("Sistema de observabilidad inicializado")
    
    def _load_config(self) -> dict:
        """Cargar configuración desde archivo YAML"""
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
            logger.info(f"Configuración cargada desde {self.config_path}")
            return config
        except FileNotFoundError:
            logger.error(f"Archivo de configuración no encontrado: {self.config_path}")
            sys.exit(1)
    
    def run(self):
        """Ejecutar el sistema completo"""
        logger.info("Iniciando ciclo de observabilidad")
        
        try:
            # 1. Recolectar métricas
            metrics = self.metrics_collector.collect()
            logger.info(f"Métricas recolectadas: {len(metrics)} items")
            
            # 2. Validar seguridad
            if self.config.get('security', {}).get('enabled', True):
                security_checks = self.security_manager.validate(metrics)
                logger.info(f"Validaciones de seguridad: {security_checks}")
            
            # 3. Almacenar datos
            self.storage.save_metrics(metrics)
            logger.info("Métricas almacenadas exitosamente")
            
            # 4. Analizar datos
            analysis_results = self.analyzer.analyze(metrics)
            logger.info(f"Análisis completado: {len(analysis_results)} anomalías detectadas")
            
            # 5. Generar recomendaciones
            recommendations = self.analyzer.generate_recommendations(analysis_results)
            logger.info(f"Recomendaciones generadas: {len(recommendations)} sugerencias")
            
            return {
                'status': 'success',
                'metrics': metrics,
                'analysis': analysis_results,
                'recommendations': recommendations,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error durante ejecución: {str(e)}", exc_info=True)
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def health_check(self) -> bool:
        """Verificar salud del sistema"""
        checks = {
            'metrics_collector': self.metrics_collector.is_healthy(),
            'logger': self.logger.is_healthy(),
            'security': self.security_manager.is_healthy(),
            'storage': self.storage.is_healthy(),
        }
        
        all_healthy = all(checks.values())
        logger.info(f"Health check: {checks}")
        
        return all_healthy


def main():
    """Función principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='EP3 - Sistema de Observabilidad de Agentes de IA'
    )
    parser.add_argument(
        '--config',
        type=str,
        default='config.yaml',
        help='Ruta del archivo de configuración'
    )
    parser.add_argument(
        '--health-check',
        action='store_true',
        help='Ejecutar solo verificación de salud'
    )
    
    args = parser.parse_args()
    
    # Crear sistema
    system = ObservabilitySystem(config_path=args.config)
    
    # Ejecutar health check si se solicita
    if args.health_check:
        is_healthy = system.health_check()
        sys.exit(0 if is_healthy else 1)
    
    # Ejecutar sistema completo
    result = system.run()
    
    if result['status'] == 'success':
        logger.info("Ciclo de observabilidad completado exitosamente")
        sys.exit(0)
    else:
        logger.error(f"Error en ciclo: {result.get('error')}")
        sys.exit(1)


if __name__ == '__main__':
    main()
