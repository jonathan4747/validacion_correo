from correo_app.modelos.modelo_correo import Correo
from flask import render_template, request, redirect, session
from correo_app import app

@app.route('/' , methods=['GET'])
def paginaPrincipal():
     return render_template('index.html')
 
@app.route('/success' , methods=['GET'])
def paginaRegistro():
     lista=Correo.obtenerListaCorreo()
     #print("esto es lista",lista)
     return render_template('plataforma.html',email=lista)
 
@app.route('/registro', methods=['POST'])
def Registro():
    nuevoCorreo={
        "correo" : request.form["correo"]
    }
    validar=Correo.Validacion(nuevoCorreo)
    if not validar:
        return redirect ('/')
    else:
        resultado=Correo.agregarCorreo(nuevoCorreo) 
        return redirect('/success')

@app.route( '/success/<int:id>', methods=["POST"] )
def eliminarCorreo( id ):
    eliminado= {
        "id" : id
    }
    resultado = Correo.eliminarCorreo(eliminado)
    print('esto es elimanado',eliminado)
    return redirect( '/success' )
