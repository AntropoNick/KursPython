#Stwórz listę składającą się z kilku elementów różnego typu np.
# [13, ‘string’, 2.45] itp. W pętli spróbuj wykonać dzielenie
# 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej
# okazji wydarzyć.

list=[13,'string',2.45,[],{'klucz':123}]

for i in list:
    try:
        print(10/i)
    except Exception as err:
        print(f"Bład przy dzieleniu przez '{i}':{err} ")