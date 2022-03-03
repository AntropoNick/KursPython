# Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#
#     C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
#
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.
print ("Petla while")
fahr_temp=0
while fahr_temp<=200:
    celc_temp=round(5/9*(fahr_temp-32),2)
    print("Temp.",fahr_temp,"F odpowiada",celc_temp,"C")
    fahr_temp+=20

print ("Petla for")
for fahr_temp in range(0,201,20):
    celc_temp = round(5 / 9 * (fahr_temp - 32), 2)
    print("Temp.", fahr_temp, "F odpowiada", celc_temp, "C")
    fahr_temp += 20
