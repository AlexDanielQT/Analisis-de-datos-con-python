import plotly.express as px
import pandas as pd

def create_charts(df):
    charts = {}

# Aspectos Demográficos
    genero_counts = df['GENERO'].value_counts()
    fig_genero = px.pie(values=genero_counts.values, 
                        names=genero_counts.index, 
                        title='Número de Internos según el Género',
                        hole=0.3)  # Added hole to make it a donut chart
    charts['Genero'] = fig_genero

    fig_edad = px.histogram(df, 
                            x='EDAD', 
                            nbins=20,  # Reduced number of bins
                            title='Número de Internos según la Edad',
                            color_discrete_sequence=['indigo'])  # Changed color
    charts['Edad'] = fig_edad

    religion_counts = df['RELIGION'].value_counts()
    fig_religion = px.pie(values=religion_counts.values, 
                          names=religion_counts.index, 
                          title='Número de Internos según la Religión',
                          hole=0.3)  # Added hole to make it a donut chart
    charts['Religion'] = fig_religion

    nacionalidad_counts = df['NACIONALIDAD'].value_counts()
    fig_nacionalidad = px.bar(x=nacionalidad_counts.index, 
                              y=nacionalidad_counts.values, 
                              title='Número de Internos según la Nacionalidad',
                              labels={'x': 'Nacionalidad', 'y': 'Número de Internos'})
    charts['Nacionalidad'] = fig_nacionalidad
    
    
    pais_nac_counts = df['PAIS_NAC'].value_counts()
    fig_pais_nac = px.bar(x=pais_nac_counts.index, 
                          y=pais_nac_counts.values, 
                          title='País de nacimiento de los Internos',
                          labels={'x': 'País de Nacimiento', 'y': 'Número de Internos'})
    charts['Pais de Nacimiento'] = fig_pais_nac

    nac_dd_counts = df['NAC_DD'].value_counts()
    fig_nac_dd = px.bar(x=nac_dd_counts.index, 
                        y=nac_dd_counts.values, 
                        title='Departamento de nacimiento de los Internos',
                        labels={'x': 'Departamento de Nacimiento', 'y': 'Número de Internos'})
    charts['Departamento de Nacimiento'] = fig_nac_dd

    lista1 = [df['P103_1'], df['P103_2'], df['P103_3']]
    concatenated_series = pd.concat(lista1)
    saben_leer_ecribir_hablar = concatenated_series.value_counts()
    fig_declaracion = px.pie(values=saben_leer_ecribir_hablar.values, 
                             names=saben_leer_ecribir_hablar.index, 
                             title='Saben leer, escribir o hablar',
                             hole=0.3)  # Added hole to make it a donut chart
    charts['leerescribirhablar'] = fig_declaracion


    niv_estudios = df['P104_1'].value_counts()
    fig_estudios = px.bar(x=niv_estudios.index, 
                          y=niv_estudios.values, 
                          title='Nivel de Estudios',
                          labels={'x': 'Nivel de Estudios', 'y': 'Número de Internos'})
    charts['Estudios'] = fig_estudios

    p120_counts = df['P120'].value_counts()
    fig_p120 = px.pie(values=p120_counts.values, 
                      names=p120_counts.index, 
                      title='Identificación de los Internos',
                      hole=0.3)  # Added hole to make it a donut chart
    charts['Ancestrales'] = fig_p120

    # Aspectos Personales
    idioma_counts = df['P101'].value_counts()
    fig_idioma = px.bar(x=idioma_counts.index, 
                        y=idioma_counts.values, 
                        title='Idioma y Lengua Materna',
                        labels={'x': 'Idioma', 'y': 'Número de Internos'})
    charts['Idioma'] = fig_idioma

    idiomas_fluidos_counts = df['P102'].value_counts()
    fig_idiomas_fluidos = px.pie(values=idiomas_fluidos_counts.values, 
                                 names=idiomas_fluidos_counts.index, 
                                 title='Idiomas Fluidos',
                                 hole=0.3)  # Added hole to make it a donut chart
    charts['Idiomas Fluidos'] = fig_idiomas_fluidos
    
    
    
    lista2 = [df['P137A_HIJO'], df['P137A_HIJA']]
    concatenated_series = pd.concat(lista2)
    declaracion_counts = concatenated_series.value_counts()
    fig_declaracion = px.pie(values=declaracion_counts.values, 
                             names=declaracion_counts.index, 
                             title='Cantidad de Hijos e Hijas',
                             hole=0.3)  # Added hole to make it a donut chart
    charts['hijos-hijas'] = fig_declaracion

    # Relaciones y Conductas
    razon_counts = df['P105'].value_counts()
    fig_razon = px.bar(x=razon_counts.index, 
                       y=razon_counts.values, 
                       title='Razón principal por la que no estudió o por la cual no terminó de estudiar en el colegio',
                       labels={'x': 'Razón', 'y': 'Número de Internos'})
    charts['Razon_no_estudiar'] = fig_razon

    sexualidad_counts = df['P112'].value_counts()
    fig_sexualidad = px.bar(x=sexualidad_counts.index, 
                            y=sexualidad_counts.values, 
                            title='Sexualidad con la que se identifica',
                            labels={'x': 'Sexualidad', 'y': 'Número de Internos'})
    

    charts['Sexualidad'] = fig_sexualidad


    series_list2 = [df['P109_1'], df['P109_2'], df['P109_3']]
    concatenated_series = pd.concat(series_list2)
    consumo_sustancias = concatenated_series.value_counts()
    fig_consumo_sustancias = px.bar(x=consumo_sustancias.index, 
                                    y=consumo_sustancias.values, 
                                    title='Consumo de drogas, alcohol o cigarrillos',
                                    labels={'x': 'Sustancia', 'y': 'Número de Internos'})
    charts['Consumo de sustancias'] = fig_consumo_sustancias
        
    
    # Experiencias de vida y entorno social
    amigos_delitos_counts = df['P135'].value_counts()
    fig_amigos_delitos = px.bar(amigos_delitos_counts, 
                                x=amigos_delitos_counts.index, 
                                y=amigos_delitos_counts.values,
                                title='Se relacionó con amigos que Cometían Delitos antes de los 18 Años')
    charts['Amigos-delitos'] = fig_amigos_delitos

    pandillas_counts = df['P136'].value_counts()
    fig_pandillas = px.bar(pandillas_counts, 
                           x=pandillas_counts.index, 
                           y=pandillas_counts.values,
                           title='Hubo Presencia de Pandillas o Bandas Delictivas en el Barrio donde creció hasta los 18 años')
    charts['Pandillas-barrio'] = fig_pandillas

    discriminacion_counts = df['P139'].value_counts()
    fig_discriminacion = px.bar(x=discriminacion_counts.index, 
                                y=discriminacion_counts.values,
                                title='Tuvo alguna experiencia de Discriminación anteriormente',
                                labels={'x': 'Experiencia de Discriminación', 'y': 'Número de Internos'})
    charts['ExDiscriminación'] = fig_discriminacion

    # Condiciones Familiares y de crianza
    series_list3 = [df['P122'], df['P124']]
    concatenated_series = pd.concat(series_list3)
    vivio_padres = concatenated_series.value_counts()
    fig_vivio_padres = px.bar(x=vivio_padres.index, 
                              y=vivio_padres.values, 
                              title='Edad de convivencia con los padres',
                              labels={'x': 'Edad', 'y': 'Número de Internos'})
    charts['Conviv_padres'] = fig_vivio_padres

    pegaba_nino_counts = df['P126'].value_counts()
    fig_pegaba_nino = px.bar(x=pegaba_nino_counts.index, 
                             y=pegaba_nino_counts.values, 
                             title='Maltrato Infantil por Padres o Figuras Parentales',
                             labels={'x': 'Maltrato', 'y': 'Número de Internos'})
    charts['Maltrato Infantil por Padres o Figuras Parentales'] = fig_pegaba_nino

    consumo_alcohol_padres_counts = df['P127'].value_counts()
    fig_consumo_alcohol_padres = px.pie(values=consumo_alcohol_padres_counts.values, 
                                        names=consumo_alcohol_padres_counts.index, 
                                        title='Consumo de Alcohol por parte de Padres o Figuras Parentales',
                                        hole=0.3)  # Added hole to make it a donut chart
    charts['Padres-alcohol'] = fig_consumo_alcohol_padres

    consumo_drogas_padres_counts = df['P128'].value_counts()
    fig_consumo_drogas_padres = px.pie(values=consumo_drogas_padres_counts.values, 
                                        names=consumo_drogas_padres_counts.index, 
                                        title='Consumo de Drogas por parte de Padres o Figuras Parentales',
                                        hole=0.3)  # Added hole to make it a donut chart
    charts['Padres-drogas'] = fig_consumo_drogas_padres

    
    delito_generico_counts = df['DELITO_GENERICO'].value_counts()
    fig_delito_generico = px.bar(delito_generico_counts, 
                                 x=delito_generico_counts.index, 
                                 y=delito_generico_counts.values, 
                                 title='Delitos Genéricos Cometidos')
    charts['DelGen'] = fig_delito_generico

    delito_especifico_counts = df['DELITO_ESPECIFICO'].value_counts().head(10)
    fig_delito_especifico = px.bar(delito_especifico_counts, 
                                   x=delito_especifico_counts.index, 
                                   y=delito_especifico_counts.values, 
                                   title='Delitos Específicos Cometidos')
    charts['DelEsp'] = fig_delito_especifico

    fig_delito_vs_genero = px.histogram(df, 
                                        x='DELITO_GENERICO', 
                                        color='GENERO', 
                                        title='Delitos Genericos segun Genero')
    charts['DelGenero'] = fig_delito_vs_genero

    fig_delito_esp_vs_genero = px.histogram(df, x='DELITO_ESPECIFICO', 
                                            color='GENERO', 
                                            title='Delitos Específicos segun Genero')
    charts['DelEspGen'] = fig_delito_esp_vs_genero

    situacion_juridica_counts = df['SITUACION_JURIDICA'].value_counts()
    fig_sit_juridica = px.bar(situacion_juridica_counts, 
                              x=situacion_juridica_counts.index, 
                              y=situacion_juridica_counts.values, 
                              title='Situación Jurídica')
    charts['SitJuridica'] = fig_sit_juridica

    fig_sit_juridica_vs_delito = px.histogram(df, 
                                              x='SITUACION_JURIDICA', 
                                              color='DELITO_ESPECIFICO', 
                                              title='Situación Jurídica segun Delito Específico')
    charts['SitJuridicaEsp'] = fig_sit_juridica_vs_delito

    lugar_counts = df['P202'].value_counts()
    fig_lugar_ocurrencia = px.bar(lugar_counts, x=lugar_counts.index, y=lugar_counts.values, title='Lugar donde ocurrió el Delito')
    charts['Lugar_Delito'] = fig_lugar_ocurrencia

    motivo_counts = df['P203'].value_counts()
    fig_motivo_delito = px.bar(motivo_counts, 
                               x=motivo_counts.index, 
                               y=motivo_counts.values, 
                               title='Motivo Principal del Delito')
    charts['Motivo_Delito'] = fig_motivo_delito

    uso_arma_counts = df['P204'].value_counts()
    fig_uso_arma = px.pie(uso_arma_counts, 
                          names=uso_arma_counts.index, 
                          values=uso_arma_counts.values, 
                          title='Uso de Arma en el Delito', 
                          hole=0.4)  # Gráfico de dona
    charts['UsoArma'] = fig_uso_arma

    fig_edad_arma = px.histogram(df, 
                                 x='P207',
                                 title='Edad a la que Inicio en el Uso de Armas de Fuego',
                                 nbins=15)  # Ajuste de bins
    charts['ArmsFuegInic'] = fig_edad_arma
    
    consumo_counts = df['P209'].value_counts()
    fig_consumo_alcohol_drogas = px.pie(consumo_counts, 
                                        names=consumo_counts.index, 
                                        values=consumo_counts.values, 
                                        title='Consumio Drogas o Alcohol durante el delito', 
                                        hole=0.4)  # Gráfico de dona
    charts['ConsumoDrogasDelito'] = fig_consumo_alcohol_drogas

    organiza_delitos_counts = df['P214'].value_counts()
    fig_organiza_delitos = px.bar(organiza_delitos_counts, 
                                  x=organiza_delitos_counts.index, 
                                  y=organiza_delitos_counts.values, 
                                  title='Fue testigo de delitos dentro del penal durante su estancia allí')
    charts['Delitos-penal'] = fig_organiza_delitos

    centro_juvenil_counts = df['P215'].value_counts()
    fig_centro_juvenil = px.bar(centro_juvenil_counts, 
                                x=centro_juvenil_counts.index, 
                                y=centro_juvenil_counts.values, 
                                title='Fue internado en algun centro juvenil')
    charts['Internado-juvenil'] = fig_centro_juvenil

    declaracion_counts = df['P218'].value_counts()
    fig_declaracion = px.pie(declaracion_counts, 
                             names=declaracion_counts.index, 
                             values=declaracion_counts.values, 
                             title='Se declara inocente o culpable', 
                             hole=0.4)  # Gráfico de dona
    charts['inocente-culpable'] = fig_declaracion

    # Condiciones dentro del penitenciario

    declaracion_counts = df['P301'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='Los servicios Higiénicos se encuentran: ')
    charts['Estado de Servicios Higiénicos'] = fig_declaracion

    declaracion_counts = df['P302'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='La calidad de los alimentos es: ')
    charts['Calidad de los alimentos'] = fig_declaracion  

    declaracion_counts = df['P303'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='Está estudiando algún programa en el establecimiento penitenciario: ')
    charts['Esta en programa de estudios'] = fig_declaracion  

    declaracion_counts = df['P309'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='En el establecimiento penitenciario presentó alguna dolencia: ')
    charts['Dolencia en el penitenciario'] = fig_declaracion     
        
    declaracion_counts = df['P310'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='Fue atendido en el tópico del establecimiento penitenciario: ')
    charts['Atencion en el Penitenciario'] = fig_declaracion  

    series_list = [
        df['P311_1'], df['P311_2'], df['P311_3'], df['P311_4'], df['P311_5'], 
        df['P311_6'], df['P311_7'], df['P311_8'], df['P311_9'], df['P311_10'], df['P311_11']
    ]

    concatenated_series = pd.concat(series_list)
    declaracion_counts = concatenated_series.value_counts()

    fig_declaracion = px.bar(declaracion_counts, 
                            x=declaracion_counts.index, 
                            y=declaracion_counts.values, 
                            title='Razón por la que no acudió al centro médico del establecimiento')
    charts['Razon por que no acudio al centro medico del establecimiento'] = fig_declaracion

    declaracion_counts = df['P313_1'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='En el último mes participó en actividades deportivas')
    charts['Actividad1'] = fig_declaracion      

    declaracion_counts = df['P313_2'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='En el último mes participó en actividades laborales reconocidas por el INPE')
    charts['Actividad2'] = fig_declaracion     

    declaracion_counts = df['P313_3'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='En el último mes participó en actividades laborales de limpieza o mantenimiento de la institución')
    charts['Actividad3'] = fig_declaracion     

    declaracion_counts = df['P313_4'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='En el último mes participó en actividades del programa de tratamiento PIM')
    charts['Actividad4'] = fig_declaracion     

    declaracion_counts = df['P313_5'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='En el último mes participó en otro tipo de actividades ')
    charts['Actividad5'] = fig_declaracion            

    declaracion_counts = df['P314'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values, 
                             title='Razón por la cual no realiza ninguna actividad dentro de la institución')
    charts['Actividad6'] = fig_declaracion      

    # Visita

    declaracion_counts = df['P315'].value_counts()
    fig_declaracion = px.bar(declaracion_counts, 
                             x=declaracion_counts.index, 
                             y=declaracion_counts.values,
                             title='En los últimos 3 meses con qué frecuencia lo visitaron')
    charts['Visita1'] = fig_declaracion        

    declaracion_counts = df['P316'].value_counts()
    fig_declaracion = px.bar(declaracion_counts,
                             x=declaracion_counts.index,
                             y=declaracion_counts.values,
                             title='Quiénes lo visitan frecuentemente')
    charts['Visita2'] = fig_declaracion
    
    # Discriminación

    declaracion_counts = df['P317'].value_counts()
    fig_declaracion = px.pie(declaracion_counts,
                             names=declaracion_counts.index, 
                             values=declaracion_counts.values, 
                             title='Se siente discriminado en el establecimiento penitenciario',
                             hole=0.4)  # Gráfico de dona
    charts['Se siente discriminado'] = fig_declaracion

    declaracion_counts = df['P318'].value_counts()
    fig_declaracion = px.pie(declaracion_counts,
                             names=declaracion_counts.index, 
                             values=declaracion_counts.values, 
                             title='Razón por la cual cree que lo discriminan',
                             hole=0.4)  # Gráfico de dona
    charts['Razon de discriminacion'] = fig_declaracion
    
    return charts


