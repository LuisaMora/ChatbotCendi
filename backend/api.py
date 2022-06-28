from flask import Flask, jsonify
from train_chatbot import entrenar_modelo
from chatgui import ChatBot
import json

app = Flask(__name__)


@app.route('/chatbot', methods=['GET'])
def get_respuesta():
    return jsonify({"mensaje": "Hola a todos"})


@app.route('/chatbot/<index_no>', methods=['POST'])
def post_metodo(index_no):
    try:
        chatbot = ChatBot()
        print(index_no)
        mensaje = index_no
        print(mensaje)
        respuesta = chatbot.responde(mensaje)
        print(f"-----*************{respuesta}")

        data_json = json.dumps(respuesta)
        archivo_json = open("../frontend/data.json", "w")
        archivo_json.write(data_json)
        archivo_json.close()
        return jsonify({"body": respuesta}), 200
    except Exception as e:
        print(e)
        return jsonify({"mensaje": "Error al obtener la respuesta"}), 500


@app.route('/chatbot/entrenar', methods=['GET'])
def post_metodo_entrenar():
    try:
        entrenar_modelo()
        return jsonify({"mensaje": "Modelo entrenado"})
    except:
        return jsonify({"mensaje": "Error al entrenar el modelo"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5050)
