# Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
import random

def check_number(search_number, number_of_rounds):
    for index in range(0, number_of_rounds):
        user_number = int(input("Podaj liczbę: "))
        while user_number >= 100 or user_number <= 0:
            user_number = int(input("Podałeś liczbę z poza zakresu. Podaj liczbę: "))
        if user_number == number:
            print("Trafiłeś")
            break
        else:
            if user_number - number > 0:
                print("Ciepło")
            else:
                print("Zimno")
            if index == number_of_rounds - 1:
                print("Przegrales")
    print("Poszukiwna liczba to", number)


number = random.randrange(1, 100)
number_of_rounds = 6
check_number(number,number_of_rounds)
