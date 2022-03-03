# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

number_1 = int(input("Podaj pierwsza liczbę: "))
number_2 = int(input("Podaj drugą liczbę: "))
number_3 = int(input("Podaj trzecią liczbę: "))

if number_1>number_2 :
    if number_1>number_3:
        print ("Liczba :",number_1," jest najwieksza")
        if number_2>number_3:
            print("Posegregowane liczby to : ",number_1,number_2,number_3)
        else:
            print("Posegregowane liczby to : ", number_1, number_3, number_2)
    else:
        print("Liczba :", number_3, " jest najwieksza")
        print("Posegregowane liczby to : ", number_3, number_1, number_2)
else:
    if number_2>number_3:
        print ("Liczba :",number_2," jest najwieksza")
        if number_1>number_3:
            print("Posegregowane liczby to : ",number_2,number_1,number_3)
        else:
            print("Posegregowane liczby to : ", number_2, number_3, number_1)
    else:
        print("Liczba :", number_3, " jest najwieksza")
        print("Posegregowane liczby to : ", number_3, number_2, number_1)