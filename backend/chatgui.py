
import pickle
import numpy as np

from tensorflow.keras.models import load_model

import json
import random
from nlp_procesamiento import tokenizar,lemmatizar

class ChatBot:
    def __init__(self) -> None:
        self.model = load_model('./chatbot_model.h5')
        self.intents = json.loads(open('./intents.json').read())
        self.words = pickle.load(open('./palabras_lematizadas.pkl','rb'))
        self.classes = pickle.load(open('./etiquetas.pkl','rb'))

    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

    def _bow(self, sentence, show_details=True):
        # tokenize the pattern
        print(sentence )
        pal_tokenizada = tokenizar(sentence,"")
        print(pal_tokenizada)
        pal_lemmatizda = lemmatizar(pal_tokenizada)
        # bag of words - matrix of N words, vocabulary matrix
        bag = [0]*len(self.words)  
        for s in pal_lemmatizda:
            for i,w in enumerate(self.words):
                if w == s: 
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag))

    def _predict_class(self,sentence):
        # filter out predictions below a threshold
        p = self._bow(sentence,show_details=True)
        res = self.model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})
        return return_list

    def _getResponse(self,ints):
        tag = ints[0]['intent']
        list_of_intents = self.intents['intents']
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                break
        return result

    def chatbot_response(self,msg):
        ints = self._predict_class(msg)
        print(ints)
        res = self._getResponse(ints)
        return res

