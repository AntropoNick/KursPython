while True:
    try:
        age = int(input("Podaj wiek: "))
        print("Wiek", age)
        break
    except ValueError:
        print ("Zła wartość")



