# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie
# (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 7
num=int(input("Podaj liczbę [0-20]: "))
while num!=secret_num:
    print ("Pudł0. Spróbuj ponownie.")
    num=int(input("Podaj liczbę [0-20]: "))
    if num<0 or num>20:
        print ("Podano liczbe z poza zakresu")
print ("Grtatulacje. Szukana liczba to ",secret_num)
