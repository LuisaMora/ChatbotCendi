from nltk.stem import WordNetLemmatizer
from typing import List
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()


def tokenizar(lista_patrones: List[str], etiqueta: str):
    if etiqueta:
        palabras_con_token = []
        clases = []
        documentos = []
        for pattern in lista_patrones:
            w = nltk.word_tokenize(pattern, language="spanish")
            palabras_con_token.extend(w)
            documentos.append((w, etiqueta))
            if etiqueta not in clases:
                clases.append(etiqueta)
        return palabras_con_token, clases, documentos
    return nltk.word_tokenize(lista_patrones, language="spanish")


def lemmatizar(palabras_tokenizadas):
    palabras_a_ignorar = ['?', '!']
    pal_lematizada = [lemmatizer.lemmatize(palabra.lower())
             for palabra in palabras_tokenizadas if palabra not in palabras_a_ignorar]
    return pal_lematizada
