from textblob import TextBlob

def analisar_sentimento(texto):
    analise = TextBlob(texto)
    sentimento = analise.sentiment.polarity  # Varia de -1 (negativo) a 1 (positivo)

    if sentimento > 0:
        return "Sentimento Positivo 😊"
    elif sentimento < 0:
        return "Sentimento Negativo 😡"
    else:
        return "Sentimento Neutro 😐"

# Teste
texto = input("Digite um texto: ")
print(analisar_sentimento(texto))
