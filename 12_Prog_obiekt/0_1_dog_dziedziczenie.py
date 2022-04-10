# Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
#         atrybuty: imię, kolor sierści, rasę
#         metody: szczekaj, machaj ogonem
class Animal ():
    def __init__(self):
        print("I'm animal")
    def give_sound(self):
        print ("roar!")

class Wolf(Animal):
    paw=4
    def __init__(self):
        print ("I'm wolf")
    def show_desc(self):
        print("opis wolfa")

class Dog (Wolf):
    def __init__(self,imie,kolor_siersci,rasa):
        self.imie = imie
        self.kolor_siersci = kolor_siersci
        self.rasa=rasa
    def szczekaj(self, sound='bu!'):
        return ("Hau Hau "+ sound)
    def machaj_ogonem(self):
        return("Macha, ogonem")
    def show_desc(self):
        super().show_desc()
        super().__init__()
        print("opis psa")

pies_1=Dog("Reksio","popielaty","kundelek")
pies_2=Dog('Szarik','szary','owczarek niemiecki')
wolf_obj=Wolf()
print(wolf_obj.paw)
print (pies_2.paw)
print(pies_1.szczekaj())
print(pies_2.rasa)

pies_2.show_desc()
pies_1.give_sound()