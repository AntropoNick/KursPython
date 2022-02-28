# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć
# łańcuch złożony z trzech środkowych znaków danego ciągu.

str = "kontrybucja"
middle = int(len(str)/2)
left_side = middle-1
right_side = middle+2
print (str[left_side:right_side])

# Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
# utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = "Boolek"
s2 = "Lolek"

print (s1[0:int(len(s1)/2)]+s2+s1[int(len(s1)/2):])