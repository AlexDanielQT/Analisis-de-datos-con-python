import streamlit as st

def generar_descarga_csv(df_filtered):
    csv = df_filtered.to_csv(index=False)
    st.download_button(
        label="Descargar datos filtrados como CSV",
        data=csv,
        file_name='datos_filtrados.csv',
        mime='text/csv',
    )
