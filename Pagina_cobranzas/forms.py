from wtforms import Form
from wtforms import StringField
from wtforms.fields.html5 import EmailField
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import RadioField
from wtforms import SelectField
from wtforms import validators
from wtforms import IntegerField
from wtforms import FloatField, DecimalField
from wtforms import BooleanField
from wtforms.fields import TimeField
from wtforms.fields import DateField
from wtforms import HiddenField
from wtforms import SubmitField
from wtforms.fields import BooleanField
from wtforms.fields.html5 import DateTimeLocalField 
from wtforms.fields import TextAreaField
from wtforms.fields import DateTimeField, TimeField



def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo no debe estar vacio.')

class login(Form):
    username = StringField("", [validators.InputRequired(message="Nombre de usuario vacio!")])
    clave = PasswordField("", [validators.InputRequired(message="Ingrese la contraseña!"),
                               validators.Length(min=6,max=15,message="Se requiere contraseña")])
    honeypot = HiddenField('',[length_honeypot])

class RegistroForm(Form):
    nombre= StringField("", [validators.InputRequired(message="Ingrese su nombre porfavor")])
    identificacion = StringField("", [validators.InputRequired(message="Ingrese su nombre porfavor")])
    contraseña = PasswordField("", [validators.InputRequired(message="Ingrese la contraseña!"),
                               validators.Length(min=6,max=15,message="Se requiere contraseña")])
    email= EmailField("Email",  [validators.InputRequired("Por favor, ingresa tu dirección de correo.")])
    
    

    
    
