from correo_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{3}$')

class Correo:
    def __init__(self,id,correo,created_at,updated_at):
        self.id = id
        self.correo= correo
        self.created_at=created_at
        self.updated_at=updated_at
        
    @classmethod
    def agregarCorreo(cls,nuevo):
        query = "INSERT INTO usuario(correo,created_at,updated_at) VALUES(%(correo)s,NOW(),NOW());"
        resultado = connectToMySQL("correo").query_db(query,nuevo)
        return resultado
    
    @classmethod
    def obtenerListaCorreo(cls):
        query = "SELECT * FROM usuario;"
        resultado = connectToMySQL( "correo" ).query_db( query )
        #print("este es resultado",resultado)
        listaCorreos = []
        for ruta in resultado:
            listaCorreos.append( Correo(ruta["id"],ruta["correo"],ruta["created_at"],ruta["updated_at"]))
        return listaCorreos
    
    @classmethod
    def eliminarCorreo(cls,eliminaCorreo):
        query = "DELETE FROM usuario WHERE id= %(id)s;"
        resultado = connectToMySQL( "correo" ).query_db( query, eliminaCorreo )
        print("Verificar si llega al metodo",query)
        return resultado
    
    @staticmethod
    def Validacion(nuevo):
        valida= True
        if not EMAIL_REGEX.match(nuevo['correo']):
            flash("correo invalido,probar otra vez!!!")
            valida=False
        return valida