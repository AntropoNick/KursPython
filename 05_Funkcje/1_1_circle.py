#Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
def circle_field(r):
    return(3.1415*pow(r,2))

r =float(input("Podaj promień: "))
print (circle_field(r))