# Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane
# przez użytkownika po przecinku. Napisz funkcję, która przyjmie
# wartości i wyświetli średnią. Program powinen być odporny na
# błędy użytkownika. Błędów nie wyświetlaj, ale rodzaj błędu
# zapisz do pliku.

numbers =str(input("Podaj liczby po przecinku: "))
numbers=numbers.strip()
list_nr= numbers.split(',')

sum=0
print (list_nr)
try:
    for number in list_nr:
        sum=sum+int(number)
    print("Wartość srednia równa się: ",sum/len(list_nr))
except Exception as err:
    with open ('Błędy.txt','w+') as fileopen:
        fileopen.write("Error: "+str(err))
