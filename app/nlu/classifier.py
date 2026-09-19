import csv

from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


DATASET_PATH = Path("data/intents.csv")


def carregar_dataset():

    textos = []
    intents = []

    with open(DATASET_PATH, "r", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            textos.append(linha["texto"])
            intents.append(linha["intent"])

    return textos, intents


def treinar_modelo():

    textos, intents = carregar_dataset()

    vectorizer = TfidfVectorizer(
        lowercase=True
    )

    X = vectorizer.fit_transform(textos)

    modelo = LogisticRegression(
        max_iter=1000
    )

    modelo.fit(X, intents)

    return vectorizer, modelo


vectorizer, modelo = treinar_modelo()


def classificar_intent(texto: str):

    X = vectorizer.transform([texto])

    intent = modelo.predict(X)[0]

    probabilidades = modelo.predict_proba(X)[0]

    confianca = max(probabilidades)

    return intent, confianca