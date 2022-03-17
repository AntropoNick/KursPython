#Poniżej mamy listą zawierającą krotki:

data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
      ]

def make_table(number):

    for day in range(1, number + 1):
        if day < 10:
            print('0' + str(day), end='\t')
        else:
            print(str(day), end='\t')

        if day % 7 == 0:
            print()


make_table(30)




