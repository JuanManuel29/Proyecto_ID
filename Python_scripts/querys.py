#FUNCIONES PARA DEFINIR LAS QUERYS SQL
def caso1_1():
    return  """ SELECT codigo, 'Stock' as tipo_registro
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica = r.total


                UNION

                SELECT codigo, 'Flujos' as tipo_registro
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica != r.total
                ORDER BY 1
            """


def caso1_2():
    return  """ SELECT 'Flujos' as tipo_registro, COUNT(DISTINCT s.codigo)
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica = r.total
                UNION
                SELECT 'Stock' as tipo_registro, COUNT(DISTINCT s.codigo)
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica != r.total;
            """

def caso1_3():
    return  """SELECT s.codigo, 'Flujos' as tipo_registro
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica = r.total


                UNION

                SELECT s.codigo, 'Stock' as tipo_registro
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica != r.total


                UNION

                SELECT s.codigo, 'Desviaciones' as tipo_registro
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica = r.total


                INTERSECT 

                SELECT s.codigo, 'Desviaciones' as tipo_registro
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica != r.total
            """
            
def caso1_4():
    return  """ SELECT 'Desviaciones' as tipo_registro, count(codigo) FROM (
                SELECT s.codigo, 'Desviaciones' as tipo
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica = r.total

                INTERSECT 

                SELECT s.codigo, 'Desviaciones' as tipo
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica != r.total) A WHERE tipo='Desviaciones'

                UNION

                SELECT 'Flujos' as tipo_registro, COUNT(codigo) FROM (
                SELECT s.codigo, 'Flujos' as tipo_registro
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica = r.total 

                EXCEPT

                SELECT s.codigo, 'Flujos' as tipo_registro
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica != r.total 
                ) A WHERE tipo_registro='Flujos'

                UNION

                SELECT 'Stock' as tipo_registro, COUNT(codigo) FROM (
                SELECT s.codigo, 'Stock' as tipo_registro
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica != r.total 

                EXCEPT

                SELECT s.codigo, 'Stock' as tipo_registro
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta)
                WHERE r.natural + r.juridica = r.total 
                ) A WHERE tipo_registro='Stock'
            """

def oferta_empresas_tarjetas_credito():
    return """  SELECT clase.nombre, COUNT(e.nombre) as cantidad_empresas
                FROM clase INNER JOIN entidad as e ON (clase.codigo = e.codigo_clase)
                GROUP BY clase.codigo;
           """

def subcuentas_utilizadas():
    return """  SELECT codigo, COUNT(r.numero_registro) as cantidad_registros
                FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta) 
                GROUP BY s.codigo
                ORDER BY 1
           """

def compras_avances_tarjetas(tipo_tarjeta):
    if tipo_tarjeta == 'CREDIBANCO-VISA':
        return """  SELECT uca.nombre, s.descripcion, sum(r.total)
                    FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta) INNER JOIN UCA ON (r.codigo_uca = uca.codigo)
                    WHERE uca.nombre = 'CREDIBANCO-VISA' AND (s.codigo = 25 or s.codigo = 30 or s.codigo = 35 or s.codigo = 40)
                    GROUP BY uca.nombre, s.descripcion;
               """

    elif tipo_tarjeta == 'AMERICAN EXPRESS':
        return """  SELECT uca.nombre, s.descripcion, sum(r.total)
                    FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta) INNER JOIN UCA ON (r.codigo_uca = uca.codigo)
                    WHERE uca.nombre = 'CREDIBANCO-VISA' AND (s.codigo = 25 or s.codigo = 30 or s.codigo = 35 or s.codigo = 40)
                    GROUP BY uca.nombre, s.descripcion;
               """

    elif tipo_tarjeta == 'MASTERCARD':
        return """  SELECT uca.nombre, s.descripcion, sum(r.total)
                    FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta) INNER JOIN UCA ON (r.codigo_uca = uca.codigo)
                    WHERE uca.nombre = 'MASTERCARD' AND (s.codigo = 25 or s.codigo = 30 or s.codigo = 35 or s.codigo = 40)
                    GROUP BY uca.nombre, s.descripcion;
               """

    elif tipo_tarjeta == 'DINERS':
        return """  SELECT uca.nombre, s.descripcion, sum(r.total)
                    FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta) INNER JOIN UCA ON (r.codigo_uca = uca.codigo)
                    WHERE uca.nombre = 'DINERS' AND (s.codigo = 25 or s.codigo = 30 or s.codigo = 35 or s.codigo = 40)
                    GROUP BY uca.nombre, s.descripcion;
               """
    elif tipo_tarjeta == 'OTRAS TARJETAS DE CREDITO':
        return """  SELECT uca.nombre, s.descripcion, sum(r.total)
                    FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta) INNER JOIN UCA ON (r.codigo_uca = uca.codigo)
                    WHERE uca.nombre = 'OTRAS TARJETAS DE CREDITO' AND (s.codigo = 25 or s.codigo = 30 or s.codigo = 35 or s.codigo = 40)
                    GROUP BY uca.nombre, s.descripcion;
               """

    elif tipo_tarjeta == 'ADMINISTRADORAS DE SISTEMAS DE PAGO DE BAJO VALOR':
        return """  SELECT uca.nombre, s.descripcion, sum(r.total)
                    FROM subcuenta s INNER JOIN registro r ON (s.codigo = r.codigo_subcuenta) INNER JOIN UCA ON (r.codigo_uca = uca.codigo)
                    WHERE uca.nombre = 'ADMINISTRADORAS DE SISTEMAS DE PAGO DE BAJO VALOR' AND (s.codigo = 25 or s.codigo = 30 or s.codigo = 35 or s.codigo = 40)
                    GROUP BY uca.nombre, s.descripcion;
               """
    