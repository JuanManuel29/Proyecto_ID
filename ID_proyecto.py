import dash
from dash import dcc
from dash import html
import plotly.express as px 
import plotly.graph_objects as go
import psycopg2
import credenciales as cd

#CONEXIÓN CON LA BASE DE DATOS-------------------------------------------------
connection = psycopg2.connect(user=cd.user,
                        password=cd.password,
                        database=cd.dbname,
                        host=cd.host,
                        port=cd.port)

#-----CREACIÓN DE LAS SENTENCIAS PARA HACER LA CONSULTA DE LAS TABLAS DE LA BD

#SENTENCIA PARA LA CONSULTA DE LA TABLA ''
print("-----------------DATOS DE LA TABLA ''-------------------- ")
cur = connection.cursor()
cur.execute('SELECT * FROM ')
muestra = cur.fetchall()
for i in range(len(muestra)):
        print(muestra[i])
cur.close()
connection.close()


#SENTENCIA PARA LA CONSULTA DE LA TABLA ''
print("-----------------DATOS DE LA TABLA ''-------------------- ")
cur = connection.cursor()
cur.execute('SELECT * FROM ')
muestra = cur.fetchall()
for i in range(len(muestra)):
        print(muestra[i])
cur.close()
connection.close()


#SENTENCIA PARA LA CONSULTA DE LA TABLA ''
print("-----------------DATOS DE LA TABLA ''-------------------- ")
cur = connection.cursor()
cur.execute('SELECT * FROM ')
muestra = cur.fetchall()
for i in range(len(muestra)):
        print(muestra[i])
cur.close()
connection.close()


#SENTENCIA PARA LA CONSULTA DE LA TABLA ''
print("-----------------DATOS DE LA TABLA ''-------------------- ")
cur = connection.cursor()
cur.execute('SELECT * FROM ')
muestra = cur.fetchall()
for i in range(len(muestra)):
        print(muestra[i])
cur.close()
connection.close()


#SENTENCIA PARA LA CONSULTA DE LA TABLA ''
print("-----------------DATOS DE LA TABLA ''-------------------- ")
cur = connection.cursor()
cur.execute('SELECT * FROM ')
muestra = cur.fetchall()
for i in range(len(muestra)):
        print(muestra[i])
cur.close()
connection.close()


#SENTENCIA PARA LA CONSULTA DE LA TABLA ''
print("-----------------DATOS DE LA TABLA ''-------------------- ")
cur = connection.cursor()
cur.execute('SELECT * FROM ')
muestra = cur.fetchall()
for i in range(len(muestra)):
        print(muestra[i])
cur.close()
connection.close()


# #APLICACIÓN--------------------------------------------------------------------
# #CREACIÓN DE LA APLICACIÓN
# app = dash.Dash()


# #LAYOUT DE LA APLICACIÓN
# app.layout = html.Div('Proyecto ID')


# #CORRER LA APLICACIÓN--------------------------
# if __name__ == '__main__':
#  app.run_server(debug=True)