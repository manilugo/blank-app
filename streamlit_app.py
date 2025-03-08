import streamlit as st
import pandas as pd
import numpy as np

# Configurar la página
st.set_page_config(page_title="Calculadora de ROI - Agente con IA", page_icon="🤖", layout="wide")

st.title("📊 Calculadora de ROI - Agente con IA")
st.write("Descubre cómo incrementar tus ventas y optimizar procesos con Agente con IA.")

# Sidebar con parámetros de negocio
st.sidebar.header("Parámetros de tu Negocio")

num_leads = st.sidebar.slider("Número de Leads al Mes", 50, 50000, 1000)
tasa_cierre = st.sidebar.slider("Tasa de Cierre Actual (%)", 1, 50, 10)
valor_venta = st.sidebar.number_input("Valor Promedio de Cada Venta (USD)", min_value=1.0, value=500.0)
costo_agente_ia = 1000  # Costo fijo del Agente con IA en pesos mexicanos
costo_empleado = st.sidebar.number_input("Costo Mensual de un Empleado (USD)", min_value=0.0, value=500.0)
empleados_prospeccion = st.sidebar.slider("Empleados dedicados a Prospección (sin Agente con IA)", 0, 20, 2)

# Parámetros adicionales
st.sidebar.header("Escenario con Agente con IA")
mantener_empleados = st.sidebar.checkbox("Mantener el mismo número de empleados", value=True)
meses_analisis = st.sidebar.slider("Meses de Análisis", 1, 36, 3)

# Paquetes de implementación
st.sidebar.header("Paquetes de Implementación")
paquete = st.sidebar.selectbox("Selecciona el Nivel", ["Básica", "Avanzada", "Pro"])
incremento_cierre = st.sidebar.slider("Incremento en Tasa de Cierre (%)", 0.0, 5.0, 1.0)

# Cálculos
conversiones = (num_leads * tasa_cierre) / 100
ingresos_sin_ia = conversiones * valor_venta
incremento_conversiones = conversiones * (1 + incremento_cierre / 100)
ingresos_con_ia = incremento_conversiones * valor_venta
utilidad_adicional = ingresos_con_ia - ingresos_sin_ia - costo_agente_ia

# Cálculo del ROI a 3 meses y punto de equilibrio
roi_3_meses = ((utilidad_adicional * meses_analisis) / costo_agente_ia) * 100 if costo_agente_ia > 0 else 0
punto_equilibrio = costo_agente_ia / utilidad_adicional if utilidad_adicional > 0 else 0

# Mostrar métricas
st.subheader("Resumen Ejecutivo")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Ingresos Mensuales SIN Agente con IA", value=f"${ingresos_sin_ia:,.0f}")
with col2:
    st.metric(label="Ingresos Mensuales CON Agente con IA", value=f"${ingresos_con_ia:,.0f}")
with col3:
    st.metric(label="Utilidad Adicional Mensual", value=f"${utilidad_adicional:,.0f}")

# Crear DataFrame para gráficas
datos = pd.DataFrame({
    "Escenario": ["SIN Agente con IA", "CON Agente con IA"],
    "Utilidad (USD)": [ingresos_sin_ia, ingresos_con_ia],
})

# Mostrar gráfica
st.subheader("Utilidad Mensual: Con vs. Sin Agente con IA")
st.bar_chart(datos.set_index("Escenario"))

# Mostrar ROI y punto de equilibrio
st.subheader("Análisis Financiero")
col4, col5 = st.columns(2)
with col4:
    st.metric(label="ROI a 3 meses", value=f"{roi_3_meses:.0f}%")
with col5:
    st.metric(label="Punto de Equilibrio", value=f"{punto_equilibrio:.1f} meses")

st.write("🚀 Modifica los parámetros en la barra lateral y observa los cambios en tiempo real.")
