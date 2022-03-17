#Napisać funkcję, która sprawdza czy liczba jest parzysta.
def check_even_number(number):
    if number%2==0:
        return ("Liczba parzysta")
    else:
        return ("Liczba nieparzysta")

num=float(input("Podaj liczba: "))
print (check_even_number(num))