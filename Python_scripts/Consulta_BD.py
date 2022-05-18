import psycopg2
import credenciales as cd

#CONEXIÓN CON LA BASE DE DATOS-------------------------------------------------
connection = psycopg2.connect(user=cd.user,
                              password=cd.password,
                              database=cd.dbname,
                              host=cd.host,
                              port=cd.port)


#LISTA QUE CONTIENE LOS NOMBRES DE LAS TABLAS DE LA BASE DE DATOS
table_names = ['clase', 'entidad', 'subcuenta', 'uca', 'registro', 'oferta']


#FUNCION QUE PERMITE VISUALIZAR TODAS LAS TUPLAS DE LA TABLA QUE SE DESEE
def print_all_data(table_name: str):
        try:
                print(f"-----------------DATOS DE LA TABLA '{table_name}'--------------------")
                cur = connection.cursor()
                cur.execute(f'SELECT * FROM {table_name}')
                data = cur.fetchall()
                for i in range(len(data)):
                        print(data[i])
                cur.close()
                connection.close()
        except:
                print(f'THERE IS NO TABLE NAMED: "{table_name}" ')


#EJECUCION DE LA FUNCION
print_all_data(table_name = 'oferta')

