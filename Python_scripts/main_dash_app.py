from turtle import width
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from connection_to_database import Connection
import querys as sql


#-------------------------------------------------APLICACIÓN--------------------------------------------------------------------
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
#CREACIÓN DE LA APLICACIÓN Y SUS COMPONENTES
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

#---------CREACIÓN DEL GRÁFICO PARA VISUALIZAR LAS SUBCUENTAS (3ER ESCENARIO)-------------
#CONSULTA DE LOS DATOS Y CREACIÓN DEL DATAFRAME
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql=sql.subcuentas_utilizadas(), con=con.connection)
con.closeConnection()
dfSubcuentas = pd.DataFrame(query, columns=['codigo', 'cantidad_registros'])

#GRÁFICO DE BARRAS
figBarSubcuentas = px.bar(dfSubcuentas.head(66), x='codigo', y='cantidad_registros')
#(para dos barras se pone el atributo barmode='group')


#LAYOUT DE LA APLICACIÓN
app.layout = html.Div([
    html.H1("Proyecto ID", className='text-center fw-bold text-light'),
    html.H2("Tercer caso de análisis: ", className='text-center opacity-100, p-2 m-5 bg-secondary text-light fw-bold rounded'),
    dbc.Row(dbc.Col(dcc.Graph(
                        id='barSubcuentas',
                        figure=figBarSubcuentas
                    ), width=7
                )   
            )   
])


#CORRER LA APLICACIÓN--------------------------
if __name__ == '__main__':
 app.run_server(debug=True)
