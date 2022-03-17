# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def add_to_list (numer_of_elements):
    list=[]
    for i in range(0,numer_of_elements):
        tmp= float(input(f"Podaj element {i+1}:"))
        list.append(tmp)
    return (sum(list))

num_of_inputs = int(input("Podaj liczbe elementów listy:"))
print(f"Suma elementów wynosi {add_to_list(num_of_inputs)}")
        