# Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie.
# Obsłuż błąd
tuple=(1,4,2,6,4,7,4,5,3,2,4,6)
index= int(input('Podaj index: '))
value=int(input('Podaj wartosc: '))
try:
    tuple[index]=value
except Exception as err:
    print ("Błąd: ",err)
