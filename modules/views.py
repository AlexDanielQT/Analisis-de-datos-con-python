import streamlit as st
from modules.charts import create_charts
from modules.maps import mostrar_mapas
from modules.downloads import generar_descarga_csv

def mostrar_sidebar(df_origin):
    st.sidebar.title("Navegación")
    opcion_principal = st.sidebar.selectbox("Selecciona un aspecto principal", ["Aspectos Demográficos", "Aspectos Sociales", "Aspectos Penitenciarios", "Aspectos Delictivos", "Mapas"])

    # Filtros para departamentos, provincias y distritos
    departamento = st.sidebar.multiselect('Departamentos', sorted(df_origin['DD'].dropna().unique()))

    if departamento:
        provincias_disponibles = df_origin[df_origin['DD'].isin(departamento)]['PP'].dropna().unique()
        provincia = st.sidebar.multiselect('Provincias', sorted(provincias_disponibles))
    else:
        provincia = []

    if provincia:
        distritos_disponibles = df_origin[df_origin['PP'].isin(provincia)]['DI'].dropna().unique()
        distrito = st.sidebar.multiselect('Distritos', sorted(distritos_disponibles))
    else:
        distrito = []

    return opcion_principal, departamento, provincia, distrito


def mostrar_datos_rapidos(df_filtered):
    st.header("Reclusos en Perú - 2016")
    st.subheader("Datos Rápidos")

    # Métricas de interés
    total_internos = len(df_filtered)
    delito_comun = df_filtered['DELITO_GENERICO'].mode()[0] if not df_filtered['DELITO_GENERICO'].mode().empty else 'N/A'
    edad_media = df_filtered['EDAD'].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Internos", f"{total_internos:,}")
    col2.metric("Edad Media", f"{edad_media:.1f}")
    col3.metric("Delito Más Común", delito_comun)

def mostrar_resultados(opcion_principal, df_filtered, df_establecimientos, df_mapeo):
    charts = create_charts(df_filtered)

    if opcion_principal == "Aspectos Demográficos":
        mostrar_aspecto1(df_filtered, charts)
    elif opcion_principal == "Aspectos Sociales":
        mostrar_aspecto2(df_filtered, charts)
    elif opcion_principal == "Aspectos Penitenciarios":
        mostrar_aspecto3(df_filtered, charts)
    elif opcion_principal == "Aspectos Delictivos":
        mostrar_aspecto4(df_filtered, charts)
    elif opcion_principal == "Mapas":
        mostrar_mapas(df_establecimientos, df_mapeo)
        


def mostrar_aspecto1(df_filtered, charts):
    st.header("Aspectos Demograficos")
    tabs = st.tabs(["Datos Personales", "Lugar de Nacimiento", "Identidad y Pertenencia"])

    with tabs[0]:  # Pestaña "Datos Personales"
        st.plotly_chart(charts['Genero'])
        st.plotly_chart(charts['Edad'])
        st.plotly_chart(charts['Religion'])
        st.plotly_chart(charts['Nacionalidad'])
        st.plotly_chart(charts['hijos-hijas'])
    

    with tabs[1]:  # Pestaña "Lugar de Nacimiento"
        st.plotly_chart(charts['Pais de Nacimiento'])
        st.plotly_chart(charts['Departamento de Nacimiento'])

    with tabs[2]:  # Pestaña "Identidad y Pertenencia"
        st.plotly_chart(charts['Idioma'])
        st.plotly_chart(charts['Ancestrales'])
    
# Funciones para otros aspectos similares

