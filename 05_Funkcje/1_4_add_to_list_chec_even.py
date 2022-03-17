# Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów
def add_to_list (numer_of_elements):
    list=[]
    for i in range(0,numer_of_elements):
        tmp= float(input(f"Podaj element {i+1}:"))
        list.append(tmp)
    return (list)

def check_even_number(number):
    if number%2==0:
        return (1)
    else:
        return (0)


num_of_inputs = int(input("Podaj liczbe elementów listy: "))
list=add_to_list(num_of_inputs)

for number in list:
    if (check_even_number(number)):
        print (number)
