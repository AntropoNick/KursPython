# Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi
# na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def calc_BMI(weight, height):
    BMI_result = round(weight / (height ** 2), 2)

    if BMI_result<18.5:
        return ("niedowaga")
    elif BMI_result>25 and BMI_result<30:
        return ("nadwaga")
    elif BMI_result >= 30:
        return ("otyłość")
    else:
        return ("waga normalna")