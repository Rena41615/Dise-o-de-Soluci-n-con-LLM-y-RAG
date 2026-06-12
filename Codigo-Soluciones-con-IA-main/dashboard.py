import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(page_title="Dashboard Metro IA", layout="wide")
st.title("🚇 Monitoreo y Observabilidad: Agente Metro de Santiago")

@st.cache_data
def load_data():
    try:
        with open("agent_logs.jsonl", "r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f]
        df = pd.DataFrame(data)
        if not df.empty:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except FileNotFoundError:
        return pd.DataFrame()
    except json.JSONDecodeError:
        return pd.DataFrame()


df = load_data()

if not df.empty:
    col1, col2, col3 = st.columns(3)
    tasa_exito = (len(df[df["evento"] == "Exito"]) / len(df)) * 100
    latencia_media = df["latencia_segundos"].mean()
    errores = len(df[df["evento"] == "Error"])

    col1.metric("Tasa de Éxito (Consistencia)", f"{tasa_exito:.1f}%")
    col2.metric("Latencia Promedio", f"{latencia_media:.2f} s")
    col3.metric("Frecuencia de Errores", f"{errores}")

    st.subheader("Uso de Recursos y Latencia")
    fig_lat = px.line(df, x='timestamp', y='latencia_segundos', title="Latencia por consulta (Segundos)")
    st.plotly_chart(fig_lat, use_container_width=True)

    fig_ram = px.area(df, x='timestamp', y='ram_porcentaje', title="Uso de RAM (%)")
    st.plotly_chart(fig_ram, use_container_width=True)

    st.subheader("Registros de Ejecución")
    st.dataframe(df.sort_values(by='timestamp', ascending=False).reset_index(drop=True))
else:
    st.warning("No hay datos de ejecución. Ejecuta el agente primero para generar logs.")
