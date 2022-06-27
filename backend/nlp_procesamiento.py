from nltk.stem import WordNetLemmatizer
from typing import List
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
# nltk.download('perluniprops')
# nltk.download('nonbreaking_prefixes')
# from nltk.tokenize.toktok import ToktokTokenizer

# toktok = ToktokTokenizer()
# sent = u"¿Quién eres tú? ¡Hola! ¿Dónde estoy?"
# toktok.tokenize(sent)
lemmatizer = WordNetLemmatizer()


def tokenizar(lista_patrones: List[str], etiqueta: str) -> List[str]:
    palabras_con_token = []
    clases = []
    documentos = []
    for pattern in lista_patrones:
        # tokenize each word
        w = nltk.word_tokenize(pattern, language="spanish")
        palabras_con_token.extend(w)
        # add documents in the corpus
        documentos.append((w, etiqueta))

        # add to our classes list
        if etiqueta not in clases:
            clases.append(etiqueta)
    return palabras_con_token, clases, documentos


def lemmatizar():
    pass
