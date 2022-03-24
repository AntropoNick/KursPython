# Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków
# składające się z jedynie z cyfr od 0-9. Upewnij się, że conajmniej 2 takie
# same znaki znajdą się w sekwencji.
import random
def digit_sequence():
    nr_char = int(input("Podaj liczbę znaków: "))
    text = ''
    for i in range (0,nr_char):
        text=text+str(random.randrange(0,9,1))
    print("Wygenerowany ciąg ma postać: ", text)
    return(text)
    result=seria.series(text)
    if result[1]>=2:
        print (f"W ciągu występuje seria następujących po sobie conajmniej dwóch cyfr, tj. cyfra '{result[0]}' występuje {result[1]} razy")
    else:
        print ("Brak w ciągu serii conajmniej 2 cyfr")


# Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np.
# użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
def own_text():
    nr_char = int(input("Podaj liczbę znaków: "))
    text = ''
    for i in range(0, nr_char):
        text = text + str(input('Podaj znak: '))
    print("Wygenerowany ciąg ma postać: ", text)
    return(text)
