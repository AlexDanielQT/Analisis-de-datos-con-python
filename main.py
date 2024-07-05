import streamlit as st
from modules.data_loader import load_data
from modules.filters import filter_data
from modules.views import mostrar_sidebar, mostrar_datos_rapidos, mostrar_resultados, generar_descarga_csv
from modules.downloads import generar_descarga_csv  # Importar la función desde downloads.py

def main():
    # Cargar los datos
    df_origin, df_mapeo, df_establecimientos = load_data()

    # Mostrar barra lateral y obtener opciones seleccionadas
    opcion_principal, departamento, provincia, distrito = mostrar_sidebar(df_origin)

    # Aplicar filtros y obtener datos filtrados
    df_filtered = filter_data(df_origin, departamento, provincia, distrito)

    # Mostrar datos rápidos (cabecera)
    mostrar_datos_rapidos(df_filtered)

    # Mostrar resultados según la opción principal seleccionada
    mostrar_resultados(opcion_principal, df_filtered, df_establecimientos, df_mapeo)

    # Configuración del archivo a descargar
    generar_descarga_csv(df_filtered)

if __name__ == '__main__':
    main()
