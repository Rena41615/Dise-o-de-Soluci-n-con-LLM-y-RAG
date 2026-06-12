"""
Dashboard de Monitoreo - EP3 Observabilidad
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
import os

st.set_page_config(
    page_title="EP3 - Dashboard de Observabilidad",
    page_icon="📊",
    layout="wide"
)

# Estilos CSS
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .header-title {
        color: #1f77b4;
        font-size: 32px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="header-title">📊 Dashboard de Observabilidad - EP3</div>', 
            unsafe_allow_html=True)
st.markdown("Sistema de monitoreo para Agentes de IA - Evaluación Parcial 3")

# Cargar datos simulados
def load_mock_data():
    """Cargar datos de prueba"""
    data = {
        'timestamp': pd.date_range(start='2025-05-30', end='2025-06-06', freq='1H'),
        'precision': [0.94 + (i % 7) * 0.01 for i in range(169)],
        'latency': [342 + (i % 24) * 20 for i in range(169)],
        'error_rate': [2.05 - (i % 7) * 0.1 for i in range(169)],
        'cpu_usage': [35.2 + (i % 12) * 3 for i in range(169)],
        'memory_usage': [512 + (i % 6) * 50 for i in range(169)]
    }
    return pd.DataFrame(data)

df = load_mock_data()

# Sidebar - Filtros
with st.sidebar:
    st.header("Filtros")
    
    date_range = st.date_input(
        "Rango de fechas",
        value=(datetime(2025, 5, 30), datetime(2025, 6, 6)),
        key="date_range"
    )
    
    metric_filter = st.multiselect(
        "Métricas a mostrar",
        ['Precision', 'Latencia', 'Tasa de Errores', 'CPU', 'Memoria'],
        default=['Precision', 'Latencia', 'Tasa de Errores']
    )
    
    st.divider()
    
    if st.button("🔄 Actualizar Datos"):
        st.rerun()
    
    st.divider()
    
    st.subheader("Información del Sistema")
    st.info("**Estado:** ✓ Operativo")
    st.success("**Último ciclo:** Hace 2 minutos")
    st.warning("**Alertas activas:** 1")

# KPIs principales
col1, col2, col3, col4 = st.columns(4)

with col1:
    precision_avg = df['precision'].mean()
    st.metric(
        "Precisión",
        f"{precision_avg:.1%}",
        delta=f"+{(precision_avg - 0.93) * 100:.1f}%",
        delta_color="normal"
    )

with col2:
    latency_avg = df['latency'].mean()
    st.metric(
        "Latencia Promedio",
        f"{latency_avg:.0f}ms",
        delta=f"{(latency_avg - 320):.0f}ms",
        delta_color="inverse"
    )

with col3:
    error_avg = df['error_rate'].mean()
    st.metric(
        "Tasa de Errores",
        f"{error_avg:.2f}%",
        delta=f"-{(2.05 - error_avg):.2f}%",
        delta_color="normal"
    )

with col4:
    uptime = 99.8
    st.metric(
        "Disponibilidad",
        f"{uptime:.1f}%",
        delta="No cambios",
        delta_color="normal"
    )

st.divider()

# Gráficos principales
col1, col2 = st.columns(2)

with col1:
    st.subheader("Tendencia de Precisión")
    fig_precision = go.Figure()
    fig_precision.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['precision'] * 100,
        mode='lines+markers',
        name='Precisión (%)',
        line=dict(color='#1f77b4', width=2),
        fill='tozeroy'
    ))
    fig_precision.update_layout(
        xaxis_title="Tiempo",
        yaxis_title="Precisión (%)",
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig_precision, use_container_width=True)

with col2:
    st.subheader("Latencia en Tiempo Real")
    fig_latency = go.Figure()
    fig_latency.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['latency'],
        mode='lines',
        name='Latencia (ms)',
        line=dict(color='#ff7f0e', width=2),
        fill='tozeroy'
    ))
    fig_latency.add_hline(
        y=5000,
        line_dash="dash",
        line_color="red",
        annotation_text="Umbral crítico"
    )
    fig_latency.update_layout(
        xaxis_title="Tiempo",
        yaxis_title="Latencia (ms)",
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig_latency, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribución de Errores por Tipo")
    error_types = {
        'Timeouts': 45.3,
        'Input Inválido': 28.1,
        'Servicio Indisponible': 15.4,
        'Logic Error': 11.2
    }
    fig_errors = px.pie(
        values=list(error_types.values()),
        names=list(error_types.keys()),
        title="Distribución de Errores (%)"
    )
    st.plotly_chart(fig_errors, use_container_width=True)

with col2:
    st.subheader("Uso de Recursos")
    fig_resources = go.Figure()
    fig_resources.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['cpu_usage'],
        mode='lines',
        name='CPU (%)',
        line=dict(color='#2ca02c')
    ))
    fig_resources.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['memory_usage'] / 1024 * 100,
        mode='lines',
        name='Memoria (%)',
        line=dict(color='#d62728')
    ))
    fig_resources.update_layout(
        xaxis_title="Tiempo",
        yaxis_title="Porcentaje (%)",
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig_resources, use_container_width=True)

st.divider()

# Análisis de Anomalías
st.subheader("⚠️ Anomalías Detectadas")

anomalies = [
    {
        'timestamp': '2025-06-03 14:32',
        'metric': 'Error Rate',
        'value': '23.4%',
        'severity': 'HIGH',
        'cause': 'Mantenimiento de API externa'
    },
    {
        'timestamp': '2025-06-05 08:15',
        'metric': 'Memory Usage',
        'value': '1,180 MB',
        'severity': 'MEDIUM',
        'cause': 'Memory leak en sesión larga'
    }
]

for anomaly in anomalies:
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.caption(anomaly['timestamp'])
    with col2:
        st.caption(f"**{anomaly['metric']}**")
    with col3:
        st.caption(anomaly['value'])
    with col4:
        if anomaly['severity'] == 'HIGH':
            st.warning(anomaly['severity'])
        else:
            st.info(anomaly['severity'])
    with col5:
        st.caption(anomaly['cause'])

st.divider()

# Recomendaciones
st.subheader("💡 Recomendaciones de Optimización")

recommendations = [
    {
        'title': 'R1. Optimizar Queries de Base de Datos',
        'priority': 'ALTA',
        'impact': '+40-60% latencia, 80% menos timeouts',
        'timeline': '1-2 semanas'
    },
    {
        'title': 'R2. Implementar Rate Limiting',
        'priority': 'ALTA',
        'impact': 'Estabilizar latencia en hora pico',
        'timeline': '1-2 semanas'
    },
    {
        'title': 'R3. Corregir Validador de Entrada',
        'priority': 'MEDIA',
        'impact': 'Reducir errores 28% → 8%',
        'timeline': '2-4 semanas'
    }
]

for idx, rec in enumerate(recommendations, 1):
    with st.expander(f"{rec['title']} - {rec['priority']}", expanded=(idx==1)):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Prioridad", rec['priority'])
        with col2:
            st.metric("Impacto", rec['impact'][:20] + "...")
        with col3:
            st.metric("Timeline", rec['timeline'])

st.divider()

# Footer
st.markdown("""
---
**EP3 - Evaluación Parcial 3** | Ingeniería de Soluciones con IA (ISY0101)

*Dashboard de Observabilidad - Última actualización: 2025-06-06 15:32 UTC*
""")
