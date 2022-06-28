import pickle
import json
from nlp_procesamiento import tokenizar, lemmatizar
from funciones_entrenamiento import procesado_datos, entrenar

def entrenar_modelo():
    palabras_tokenizadas = []
    palabras_lematizadas = []
    etiquetas = []
    etiquetas_relacionadas = []
    archivo_patrones = open('./preguntas.json').read()

    dict_patrones = json.loads(archivo_patrones)
    for textos in dict_patrones['preguntas']:
        p, etiqueta, etiq_rel, = tokenizar(textos["patterns"], textos["tag"])
        palabras_tokenizadas += p
        etiquetas += etiqueta
        etiquetas_relacionadas += etiq_rel
    palabras_lematizadas = sorted(list(set(lemmatizar(palabras_tokenizadas))))
    etiquetas = sorted(list(set(etiquetas)))
    pickle.dump(palabras_lematizadas, open('palabras_lematizadas.pkl', 'wb'))
    pickle.dump(etiquetas, open('etiquetas.pkl', 'wb'))
    train_x,train_y = procesado_datos(palabras_lematizadas,etiquetas_relacionadas,etiquetas)
    entrenar(train_x,train_y)


if __name__ == "__main__":
    entrenar_modelo()
