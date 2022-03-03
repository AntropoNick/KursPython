# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków
# oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery
# a podmień na z i wyświetl powstały napis.

password = input("Wprowadź hasło: ")
if len(password)<=5:
    print("Błąd! Hasło za krótkie")
elif password.find('a')>0:
    new_password=password.replace("a","z")
    print(new_password)
else:
    print(password)