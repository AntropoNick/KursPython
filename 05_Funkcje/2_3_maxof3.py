# Nie korzystając z funkcji wbudowanej max(),
# napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def maxof(a,b,c):
    if (a>b)and (a>c):
        return a
    elif (b>a)and (b>c):
        return b
    else:
        return c

def max_of(a, b, c):
    max_value = a
    if max_value > b:
        max_value = b
    if max_value > c:
        max_value = c
    return max_value

3
a= int(input ("Podaj a: "))
b= int(input ("Podaj b: "))
c= int(input ("Podaj c: "))
print (maxof(a,b,c))
print (max_of(a,b,c))