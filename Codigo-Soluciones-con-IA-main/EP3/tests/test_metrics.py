"""
Pruebas del módulo de métricas
"""

import pytest
from src.metrics.collector import MetricsCollector, Metric


def test_metric_creation():
    """Prueba de creación de métrica"""
    metric = Metric(name='test', value=0.95, unit='%')
    
    assert metric.name == 'test'
    assert metric.value == 0.95
    assert metric.unit == '%'
    assert metric.timestamp is not None


def test_metric_to_dict():
    """Prueba de conversión métrica a diccionario"""
    metric = Metric(name='test', value=0.95, unit='%', tags={'agent': 'test'})
    metric_dict = metric.to_dict()
    
    assert metric_dict['name'] == 'test'
    assert metric_dict['value'] == 0.95
    assert metric_dict['unit'] == '%'
    assert metric_dict['tags']['agent'] == 'test'


def test_metrics_collector_initialization():
    """Prueba de inicialización del colector"""
    config = {'metrics': {'enabled': True}}
    collector = MetricsCollector(config)
    
    assert collector is not None
    assert len(collector.collectors) == 5


def test_metrics_collector_collect():
    """Prueba de recolección de métricas"""
    config = {'metrics': {'precision': {'enabled': True}}}
    collector = MetricsCollector(config)
    
    metrics = collector.collect()
    
    assert isinstance(metrics, list)
    assert len(metrics) > 0


def test_metrics_collector_health():
    """Prueba de salud del colector"""
    config = {'metrics': {'enabled': True}}
    collector = MetricsCollector(config)
    
    assert collector.is_healthy() is True
