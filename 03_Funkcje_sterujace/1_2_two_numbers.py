# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik,
# w przeciwnym wypadku wyświetl “Koniec”.

a = int(input("Podaj pierwsza liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if a+b>100:
    print ("Suma wynosi: ",a+b)
else:
    print ("Koniec")