def mostrar_aspecto2(df_filtered, charts):
    st.header("Aspectos Sociales")
    tabs = st.tabs(["Relaciones y Conductas", "Condiciones Familiares y de crianza", "Experiencias de vida y entorno social"])

    with tabs[0]:  # Pestaña "Relaciones y Conductas"
        st.plotly_chart(charts['leerescribirhablar'])
        st.plotly_chart(charts['Estudios'])
        st.plotly_chart(charts['Consumo de sustancias'])
        st.plotly_chart(charts['Razon_no_estudiar'])
        st.plotly_chart(charts['Sexualidad'])


    with tabs[1]:  # Pestaña "Condiciones Familiares y de crianza"
        st.plotly_chart(charts['Conviv_padres'])
        st.plotly_chart(charts['Maltrato Infantil por Padres o Figuras Parentales'])
        st.plotly_chart(charts['Padres-alcohol'])
        st.plotly_chart(charts['Padres-drogas'])

    with tabs[2]:  # Pestaña "Experiencias de vida y entorno social"
        st.plotly_chart(charts['Amigos-delitos'])
        st.plotly_chart(charts['Pandillas-barrio'])
        st.plotly_chart(charts['ExDiscriminación'])
    
# Funciones para otros aspectos similares
def mostrar_aspecto3(df_filtered, charts):
    
    st.header("Aspectos Penitenciario")
    charts = create_charts(df_filtered)
    tabs = st.tabs(["Condiciones de Vida", "Salud", "Actividades", "Discriminacion","Visitas"])
    
    with tabs[0]:  # Pestaña "Condiciones de Vida"
        st.plotly_chart(charts['Estado de Servicios Higiénicos'])
        
        st.plotly_chart(charts['Calidad de los alimentos'])
        
        st.plotly_chart(charts['Esta en programa de estudios'])
    
    with tabs[1]:  # Pestaña "Condiciones de Salud"
        st.plotly_chart(charts['Dolencia en el penitenciario'])
    
        st.plotly_chart(charts['Atencion en el Penitenciario'])      
        
        st.plotly_chart(charts['Razon por que no acudio al centro medico del establecimiento'])      
                    
    with tabs[2]:  # Pestaña "actividades"
        st.plotly_chart(charts['Actividad1'])  
        st.plotly_chart(charts['Actividad2'])    
        st.plotly_chart(charts['Actividad3'])    
        st.plotly_chart(charts['Actividad4'])    
        st.plotly_chart(charts['Actividad5'])             
        st.plotly_chart(charts['Actividad6'])               
        
    with tabs[3]:  # Pestaña "Discriminacion"
        st.plotly_chart(charts['Se siente discriminado'])   
        st.plotly_chart(charts['Razon de discriminacion'])              
        
                      

    with tabs[4]:  # Pestaña "visita"
        st.plotly_chart(charts['Visita1']) 
        st.plotly_chart(charts['Visita2']) 
        
                    
def mostrar_aspecto4(df_filtered, charts):
    st.header("Aspectos delictivos")
    charts = create_charts(df_filtered)
    tabs = st.tabs(["Delitos", "Demografía y Contexto", "Armas y Consumo", "Otros Aspectos"])

    with tabs[0]:  # Pestaña "Delitos"
        st.plotly_chart(charts['DelGen'])
        st.plotly_chart(charts['DelEsp'])
        st.plotly_chart(charts['DelGenero'])
        st.plotly_chart(charts['DelEspGen'])

    with tabs[1]:  # Pestaña "Demografía y Contexto"
        st.plotly_chart(charts['SitJuridica'])
        st.plotly_chart(charts['SitJuridicaEsp'])
        st.plotly_chart(charts['Lugar_Delito'])
        st.plotly_chart(charts['Motivo_Delito'])

    with tabs[2]:  # Pestaña "Armas y Consumo"
        st.plotly_chart(charts['UsoArma']) 
        st.plotly_chart(charts['ArmsFuegInic'])
        st.plotly_chart(charts['ConsumoDrogasDelito'])

    with tabs[3]:  # Pestaña "Otros Aspectos"

        st.plotly_chart(charts['Delitos-penal'])
        st.plotly_chart(charts['Internado-juvenil'])
        st.plotly_chart(charts['inocente-culpable'])
        
        