# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

text = "The Zen of Python, by Tim Peters \n\
Beautiful is better than ugly\n\
Explicit is better than implicit.\n\
Simple is better than complex.\n\
Complex is better than complicated.\n\
Flat is better than nested.\n\
Sparse is better than dense.\n\
Readability counts.\n\
Special cases aren't special enough to break the rules.\n\
Although practicality beats purity.\n\
Errors should never pass silently.\n\
Unless explicitly silenced.\n\
In the face of ambiguity, refuse the temptation to guess.\n\
There should be one-- and preferably only one --obvious way to do it.\n\
Although that way may not be obvious at first unless you're Dutch.\n\
Now is better than never.\n\
Although never is often better than *right* now.\n\
If the implementation is hard to explain, it's a bad idea.\n\
If the implementation is easy to explain, it may be a good idea.\n\
Namespaces are one honking great idea -- let's do more of those!"

# Policz liczbę wystąpień słowa better.
print("Liczba słów \'better\' w ekscie wynosi", text.count('better'))
print ("\n")
# Usuń z tekstu symbol gwiazdki
print (text.replace ("*",""))
print ("\n")
#Zamień jedno wystąpienie explain na understand
print (text.replace ("explain","understans",1))
print ("\n")
# Usuń spacje i połącz wszystkie słowa myślnikiem
print (text.replace (" ","-"))
print ("\n")

# Podziel tekst na osobne zdania za pomocą kropki
text=text.replace ("\n",". ")
print (text.replace ("..","."))
print ("\n")