from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Configuración inicial
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:contraseña@localhost/nombre_base_de_datos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'clave_secreta_segura'  # Para usar Flask-WTF y mensajes flash

# Base de datos
db = SQLAlchemy(app)

# Modelo de Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# Formulario para manejar usuarios
class UsuarioForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    submit = SubmitField('Guardar')

# Rutas
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/usuarios', methods=['GET', 'POST'])
def mostrar_usuarios():
    usuarios = Usuario.query.all()
    form = UsuarioForm()
    if form.validate_on_submit():
        nuevo_usuario = Usuario(nombre=form.nombre.data)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario agregado exitosamente', 'success')
        return redirect(url_for('mostrar_usuarios'))
    return render_template('usuarios.html', usuarios=usuarios, form=form)

@app.route('/crear', methods=['GET', 'POST'])
def crear_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        nuevo_usuario = Usuario(nombre=form.nombre.data)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario creado exitosamente', 'success')
        return redirect(url_for('mostrar_usuarios'))
    return render_template('crear.html', form=form)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    form = UsuarioForm(obj=usuario)
    if form.validate_on_submit():
        usuario.nombre = form.nombre.data
        db.session.commit()
        flash('Usuario actualizado exitosamente', 'info')
        return redirect(url_for('mostrar_usuarios'))
    return render_template('editar.html', form=form)

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado exitosamente', 'danger')
    return redirect(url_for('mostrar_usuarios'))

if __name__ == "__main__":
    app.run(debug=True)
