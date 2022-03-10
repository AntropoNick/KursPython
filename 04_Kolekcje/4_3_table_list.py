# Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy
# w formie tabeli n x n. Elementy powinny być oddzielone spacją


n=int(input('Podaj wymiar tablicy: '))
array = [['-'] * n] * n
print(array)
print('')
for row in array:
    for col in row:
        print (col, end=" ")
    print()
array[2][1]='d'
print (array)
