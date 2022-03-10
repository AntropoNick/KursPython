# Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Elementy na liście posortuj alfabetycznie, a następnie wyświetl.

trip_list = ["latarka","krzesiwo","namiot","karimata","nóż", "bidon"]
trip_list.sort()
print ("Spakuj:")
for element in trip_list:
    print(" - ",element)