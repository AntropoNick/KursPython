# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry,
# ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

opinion_1 = int(input("Podaj pierwszą ocenę: "))
opinion_2 = int(input("Podaj drugą ocenę: "))
opinion_3 = int(input("Podaj trzecią ocenę: "))
average = (opinion_1+opinion_2+opinion_3)/3
if average>7:
    print ("Ksiązka bardzo dobra")
elif average>=5:
    print ("Ksiązka przeciętna")
else:
    print ("Ksiązka niewarta uwagi")