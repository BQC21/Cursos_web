import pymysql
import os

class DAOCursos:
    def connect(self):
        # Replace the values in angle brackets with your own values
        return pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_DATABASE"),
            ssl={'ssl': {'cert': 'ruta_a_certificado', 'key': 'ruta_a_llave', 'ca': 'ruta_a_ca'}}
            # ssl_verify_identity=True,
            # ssl_ca='c:\Descargas\cacert-2023-08-22.pem'
        )

    def read(self, id):
        con = DAOCursos.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM cursos order by nombre asc")
            else:
                cursor.execute("SELECT * FROM cursos where id = %s order by nombre asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOCursos.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO usuario(nombre,creditos,ciclo,nota,estado) VALUES(%s, %s, %s, %s, %s)", (data['nombre'],data['creditos'],data['ciclo'],data['nota'],data['estado'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOCursos.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE cursos set nombre = %s, creditos = %s, ciclo = %s, nota = %s, estado = %s  where id = %s", (data['nombre'],data['creditos'],data['ciclo'],data['nota'],data['estado'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOCursos.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM cursos where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()