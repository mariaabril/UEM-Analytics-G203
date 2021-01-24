from wtforms import Form
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField
from wtforms import validators

#definimos los distintos formularios y sus requisitos (login, registro)
class LoginForm(Form):
    email = EmailField('Email', [
        validators.Email(message="Por favor, introduce un email valido "),
        validators.Required(message="El email es obligatorio"),
        ])
    
    password = PasswordField('Contraseña', [
        validators.Required(message="La contraseña es obligatoria"),
    ])

class RegisterForm(Form):
    email = EmailField('Email', [
        validators.Email(message="Por favor, introduce un email valido "),
        validators.Required(message="El email es obligatorio"),
        ])
    
    password = PasswordField('Contraseña', [
        validators.Required(message="La contraseña es obligatoria"),
    ])    