from flask import Flask, jsonify

app = Flask(__name__)

# Ruta de prueba para verificar la conexión
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Python!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
