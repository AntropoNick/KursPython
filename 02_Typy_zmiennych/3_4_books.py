# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
title_book=str(input("Podaj tytuł książki: "))
book_author = str(input("Podaj nazwisko autora książki: "))
page_number = str(input("Podaj liczbę stron:"))

# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
print("Nazwa składa sie tylko z liter:", title_book.isalpha())
print("Nazwisko składa sie tylko z liter: ", book_author.isalpha())
print ("Wprowadzono porawana liczbe stron: ", page_number.isdigit())

# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
title_book=title_book.capitalize()
book_author=book_author.title()
print ("Poprawiony tytuł kiązki: ",title_book)
print ("Poprawione nazwisko autora: ",book_author)

# Połącz dane w jeden ciąg book za pomocą spacji
book = title_book + " " + book_author + " " + page_number
print ("Polaczone slowa :",book)

# Policz liczbę wszystkich znaków w napisie book
print ("Liczba znaków w napisie wynosi:" ,len(book))