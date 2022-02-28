# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km,
# benzyny kosztuje 5,04 zł.

BurningPer100km=6.4
DistanceInKm = 120
PricePerLitr=5.04

TotalCost = round(BurningPer100km*DistanceInKm*PricePerLitr/100,2)

print ("Koszt wyprawy wynosi", TotalCost, "zł")