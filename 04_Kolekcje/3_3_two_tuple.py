# Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów
# o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej.
# Przekształć powstałą listę w set.

tuple1 = (0,1,2,3,4,5,6,7,8,9)
tuple2 = ('a','b','c','d','e','f')
tmp_list = list(tuple1[::2]+tuple2[1::2])
print (tmp_list)
tmp_set = set(tmp_list)
print (tmp_set)