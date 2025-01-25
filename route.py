from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Ruta para cargar los datos de préstamos desde el archivo JSON
def cargar_prestamos():
    with open('prestamos.json', 'r') as f:
        return json.load(f)

# Ruta para guardar los datos de préstamos en el archivo JSON
def guardar_prestamos(prestamos):
    with open('prestamos.json', 'w') as f:
        json.dump(prestamos, f, indent=4)

# Obtener todos los préstamos
@app.route('/prestamos', methods=['GET'])
def obtener_prestamos():
    prestamos = cargar_prestamos()
    return jsonify(prestamos)

# Obtener un préstamo por ID
@app.route('/prestamos/<int:id>', methods=['GET'])
def obtener_prestamo(id):
    prestamos = cargar_prestamos()
    prestamo = next((p for p in prestamos if p['id'] == id), None)
    if prestamo:
        return jsonify(prestamo)
    else:
        return jsonify({'mensaje': 'Préstamo no encontrado'}), 404

# Crear un nuevo préstamo
@app.route('/prestamos', methods=['POST'])
def crear_prestamo():
    nuevos_datos = request.get_json()
    prestamos = cargar_prestamos()

    # Crear un nuevo ID basado en el último préstamo
    nuevo_id = max([p['id'] for p in prestamos], default=0) + 1
    nuevos_datos['id'] = nuevo_id
    prestamos.append(nuevos_datos)
    
    guardar_prestamos(prestamos)
    
    return jsonify(nuevos_datos), 201

# Actualizar un préstamo por ID
@app.route('/prestamos/<int:id>', methods=['PUT'])
def actualizar_prestamo(id):
    prestamos = cargar_prestamos()
    prestamo = next((p for p in prestamos if p['id'] == id), None)
    
    if prestamo:
        datos_actualizados = request.get_json()
        prestamo.update(datos_actualizados)
        guardar_prestamos(prestamos)
        return jsonify(prestamo)
    else:
        return jsonify({'mensaje': 'Préstamo no encontrado'}), 404

# Eliminar un préstamo por ID
@app.route('/prestamos/<int:id>', methods=['DELETE'])
def eliminar_prestamo(id):
    prestamos = cargar_prestamos()
    prestamo = next((p for p in prestamos if p['id'] == id), None)
    
    if prestamo:
        prestamos.remove(prestamo)
        guardar_prestamos(prestamos)
        return jsonify({'mensaje': 'Préstamo eliminado'}), 200
    else:
        return jsonify({'mensaje': 'Préstamo no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
