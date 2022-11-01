from textblob import TextBlob 
while 1==1:
    palabraTraducir = TextBlob(input('Introduce la palabra que deseas traducir:\n '))
    idioma = input("\n¿A qué idioma deseas traducir?\n (spanish, english, german, japanese)\n")
    if idioma == "spanish":
        print("La palabra traducida en español es: ")
        print( str(palabraTraducir.translate(from_lang='en', to='es')))
    elif idioma == "english":
        print("La palabra traducida en inglés es: ")
        print( str(palabraTraducir.translate(from_lang='es', to='en')))
    elif idioma == "german":
        print("La palabra traducida en alemán es: ")
        print( str(palabraTraducir.translate(from_lang='es', to='de')))
    elif idioma == "japanese":
        print("La palabra traducida en japonés es: ")
        print( str(palabraTraducir.translate(from_lang='es', to='ja')))
    else:
        print("Lo siento, no conozco ese idioma")