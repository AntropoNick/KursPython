# Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
suma = 0
text =""
for i in range(1,11,1):
    suma=suma+i
    text = text+" "+str(i)
    print ("Suma liczb(y)" ,text, "wynosi: ",suma)