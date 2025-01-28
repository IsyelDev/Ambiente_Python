my_flask_app/
│
├── app.py                # Archivo principal de la aplicación
├── templates/            # Carpeta para las plantillas HTML
│   ├── index.html
│   └── create_item.html
└── static/               # Carpeta para archivos estáticos (CSS, JS, etc.)


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # URI de la base de datos (SQLite en este caso)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Item('{self.name}', '{self.description}')"



@app.route('/')
def index():
    items = Item.query.all()  # Trae todos los ítems de la base de datos
    return render_template('index.html', items=items)


@app.route('/create', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_item = Item(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))  # Redirige al índice después de crear el ítem

    return render_template('create_item.html')


@app.route('/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))
