from nlp_procesamiento import lemmatizar
import random
import numpy as np
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.models import Sequential

def procesado_datos(palabras_lematizadas,etiquetas_relacionadas, etiquetas):
    training = []
    salida_vacia = [0] * len(etiquetas)
    for doc in etiquetas_relacionadas:
        bag = []
        patron_palabras = doc[0]
        patron_palabras = lemmatizar(patron_palabras)
        
        for palabra in palabras_lematizadas:
            bag.append(1) if palabra in patron_palabras else bag.append(0)

        salida = list(salida_vacia)
        salida[etiquetas.index(doc[1])] = 1

        training.append([bag, salida])

    random.shuffle(training)
    training = np.array(training)
   
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])
    return train_x,train_y

def entrenar(entrenamiento_palabras,entrenamiento_etiquetas):
  
    model = Sequential()
    model.add(Dense(128, input_shape=(len(entrenamiento_palabras[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(entrenamiento_etiquetas[0]), activation='softmax'))

    
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer=sgd, metrics=['accuracy'])

    hist = model.fit(np.array(entrenamiento_palabras), np.array(entrenamiento_etiquetas),
                     epochs=200, batch_size=5, verbose=1)
    model.save('chatbot_model.h5', hist)

    print("model created and saved")