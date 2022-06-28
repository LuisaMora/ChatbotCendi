from nlp_procesamiento import lemmatizar
import random
import numpy as np
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.models import Sequential

def procesado_datos(palabras_lematizadas,etiquetas_relacionadas, etiquetas):
    # create our training data
    training = []
    # create an empty array for our output
    output_empty = [0] * len(etiquetas)
    # training set, bag of words for each sentence
    for doc in etiquetas_relacionadas:
        # initialize our bag of words([palabras],tag )
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # lemmatize each word - create base word, in attempt to represent related words
        pattern_words = lemmatizar(pattern_words)
        # create our bag of words array with 1, if word match found in current pattern
        for palabra in palabras_lematizadas:
            bag.append(1) if palabra in pattern_words else bag.append(0)

        # output is a '0' for each tag and '1' for current tag (for each pattern)
        output_row = list(output_empty)
        output_row[etiquetas.index(doc[1])] = 1

        training.append([bag, output_row])
    # shuffle our features and turn into np.array
    random.shuffle(training)
    training = np.array(training)
    # create train and test lists. X - patterns, Y - intents
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])
    return train_x,train_y

def entrenar(entrenamiento_palabras,entrenamiento_etiquetas):
    # Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
    # equal to number of intents to predict output intent with softmax
    model = Sequential()
    model.add(Dense(128, input_shape=(len(entrenamiento_palabras[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(entrenamiento_etiquetas[0]), activation='softmax'))

    # Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer=sgd, metrics=['accuracy'])

    # fitting and saving the model
    hist = model.fit(np.array(entrenamiento_palabras), np.array(entrenamiento_etiquetas),
                     epochs=200, batch_size=5, verbose=1)
    model.save('chatbot_model.h5', hist)

    print("model created and saved")