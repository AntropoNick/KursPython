# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def check_in_range (number, min_range, max_range):
    if number>=min_range and number<=max_range:
        return (f"Tak, liczba {number} znajduje sie w zadanym zakresie")
    else:
        return (f"Nie, liczba {number} nie znajduje sie w zadanym zakresie")

print (check_in_range(2,1,0))