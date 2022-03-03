# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).
result=1
text="1"
silnia = int(input("Podaj liczbe w zakresie 1-8: "))
if silnia>8:
    print ("Bład! Za duza wartość")
else:
    for i in range(1,silnia,1):
        result=result*(i+1)
        text=text+"*"+str(i+1)
print("Silnia liczby podanej liczby tj.",silnia,"!=",text,"=",result)
