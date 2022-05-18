#FUNCIONES PARA DEFINIR LAS QUERYS SQL
def subcuentas_utilizadas():
    return """SELECT codigo, COUNT(r.numero_registro) as cantidad_registros
              FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta) 
              GROUP BY s.codigo
              ORDER BY 1
           """