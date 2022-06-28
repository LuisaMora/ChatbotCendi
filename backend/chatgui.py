
import pickle
import numpy as np

from tensorflow.keras.models import load_model

import json
import random
from nlp_procesamiento import tokenizar,lemmatizar

class ChatBot:
    def __init__(self) -> None:
        self.modelo = load_model('./modelo_generado.h5')
        self.corpus = json.loads(open('./preguntas.json').read())
        self.palabras_lematizadas = pickle.load(open('./palabras_lematizadas.pkl','rb'))
        self.etiquetas = pickle.load(open('./etiquetas.pkl','rb'))

    def _buscar_pal_lematizada(self, sentence, show_details=True):
        pal_tokenizada = tokenizar(sentence,"")
        pal_lemmatizda = lemmatizar(pal_tokenizada)
        bag_pal = [0]*len(self.palabras_lematizadas)  
        for s in pal_lemmatizda:
            for i,w in enumerate(self.palabras_lematizadas):
                if w == s: 
                    bag_pal[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag_pal))

    def _predecir_tag(self,sentence):
        p = self._buscar_pal_lematizada(sentence,show_details=True)
        res = self.modelo.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": self.etiquetas[r[0]], "probability": str(r[1])})
        return return_list

    def _obtener_respuesta(self,respuestas_probables):
        tag = respuestas_probables[0]['intent']
        lista_patrones = self.corpus['intents']
        for patron_con_tag in lista_patrones:
            if(patron_con_tag['tag']== tag):
                result = random.choice(patron_con_tag['responses'])
                break
        return result

    def responde(self,mensaje):
        respuestas_probables = self._predecir_tag(mensaje)
        print(respuestas_probables)
        res = self._obtener_respuesta(respuestas_probables)
        return res

