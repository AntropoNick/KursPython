quote = "Honesty is the first chapter in the book of wisdom."

# Policz wszystkie znaki w napisie
print("Liczba znakow", len(quote))

# Nie modyfikując zmiennej wyświetl słowo wisdom
search ="wisdom"
WordLength = len(search)
WordBegin=quote.rfind(search)
print (quote[WordBegin:WordBegin+WordLength])

# Wyświetl tylko pierwszą połowę tekstu
FirstTextPart=int(len(quote)/2)
print(quote[0:FirstTextPart])

# Wyświetl tylko kropkę
print(quote[-1])

# Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[FirstTextPart::3])

# Wyświetl ‘Hnsyi h is hpentebofwso.’
print(quote[0::2])

# Wyświetl cały cytat odwrotnie
print(quote[(len(quote))::-1])

# Zamień wisdom na słowo friendship
print (quote.replace("wisdom", "friendship"))