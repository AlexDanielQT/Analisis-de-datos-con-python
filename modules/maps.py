import streamlit as st
import folium
from folium.plugins import MarkerCluster, HeatMap
from streamlit_folium import folium_static

def mostrar_mapas(df_establecimientos, df_mapeo):
    st.header("Mapas Relevantes")
    tabs = st.tabs(["Mapa de Ubicacion de los penales", "Mapa de Lugar de Procedencia"])
    
    with tabs[0]:
        st.subheader("Mapa de Ubicación de los penales")

        # Crear un objeto Map de Folium centrado en Perú
        mapa_establecimientos = folium.Map(location=[-9.19, -75.0152], zoom_start=6)

        # Crear un cluster de marcadores para los establecimientos penitenciarios
        marker_cluster_penitenciarios = MarkerCluster().add_to(mapa_establecimientos)

        # Iterar sobre los establecimientos penitenciarios y agregar marcadores al mapa
        for _, row in df_establecimientos.iterrows():
            folium.Marker(
                location=[row['y'], row['x']],  # Asumiendo que 'y' es latitud y 'x' es longitud
                popup=row['Establecimiento Penitenciario'],
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(marker_cluster_penitenciarios)

        # Mostrar el mapa
        folium.LayerControl().add_to(mapa_establecimientos)
        folium_static(mapa_establecimientos)
        
        

    with tabs[1]:
        
        st.subheader("Mapa de Lugar de Procedencia")

        # Filtrar y limpiar los datos de mapeo
        df_mapeo_clean = df_mapeo.dropna(subset=['Y', 'X'])

        # Crear un objeto Map de Folium centrado en el promedio de las coordenadas
        mapa_calor_penales = folium.Map(location=[df_mapeo_clean['Y'].mean(), df_mapeo_clean['X'].mean()], zoom_start=6)

        # Crear una lista de ubicaciones para el HeatMap
        heat_data = [[row['Y'], row['X']] for _, row in df_mapeo_clean.iterrows()]

        # Agregar el HeatMap al mapa
        HeatMap(heat_data).add_to(mapa_calor_penales)

        # Agregar una leyenda al mapa
        legend_html = '''
        <div style="position: fixed; 
                    bottom: 50px; left: 50px; width: 300px; height: 90px; 
                    background-color: white; z-index:9999; font-size:14px;
                    border:2px solid grey; padding: 10px;">
            <strong>Mapa de Calor de Delitos</strong><br>
            Colores indican la densidad de los delitos<br>
        </div>
        '''
        mapa_calor_penales.get_root().html.add_child(folium.Element(legend_html))

        # Renderizar el mapa en Streamlit
        folium_static(mapa_calor_penales)
        