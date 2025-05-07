import kagglehub
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
import spacy


path = kagglehub.dataset_download("arhamrumi/amazon-product-reviews")

df=pd.read_csv(path+"/Reviews.csv") #Carga los reviews
df=df.head(60) #Trae solo 50 revi

nlp = spacy.load("en_core_web_sm") #Se carga Spacy



sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

joined_text = "\n".join(df['Text'])

print(joined_text)

doc_sent = nlp(joined_text)
oraciones = [sent.text.strip() for sent in doc_sent.sents if sent.text.strip() != ""]

print(oraciones)

resultados = []
for idx, oracion in enumerate(oraciones):
    # Cada resultado es una lista con un diccionario, extraemos el primero
    res = sentiment_pipeline(oracion)[0]
    res["Oracion"] = oracion
    res["Indice"] = idx
    resultados.append(res)

df_sentimientos = pd.DataFrame(resultados)
print("\nResultados del análisis de sentimiento por oración:")
print(df_sentimientos)

conteo_sentimientos = df_sentimientos["label"].value_counts()
print("\nConteo de etiquetas de sentimiento:")
print(conteo_sentimientos)