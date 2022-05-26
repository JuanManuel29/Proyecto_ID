from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from connection_to_database import Connection
import querys as sql

#-------------------------------------------------APLICACIÓN--------------------------------------------------------------------
#CREACIÓN DE LA APLICACIÓN Y SUS COMPONENTES
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


#---------CREACIÓN DEL GRÁFICO PARA IDENTIFICAR EL TIPO DE SUBCUENTA (FLUJO O STOCK) (1ER ESCENARIO)-------------
con = Connection()
con.openConnection()
query1_1 = pd.read_sql_query(sql=sql.caso1_1(), con=con.connection)
query1_2 = pd.read_sql_query(sql=sql.caso1_2(), con=con.connection)
query1_3 = pd.read_sql_query(sql=sql.caso1_3(), con=con.connection)
query1_4 = pd.read_sql_query(sql=sql.caso1_4(), con=con.connection)
con.closeConnection()
caso1_1 = pd.DataFrame(query1_1, columns=['codigo', 'tipo_registro'])
caso1_2 = pd.DataFrame(query1_2, columns=['tipo_registro','count'])
caso1_3 = pd.DataFrame(query1_3, columns=['codigo','tipo_registro'])
caso1_4 = pd.DataFrame(query1_4, columns=['tipo_registro','count'])

#CREACIÓN DE LOS GRÁFICOS
fig1_1 = px.bar(caso1_1.head(150),
                x="tipo_registro", 
                y="codigo",
                labels={
                    "tipo_registro": "Tipo de registro",
                    "codigo": "Código de subcuenta"
                })

fig1_1.update_yaxes(showticklabels=False)

fig1_2 = px.pie(caso1_2, values='count',
                names='tipo_registro',
                color_discrete_sequence=px.colors.sequential.dense)

fig1_3 = px.bar(caso1_3.head(150),
                x="tipo_registro",
                y="codigo",
                labels = {
                    "tipo_registro": "Tipo de registro",
                    "codigo": "Código de subcuenta"
                    })

fig1_3.update_yaxes(showticklabels=False)

fig1_4 = px.pie(caso1_4, 
                values='count', 
                names='tipo_registro',
                color_discrete_sequence=px.colors.sequential.dense)


fig1_1.update_traces(marker_color='rgb(158,202,225)', 
                                 marker_line_color='rgb(8,48,107)',
                                 marker_line_width=1.5,
                                 opacity=0.6)

fig1_3.update_traces(marker_color='rgb(158,202,225)', 
                                 marker_line_color='rgb(8,48,107)',
                                 marker_line_width=1.5,
                                 opacity=0.6)

#---------CREACIÓN DEL GRÁFICO PARA VISUALIZAR LAS SUBCUENTAS (2DO ESCENARIO)-------------
#CONSULTA DE LOS DATOS Y CREACIÓN DEL DATAFRAME - OFERTA DE TARJETAS
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql=sql.oferta_empresas_tarjetas_credito(), con=con.connection)
con.closeConnection()
dfOferta_tarjetas = pd.DataFrame(query, columns=['nombre', 'cantidad_empresas'])

#GRÁFICO DE BARRAS
figOferta_tarjetas = px.bar(dfOferta_tarjetas.head(),
                            y='nombre', 
                            x='cantidad_empresas',
                            orientation='h',
                            labels={
                                "nombre": "Tipo de entidad",
                                "cantidad_empresas": "Cantidad de empresas"
                                })

figOferta_tarjetas.update_traces(marker_color=px.colors.sequential.Teal, 
                                 marker_line_color=px.colors.sequential.Teal,
                                 marker_line_width=1.5,
                                 opacity=0.6)

#GRÁFICO DE TORTA
pieOferta_tarjetas = px.pie(dfOferta_tarjetas, values='cantidad_empresas',
                            names='nombre',
                            color_discrete_sequence=px.colors.sequential.dense)

# pieOferta_tarjetas.update_traces(hoverinfo='label+percent',
#                                 textinfo='value',
#                                 textfont_size=20,
#                                 marker=dict(colors=inner_colors,
#                                 line=dict(color='rgb(8,48,107)', width=2)))


#---------CREACIÓN DEL GRÁFICO PARA VISUALIZAR LAS SUBCUENTAS (3ER ESCENARIO)-------------
#CONSULTA DE LOS DATOS Y CREACIÓN DEL DATAFRAME PARA LA UTILIZACIÓN DE LAS CUENTAS
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql=sql.subcuentas_utilizadas(), con=con.connection)
con.closeConnection()
dfSubcuentas_utilizadas = pd.DataFrame(query, columns=['codigo', 'cantidad_registros'])

#GRÁFICO DE BARRAS
figBarSubcuentas = px.bar(dfSubcuentas_utilizadas.head(66),
                          x='codigo', 
                          y='cantidad_registros', 
                          title= 'Utilización de subcuentas',
                          text='cantidad_registros',
                          labels = {
                              "codigo": "Código de subcuenta",
                              "cantidad_registros": "Cantidad de registros"
                          })

figBarSubcuentas.update_traces( marker_color='rgb(158,202,225)', 
                                marker_line_color='rgb(8,48,107)',
                                marker_line_width=1.5,
                                opacity=0.6,
                                texttemplate='%{text:.2s}',
                                textposition='outside')


