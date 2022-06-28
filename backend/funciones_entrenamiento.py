from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras.models import Sequential
import random
import numpy as np
from nlp_procesamiento import lemmatizar

def procesado_datos(palabras_lematizadas,etiquetas_relacionadas, etiquetas):
    salidas_vacias = [0] * len(etiquetas)
    datos_de_entrenamiento = []
    for palabras_etiqueta in etiquetas_relacionadas:
        patron_palabras = palabras_etiqueta[0]
        patron_palabras = lemmatizar(patron_palabras)
        bag_pal = [ 1 if palabra in patron_palabras else 0 for palabra in palabras_lematizadas]

        bag_etiq = list(salidas_vacias)
        bag_etiq[etiquetas.index(palabras_etiqueta[1])] = 1

        datos_de_entrenamiento.append([bag_pal, bag_etiq])

    random.shuffle(datos_de_entrenamiento)
    datos_de_entrenamiento = np.array(datos_de_entrenamiento)
   
    train_x = list(datos_de_entrenamiento[:, 0])
    train_y = list(datos_de_entrenamiento[:, 1])
    return train_x,train_y

def entrenar(entrenamiento_palabras,entrenamiento_etiquetas):
  
    modelo_s = Sequential()
    modelo_s.add(Dense(128, input_shape=(len(entrenamiento_palabras[0]),), activation='relu'))
    modelo_s.add(Dropout(0.5))
    modelo_s.add(Dense(64, activation='relu'))
    modelo_s.add(Dropout(0.5))
    modelo_s.add(Dense(len(entrenamiento_etiquetas[0]), activation='softmax'))

    
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    modelo_s.compile(loss='categorical_crossentropy',
                  optimizer=sgd, metrics=['accuracy'])

    hist = modelo_s.fit(np.array(entrenamiento_palabras), np.array(entrenamiento_etiquetas),
                     epochs=200, batch_size=5, verbose=1)
    modelo_s.save('modelo_generado.h5', hist)