# Nie korzystając z funkcji wbudowanej min(), napisz funkcję
# znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

def minimum_of(a,b,c):
    if (a<b) and (a<c):
        return a
    elif (b<c) and (b<a):
        return b
    else:
        return c

print (minimum_of(1,-1,-2))