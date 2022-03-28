# Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi
# podać dowolny index. Podziel 1 przez liczbę pod indexem wybranym
# przez użytkownika. Obsłuż błędy

list = [3, 'a', 'str', 54,23,'2',3,6,8,{'k',2},(4,7)]
index =int(input("Podaj index: "))
try:
    print(1/list[index])
except Exception as err:
    print ('Bład: ',err)