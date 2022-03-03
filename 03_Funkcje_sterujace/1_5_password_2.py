# Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input("Wprowadź hasło: ")
if len(password)<8:
    print("Błąd! Hasło za krótkie")
elif password.islower():
   print ("Błąd! Hasło nie zawiera duzych liter")
elif password.isupper():
   print("Błąd! Hasło nie zawiera małych liter")
elif (password.isalpha() or password.isdigit()):
   print("Błąd! Hasło nie zawiera cyfy i litery")
else:
    print("Jest ok")