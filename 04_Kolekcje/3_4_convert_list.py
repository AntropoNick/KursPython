# Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
#
#     input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
#
#     output:
#
#     [4, 3, 2, 1]
#     [14, 13, 12, 11]
#     [24, 23, 22, 21]

list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
print(list)

list1=list[3::-1]
list2=list[7:3:-1]
list3=list[11:7:-1]


print (list1)
print (list2)
print (list3)