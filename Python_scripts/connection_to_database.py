import psycopg2
import credenciales as cd

class Connection:
    
    def __init__(self):
        self.connection = None
    
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(user=cd.user,
                                               password=cd.password,
                                               database=cd.dbname,
                                               host=cd.host, 
                                               port=cd.port)
        except Exception as e:
            print (e)

    def closeConnection(self):
        self.connection.close()