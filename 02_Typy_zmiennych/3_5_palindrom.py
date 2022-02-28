# Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź
# czy wprowadzone wyrażenie jest palindromem.

str=str(input("Wprowadz tekst: "))
str_leng=len(str)
str=str.lower()
str=str.replace(' ','')
print ("Czy wprowadzone słowo jest palindoromem?", str == str[str_leng::-1])