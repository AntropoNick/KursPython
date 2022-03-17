books={}

def add_book ():
    title=str(input("Podaj tytuł: "))
    rate= int(input("Podaj ocenę (1-10): "))
    dict_book={title:rate}
    books[title]=rate
    #return dict_book
    return books

for i in range (3):
    add_book()

print (books)

def show_book(title):
    print(f"Ksiązka {title} ma ocenę {books[title]}")

while (True):
    given_title =input("Podaj tytuł do sprawdzenia oceny: ")
    if given_title in books.keys():
        break
    print ("Takiego tytułu nie ma"
           )
show_book(given_title)