import random
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.models import Sequential
import numpy as np
import pickle
import json
from nlp_procesamiento import tokenizar, lemmatizar
from entrenador import procesado_datos, entrenar
import nltk

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


def entrenarModelo():
    palabras_tokenizadas = []
    palabras_lematizadas = []
    etiquetas = []
    etiquetas_relacionadas = []
    archivo_patrones = open('./intents.json').read()

    dict_patrones = json.loads(archivo_patrones)
    for textos in dict_patrones['intents']:
        p, etiqueta, etiq_rel, = tokenizar(textos["patterns"], textos["tag"])
        palabras_tokenizadas += p
        etiquetas += etiqueta
        etiquetas_relacionadas += etiq_rel
    # print(palabras_tokenizadas)
    palabras_lematizadas = sorted(list(set(lemmatizar(palabras_tokenizadas))))
    etiquetas = sorted(list(set(etiquetas)))
    pickle.dump(palabras_lematizadas, open('palabras_lematizadas.pkl', 'wb'))
    pickle.dump(etiquetas, open('etiquetas.pkl', 'wb'))
    train_x,train_y = procesado_datos(palabras_lematizadas,etiquetas_relacionadas,etiquetas)
    entrenar(train_x,train_y)



if __name__ == "__main__":
    entrenarModelo()
    # train()
    # words=[]
    # classes = []
    # documents = []
    # ignore_words = ['?', '!']
    # data_file = open('intents.json').read()
    # intents = json.loads(data_file)

    # for intent in intents['intents']:
    #     words+=tokenizar(intent["patterns"],intent["tag"])
    # print(words)
