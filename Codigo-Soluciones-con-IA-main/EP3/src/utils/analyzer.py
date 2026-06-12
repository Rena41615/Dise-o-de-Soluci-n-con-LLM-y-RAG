"""
Módulo de Análisis - Analizador de datos
"""

import logging
import json
from typing import Dict, List, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class DataAnalyzer:
    """Analizador de datos de observabilidad"""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.enabled = self.config.get('analysis', {}).get('enabled', True)
        
        logger.info("DataAnalyzer inicializado")
    
    def analyze(self, metrics: List[Dict]) -> Dict[str, Any]:
        """Realizar análisis de métricas"""
        if not self.enabled or not metrics:
            return {'status': 'disabled', 'anomalies': []}
        
        try:
            analysis_results = {
                'timestamp': datetime.now().isoformat(),
                'total_metrics': len(metrics),
                'anomalies': self._detect_anomalies(metrics),
                'trends': self._analyze_trends(metrics),
                'alerts': self._generate_alerts(metrics)
            }
            
            logger.info(f"Análisis completado: {len(analysis_results['anomalies'])} anomalías detectadas")
            return analysis_results
            
        except Exception as e:
            logger.error(f"Error durante análisis: {str(e)}")
            return {'status': 'error', 'error': str(e)}
    
    def _detect_anomalies(self, metrics: List[Dict]) -> List[Dict]:
        """Detectar anomalías en métricas"""
        anomalies = []
        
        # Simular detección de anomalías
        thresholds = {
            'precision': {'min': 0.85, 'max': 1.0},
            'latency': {'min': 0, 'max': 5000},
            'error_rate': {'min': 0, 'max': 5.0},
            'cpu_usage': {'min': 0, 'max': 80},
            'memory_usage': {'min': 0, 'max': 80}
        }
        
        for metric in metrics:
            metric_name = metric.get('name')
            metric_value = metric.get('value')
            
            if metric_name in thresholds:
                threshold = thresholds[metric_name]
                
                if metric_value < threshold['min'] or metric_value > threshold['max']:
                    anomalies.append({
                        'metric_name': metric_name,
                        'value': metric_value,
                        'threshold': threshold,
                        'severity': self._calculate_severity(metric_value, threshold),
                        'timestamp': metric.get('timestamp')
                    })
        
        return anomalies
    
    def _calculate_severity(self, value: float, threshold: Dict) -> str:
        """Calcular severidad de anomalía"""
        if value > threshold['max']:
            excess = (value - threshold['max']) / threshold['max']
            if excess > 0.5:
                return 'CRITICAL'
            elif excess > 0.2:
                return 'HIGH'
            else:
                return 'MEDIUM'
        elif value < threshold['min']:
            return 'LOW'
        return 'INFO'
    
    def _analyze_trends(self, metrics: List[Dict]) -> Dict:
        """Analizar tendencias en métricas"""
        trends = {
            'overall_trend': 'stable',
            'improving_metrics': [],
            'degrading_metrics': [],
            'analysis_window': '7_days'
        }
        
        # Simulación de análisis de tendencias
        if metrics:
            # En producción, analizar histórico de datos
            trends['improving_metrics'] = ['precision', 'consistency']
            trends['degrading_metrics'] = ['latency']
        
        return trends
    
    def _generate_alerts(self, metrics: List[Dict]) -> List[Dict]:
        """Generar alertas basadas en métricas"""
        alerts = []
        
        # Simular generación de alertas
        alert_thresholds = {
            'error_rate': {'threshold': 5.0, 'message': 'Tasa de error elevada'},
            'latency': {'threshold': 2000, 'message': 'Latencia excesiva'},
            'cpu_usage': {'threshold': 85, 'message': 'Uso de CPU crítico'}
        }
        
        for metric in metrics:
            metric_name = metric.get('name')
            metric_value = metric.get('value')
            
            if metric_name in alert_thresholds:
                if metric_value > alert_thresholds[metric_name]['threshold']:
                    alerts.append({
                        'metric': metric_name,
                        'value': metric_value,
                        'threshold': alert_thresholds[metric_name]['threshold'],
                        'message': alert_thresholds[metric_name]['message'],
                        'timestamp': datetime.now().isoformat()
                    })
        
        return alerts
    
    def generate_recommendations(self, analysis_results: Dict) -> List[Dict]:
        """Generar recomendaciones basadas en análisis"""
        recommendations = []
        
        anomalies = analysis_results.get('anomalies', [])
        
        for anomaly in anomalies:
            metric_name = anomaly.get('metric_name')
            severity = anomaly.get('severity')
            
            if severity in ['CRITICAL', 'HIGH']:
                recommendation = self._generate_recommendation(metric_name, severity)
                if recommendation:
                    recommendations.append(recommendation)
        
        logger.info(f"Se generaron {len(recommendations)} recomendaciones")
        return recommendations
    
    def _generate_recommendation(self, metric_name: str, severity: str) -> Dict:
        """Generar recomendación específica para métrica"""
        recommendations_map = {
            'precision': {
                'CRITICAL': 'Revisar algoritmo del agente. Precisión crítica.',
                'HIGH': 'Optimizar entrenamiento del modelo.'
            },
            'latency': {
                'CRITICAL': 'Optimizar queries de BD. Considerar caché.',
                'HIGH': 'Aumentar recursos de procesamiento.'
            },
            'error_rate': {
                'CRITICAL': 'Investigar causa raíz. Implementar fallbacks.',
                'HIGH': 'Mejorar validación de entrada.'
            },
            'cpu_usage': {
                'CRITICAL': 'Auto-scaling requerido. Optimizar código.',
                'HIGH': 'Monitorear patrones de uso.'
            },
            'memory_usage': {
                'CRITICAL': 'Memory leak detectado. Revisar código.',
                'HIGH': 'Considerar compresión de datos.'
            }
        }
        
        if metric_name in recommendations_map:
            message = recommendations_map[metric_name].get(severity, '')
            
            return {
                'metric': metric_name,
                'severity': severity,
                'recommendation': message,
                'priority': 'immediate' if severity == 'CRITICAL' else 'urgent',
                'confidence': 0.85
            }
        
        return None
