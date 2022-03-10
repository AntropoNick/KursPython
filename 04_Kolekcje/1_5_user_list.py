# Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
#     Dorota, Wellman, dziennikarka
#     Adam, Małysz, sportowiec
#     Robert, Lewandowski, piłkarz
#     Krystyna, Janda, aktorka
#
# Wyświetl w sposób przyjazny dla użytkownika

persons= [["Dorota","Adam", "Robert","Krystyna"],["Wellman","Małysz", "Lewandowski","Janda"],["dziennikarka","sportowiec","piłkarz","aktorka"]]
print (persons)

for person in persons:
    print (person)
    for user in person:
        print (user, end=(" "))
        print()