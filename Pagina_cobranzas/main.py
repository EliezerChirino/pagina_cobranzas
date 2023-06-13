from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from wtforms.csrf.session import SessionCSRF
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import jsonify
import forms
from wtforms.widgets import html_params
import sqlite3
from sqlite3 import Error



app = Flask(__name__)
app.secret_key = 'mi_clave'
csrf = SessionCSRF()

#---------------------------------------------------------Ruta del login-----------------------------------------------------------------------------#

@app.route("/", methods=["GET", "POST"])
def login():
    titulo = 'login'
    login_form = forms.login(request.form)
    
    if request.method == "POST" and login_form.validate():
        username = login_form.username.data.lower()
        clave = login_form.clave.data
        return redirect(url_for('formulario_cobranzas')) 
    
    return render_template('login.html', form=login_form, titulo=titulo) 

@app.route("/formulario_cobranzas", methods=["GET"])
def formulario_cobranzas():
    titulo = "formulario_cobranzas"
    return render_template("index.html", titulo=titulo)


@app.route ("/registro", methods= ["GET"])
def registro():
    titulo= "registro"
    registro_form= forms.RegistroForm(request.form)
    
    if request.method== "POST":
    #-------declaracion variables----------#
        nombre=registro_form.nombre.data.lower()
        contraseña=registro_form.apellido.data.lower()
        identificacion=registro_form.username.data
        email= registro_form.email.data
        
        
    #-------Conexion base de datos----------#    
        #connect=sqlite3.connect(" #basededatos")
        #cursor= connect.cursor()
        
        #sentencia= (""" INSERT INTO usuarios () VALUES ()""" )
        
        
        #cursor.execute( sentencia, ( nombre, contraseña, identificacion, email  ))
        #connect.commit()
        #connect.close()
        
        return redirect(url_for('login'))
    return render_template("registro_usuario.html",titulo=titulo, form=registro_form)

@app.route ("/tabla_vista_registro", methods= ["GET"])
def tabla_vista_registro():
    titulo= "tabla_vista_registro"

    return render_template("tabla_vista_registro.html",titulo=titulo)

if __name__ == "__main__":
    
	app.run(debug=True, port=5000, host="0.0.0.0")
 
        