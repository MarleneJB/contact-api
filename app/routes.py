from flask import request, jsonify
from app import app, db
from app.models import Contact

@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    telefono = data.get('telefono')  
    asunto = data.get('asunto')  
    mensaje = data.get('mensaje')

    if not nombre or not email or not mensaje:
        return jsonify({'error': 'Faltan datos'}), 400

    contact = Contact(nombre=nombre, email=email, telefono=telefono, asunto=asunto, mensaje=mensaje)
    db.session.add(contact)
    db.session.commit()

    return jsonify({'mensaje': 'Contacto creado'}), 201

@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    contact_list = [{'id': c.id, 'nombre': c.nombre, 'email': c.email, 'telefono': c.telefono, 'asunto': c.asunto, 'mensaje': c.mensaje} for c in contacts]
    return jsonify(contact_list)