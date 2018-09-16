#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response
from flask import request

app = Flask(__name__)

faces = {
        'name': "Bob",
        'date': "123"
}

@app.route('/facial/api/v1.0/faces', methods=['GET'])
def get_faces():
    return jsonify({'faces': faces})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/facial/api/v1.0/faces', methods=['POST'])
def create_face():
    if not request.json or not 'faces' in request.json:
        abort(400)
    face = {
        'name': request.json['name'],
        'date': request.json['date']
    }
    faces.append(face)
    return jsonify({'face': face}), 201

if __name__ == '__main__':
    app.run(debug=True)