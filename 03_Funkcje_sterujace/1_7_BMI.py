# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.
# 17,0 - 18,5	niedowaga
# 18,5–24,9	waga prawidłowa
# 25,0–29,9	nadwaga
weight = float(input("Podaj mase w kg: "))
height= float(input("Podaj wzrost w m: "))
BMI = round(weight/(height**2),2);
print("Twoje BMI wynosi: ",BMI)
if (BMI<18.5):
    print ("Masz niedowagę")
elif BMI>25:
    print ("Masz nadwage")
else:
    print ("Twoja waga jest prawidłowa")
