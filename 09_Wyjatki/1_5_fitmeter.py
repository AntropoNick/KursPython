# Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py.
# Zaimportuj module do pliku fitmeter.py. Nowy plik będzie informował
# użytkownika o jego aktualnym BMI i na podstawie wyniku (niedowaga,
# nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.

import BMI

def read_file(name):
    with open (name,'r',encoding='utf8') as fopen:
        return(fopen.readline())

def choose_file(BMI_result):
    if BMI_result == 'niedowaga':
        print(read_file('niedowaga.txt'))
    elif BMI_result == 'nadwaga':
        print(read_file('nadwaga.txt'))
    elif BMI_result == 'otyłość':
        print(read_file('otyłość.txt'))
    else:
        print(read_file('normalna.txt'))

weight = float(input("Podaj mase w kg: "))
height = float(input("Podaj wzrost w m: "))

choose_file(BMI.calc_BMI(weight,height))
