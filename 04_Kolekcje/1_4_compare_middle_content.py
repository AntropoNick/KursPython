# Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

print ("Podaj elementy")
list=[]
for index in range(0,4):
    list.append(str(input(f"Podaj {index+1} element: ")))

if list[int(len(list)/2)-1]==list[int(len(list)/2)]:
    print ("Srodkowe elementy listy sa sobie równe:" ,list[int(len(list)/2)-1],list[int(len(list)/2)])
else:
    print ("Srodkowe elementy listy nie sa sobie równe:" ,list[int(len(list)/2)-1],list[int(len(list)/2)])