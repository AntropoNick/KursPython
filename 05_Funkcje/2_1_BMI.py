# Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi
# na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def BMI(weight, height):
    BMI_result = round(weight / (height ** 2), 2)

    if (BMI_result<18.5):
        return ("Masz niedowagę")
    elif BMI_result>25:
        return ("Masz nadwage")
    else:
        return ("Twoja waga jest prawidłowa")

weight = float(input("Podaj mase w kg: "))
height = float(input("Podaj wzrost w m: "))
print (BMI(weight,height))