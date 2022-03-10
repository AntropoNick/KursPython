# Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
# Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie
# np. “Mój pies, rasy border collie wabi się Dyzio”.

dog = ("suczka","kundel","Misia")
(male,race,name)=dog

print ("Moja ",male,", rasy",race,"wabi sie",name);
print (f"Moja {male} rasy {race} wabi sie {name}")