#LAYOUT DE LA APLICACIÓN----------------------------------------------------------------------------
app.layout = html.Div([html.Br(),
            html.H1("Proyecto Tarjetas", 
                    className='text-center fw-bold p-7 m-5 rounded',
                    style={'background-color':'#BFD6EF'}),

    html.H2("Primer caso de análisis: ",
            className='text-center opacity-100, p-0 m-5 bg-secondary text-light fw-bold rounded'),
    dbc.Row(children=[dbc.Col(width=1),
                    dbc.Col(dcc.Graph(
                            id='caso1_1',
                            figure=fig1_1
                        ),width=6
                    ),

                      dbc.Col(
                            dcc.Graph(
                            id='caso1_2',
                            figure=fig1_2
                        ), width=4
                )]
            ),

    dbc.Row(children=[dbc.Col(width=1),
                    dbc.Col(dcc.Graph(
                            id='caso1_3',
                            figure=fig1_3
                        ),width=6
                    ),

                      dbc.Col(
                            dcc.Graph(
                            id='caso1_4',
                            figure=fig1_4
                        ), width=4
                )]
            ),

    html.H2("Segundo caso de análisis: ", 
            className='text-center opacity-100, p-2 m-5 bg-secondary text-light fw-bold rounded'),
    dbc.Row(children=[dbc.Col(width=1),
                    dbc.Col(dcc.Graph(
                        id='barOferta_tarjetas',
                        figure=figOferta_tarjetas
                    ), width=6
                ),
                    dbc.Col(dcc.Graph(
                        id='pieOferta_tarjetas',
                        figure=pieOferta_tarjetas
                    ), width=4
                )]
            ),

    html.H2("Tercer caso de análisis: ", 
            className='text-center opacity-100, p-2 m-5 bg-secondary text-light fw-bold rounded'),
    dbc.Row(children=[dbc.Col(width=1),
                      dbc.Col(dcc.Graph(
                                id='barSubcuentas',
                                figure=figBarSubcuentas
                            ), width=10
                        )]   
                    ),

    html.H2("Cuarto caso de análisis: ", 
            className='text-center opacity-100, p-2 m-5 bg-secondary text-light fw-bold rounded'),
    html.Div([
    dbc.Row(dbc.Col(children=[
                html.H3('Seleccione la tarjeta que desea ver:',style={"font-weight": "bold", 'align-items': 'center'}),
                dcc.Dropdown(
                id="dropdown",
                options=["CREDIBANCO-VISA", 
                        "MASTERCARD","AMERICAN EXPRESS", 
                        "DINERS","OTRAS TARJETAS DE CREDITO", 
                        "ADMINISTRADORAS DE SISTEMAS DE PAGO DE BAJO VALOR"],
                value="CREDIBANCO-VISA",
                clearable=False,
                style={'width': '55%', 'margin':'auto'}
                ),
                dcc.Graph(
                    id='barCompras_Nacional_Exterior'
                ),
                ]
            )
         )], style={'padding-top': 100,'textAlign': 'center'}, className='justify-content-center'),
        
    html.Br(),
    html.Br(),
    html.Br(),

])

@app.callback(
    Output("barCompras_Nacional_Exterior", "figure"), 
    Input("dropdown", "value")
)

def actualizar_grafico(tipo_tarjeta: str):
    dict_tarjetas = ["CREDIBANCO-VISA", "MASTERCARD","AMERICAN EXPRESS", "DINERS"]
    con = Connection()
    con.openConnection()
    query = pd.read_sql_query(sql=sql.compras_avances_tarjetas(tipo_tarjeta), con=con.connection)
    con.closeConnection()
    dfCompras_nacional_vs_exterior = pd.DataFrame(query, columns=['nombre', 'descripcion', 'sum'])
    if tipo_tarjeta in dict_tarjetas:
        figCompras_nacional_vs_exterior = px.bar(dfCompras_nacional_vs_exterior, 
                                                x=['avances-nacional', 'avances-exterior',
                                                'compras-nacional', 'compras-exterior'],
                                                y='sum',
                                                 labels = {
                                                     "x": "Subcuentas",
                                                     "sum": "Total"
                                                 })

    elif tipo_tarjeta == 'OTRAS TARJETAS DE CREDITO':
        figCompras_nacional_vs_exterior = px.bar(dfCompras_nacional_vs_exterior, 
                                                x=['avances-nacional',
                                                'compras-nacional', 'compras-exterior'],
                                                y='sum',
                                                 labels={
                                                     "x": "Subcuentas",
                                                     "sum": "Total"
                                                 })
    
    elif tipo_tarjeta == 'ADMINISTRADORAS DE SISTEMAS DE PAGO DE BAJO VALOR':
        figCompras_nacional_vs_exterior = px.bar(dfCompras_nacional_vs_exterior, 
                                                x=['avances-nacional'],
                                                y='sum',
                                                labels = {
                                                    "x": "Subcuentas",
                                                    "sum": "Total"
                                                })

    figCompras_nacional_vs_exterior.update_traces(marker_color=px.colors.sequential.Teal, 
                                                  marker_line_color='rgb(8,48,107)',
                                                  marker_line_width=1.5,
                                                  opacity=0.6)

    return figCompras_nacional_vs_exterior



#CORRER LA APLICACIÓN--------------------------
if __name__ == '__main__':
 app.run_server(debug=True)

