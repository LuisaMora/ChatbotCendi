from flask import Flask, jsonify, request
from train_chatbot import train
from chatgui import chatbot_response

app = Flask(__name__)

@app.route('/chatbot', methods=['GET'])
def get_respuesta():
    return jsonify({"mensaje":"Hola a todos"})

@app.route('/chatbot', methods=['POST'])
def post_metodo():
    try:
        mensaje = request.json
        print(mensaje)
        respuesta = chatbot_response(mensaje["mensaje"])
        return jsonify({"mensaje":respuesta})
    except Exception as e:
        print(Exception)
        return jsonify({"mensaje":"Error al obtener la respuesta"}),500

@app.route('/chatbot/entrenar', methods=['GET'])
def post_metodo_entrenar():
    try:
        train()
        return jsonify({"mensaje":"Modelo entrenado"})
    except:
        return jsonify({"mensaje":"Error al entrenar el modelo"}),500

if __name__ =="__main__":
    app.run(debug=True, port=5050)
