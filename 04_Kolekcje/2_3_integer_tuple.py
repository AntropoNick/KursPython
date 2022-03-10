# Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks.

integer = (5,7,6,3,8,1,9,3,2,0)
choice = int(input("Podaj liczbe od 0 do 9: "))
for i in range(0,len(integer)):
    if integer[i]==choice:
        break
print (f"Liczba znajduje sie na miejscu {i+1}")
