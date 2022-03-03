# Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random
comp_score = 0
user_score = 0
game_choice = ["k","p","n"]
rund_num = int(input("Podaj liczbę rund gry: "))
text=""
for i in range(0,rund_num,1):
    print ("\nRunda ",i+1)
    figure = str(input("Wybierz figure: kamień (k) / papier (p) / nożyce (n): "))
    if figure!="k" and figure!="p" and figure!="n" and figure!="koniec":
        while figure!="k" or figure!="p" or figure!="n" or figure!="koniec":
            print ("Podano błedną figurę")
            figure = input("Wybierz figure: kamień (k) / papier (p) / nożyce (n): ")
    comp_choice = random.choice(game_choice)

    if comp_choice=='n':
        if figure =='p':
            comp_score+=1
            text = "Przegrałeś tę rundę"
        elif figure =='k':
            user_score+=1
            text = "Wygrałes tę rundę"
        else:
            text = "remis"
    elif comp_choice=='k':
        if figure =='p':
            user_score+=1
            text = "Wygrałes tę rundę"
        if figure =='n':
            comp_score+=1
            text = "Przegrałeś tę rundę"
        else:
            text = "remis"
    elif comp_choice =='p':
        if figure =='k':
            comp_score+=1
            text = "Przegrałeś tę rundę"
        if figure =='n':
            user_score+=1
            text="Wygrałes tę rundę"
        else:
            text = "Remis"

    print ("Twój wybór to ",figure, " komputer wylosowal",comp_choice,"-",text)
print ("\nGra zakończyła się wynikiem: \n- gracz:",user_score,"\n- komputer: ",comp_score)


