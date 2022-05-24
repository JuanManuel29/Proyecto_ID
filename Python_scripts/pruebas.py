from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from connection_to_database import Connection
import querys as sql


con = Connection()
con.openConnection()
query = pd.read_sql_query(sql=sql.compras_avances_tarjetas('ADMINISTRADORAS DE SISTEMAS DE PAGO DE BAJO VALOR'), con=con.connection)
con.closeConnection()
dfCompras_nacional_vs_exterior = pd.DataFrame(query, columns=['nombre', 'descripcion', 'sum'])

figCompras_nacional_vs_exterior = px.bar(dfCompras_nacional_vs_exterior, x=['avances-nacional'],
                                                                         y='sum')
figCompras_nacional_vs_exterior.show()


print(dfCompras_nacional_vs_exterior['sum'])

"""marker_color='rgb(158,202,225)', 
                                 marker_line_color='rgb(8,48,107)',
                                 marker_line_width=1.5,
                                 opacity=0.6)
                                """
