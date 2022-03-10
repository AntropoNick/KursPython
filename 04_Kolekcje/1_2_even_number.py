# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
print ("Podaj 10 liczb")
number=[]
for index in range(0,10):
    number.append(int(input(f"Podaj liczbe nr {index+1}: ")))
#----------------------------------------------------------------
even_number=[]
for index in range(0,10):
    if not number[index]%2:
        even_number.append(number[index])
print (f"Użytkownik podał liczby {number}")
print (f"Liczby parzyste to {even_number}")
#----------------------------------------------------------------
even_number=[]
for one_number in number:
    if not one_number%2:
        even_number.append(one_number)
print (f"Użytkownik podał liczby {number}")
print (f"Liczby parzyste to {even_number}")