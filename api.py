from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['GET'])
def get_respuesta():
    return jsonify({"mensaje":"Hola a todos"})

@app.route('/chatbot', methods=['POST'])
def post_metodo():
    return jsonify({"mensaje":"Recibi el mensaje"})


if __name__ =="__main__":
    app.run(debug=True, port=5050)
