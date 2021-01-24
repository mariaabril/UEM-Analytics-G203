import pandas as pd
import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, session, url_for, flash)

#importamos templates
import database
import forms
import get_data
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

database.db.init_app(app)
database.CreateDatabase()

#landing page
@app.route('/', methods = ['GET', 'POST'])
def index():
    #miramos si el usuario esta en la sesion
    if 'email' not in session:
        return redirect(url_for('login'))
        print(email)

    if 'email' in session:
        email = session['email']
        print(email)

    title = 'SMART HOME'
    tituloPag = 'SMART HOUSE'

    datos = get_data.data_to_html()

    return render_template('landing.html', title=title, tituloPag=tituloPag, datos=datos)

@app.route('/predictions', methods = ['GET', 'POST'])
def predictions():
    title = 'SMART HOME'
    tituloPag = 'PREDICCIONES'

    return render_template('predictions.html', title=title, tituloPag=tituloPag)

@app.route('/dash_hab1', methods = ['GET', 'POST'])
def hab1():
    title = 'SMART HOME'
    tituloPag = 'HABITACIÓN 1'
    return render_template('/dashboards/dash_hab1.html', title=title, tituloPag=tituloPag)

@app.route('/dash_hab2', methods = ['GET', 'POST'])
def hab2():
    title = 'SMART HOME'
    tituloPag = 'HABITACIÓN 2'
    return render_template('/dashboards/dash_hab2.html', title=title, tituloPag=tituloPag)
    
@app.route('/dash_salon', methods = ['GET', 'POST'])
def salon():
    title = 'SMART HOME'
    tituloPag = 'SALON'
    return render_template('/dashboards/dash_salon.html', title=title, tituloPag=tituloPag)
    
@app.route('/dash_despacho', methods = ['GET', 'POST'])
def despacho():
    title = 'SMART HOME'
    tituloPag = 'DESPACHO'
    return render_template('/dashboards/dash_despacho.html', title=title, tituloPag=tituloPag)
    
@app.route('/dash_pasillo', methods = ['GET', 'POST'])
def pasillo():
    title = 'SMART HOME'
    tituloPag = 'PASILLO'
    return render_template('/dashboards/dash_pasillo.html', title=title, tituloPag=tituloPag)
    
@app.route('/dash_patio', methods = ['GET', 'POST'])
def patio():
    title = 'SMART HOME'
    tituloPag = 'PATIO'
    return render_template('/dashboards/dash_patio.html', title=title, tituloPag=tituloPag)

@app.route('/dash_bano1', methods = ['GET', 'POST'])
def bano1():
    title = 'SMART HOME'
    tituloPag = 'BAÑO 1'
    return render_template('/dashboards/dash_bano1.html', title=title, tituloPag=tituloPag)

@app.route('/dash_bano2', methods = ['GET', 'POST'])
def bano2():
    title = 'SMART HOME'
    tituloPag = 'BAÑO 2'
    return render_template('/dashboards/dash_bano2.html', title=title, tituloPag=tituloPag)

@app.route('/dash_cocina', methods = ['GET', 'POST'])
def cocina():
    title = 'SMART HOME'
    tituloPag = 'COCINA'
    return render_template('/dashboards/dash_cocina.html', title=title, tituloPag=tituloPag)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    title = 'LOG-IN'
    tituloPag='Inicio de sesión'
    if request.method == 'POST' and login_form.validate():
        email = login_form.email.data
        passw = login_form.password.data
        #si existe va a devolver el usuario y si no devuelve None
        user = database.User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(passw):
            success_message = 'Bienvenido {}'.format(email)
            category = "alert alert-success alert-dismissible"
            flash(success_message, category)
            session['email'] = email
            return redirect( url_for('index') )
        else:
            user = None
            error_message = 'Usuario o contraseña incorrectos'
            category = "alert alert-danger alert-dismissible"
            flash(error_message, category)
        #validamos que la contraseña sea la misma 
        
    return render_template('login.html', title=title, form=login_form, tituloPag=tituloPag)

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = forms.RegisterForm(request.form)
    title = 'REGISTER'
    tituloPag='Registro'
    if request.method == 'POST' and register_form.validate():
        email = register_form.email.data
        passw = register_form.password.data
        #comprobar que no este en la base de datos
        user = database.User.query.filter_by(email=email).first()
        if user is None:
            user = database.User(email = email, password = passw)
            database.db.session.add(user)
            database.db.session.commit()
        
            success_message = 'Usuario {} registrado'.format(email)
            category = "alert alert-success alert-dismissible"
            flash(success_message, category)
            session['email'] = email
            return redirect( url_for('index') )
        
        else:
            error_message = 'Ya existe este usuario'
            category = "alert alert-danger alert-dismissible"
            flash(error_message, category)
        
    return render_template('register.html', title=title, form=register_form, tituloPag=tituloPag)

@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return redirect(url_for('login'))

@app.route('/delete')
def delete():
    if 'email' in session:
        user = database.User.query.filter_by(email=session.get('email')).first()
        database.db.session.delete(user)
        database.db.session.commit()
        session.pop('email')

    success_message = 'Usuario eliminado correctamente'
    category = "alert alert-success alert-dismissible"
    flash(success_message, category)

    return redirect(url_for('login'))

@app.route('/img/<path:filename>')
def send_file(filename):
    return send_from_directory('img', filename)

@app.route('/templates/graficos/<path:filename>')
def send_file_csv(filename):
    return send_from_directory('templates/graficos', filename)

#le metemos el numero correspondiente de error
@app.errorhandler(404)
def page_not_found(e):
    return(render_template('404.html'), 404)

if __name__ == '__main__':
    app.run(debug=True)
