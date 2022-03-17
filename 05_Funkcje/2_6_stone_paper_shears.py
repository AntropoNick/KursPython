# Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’


import random

def choose_figure(round):
    print("\nRunda ", round + 1)
    figure = str(input("Wybierz figure: kamień (k) / papier (p) / nożyce (n): "))
    if figure != "k" and figure != "p" and figure != "n" and figure != "koniec":
        while figure != "k" or figure != "p" or figure != "n" or figure != "koniec":
            print("Podano błedną figurę")
            figure = input("Wybierz figure: kamień (k) / papier (p) / nożyce (n): ")
    return (figure)


def shears(comp_choice, figure):
    if comp_choice == 'n':
        if figure == 'p':
            comp_score += 1
            print("Przegrałeś tę rundę")
        elif figure == 'k':
            user_score += 1
            print("Wygrałes tę rundę")
        else:
            print("Remis")


def stone(comp_choice,figure):
    if comp_choice == 'k':
        if figure == 'p':
            user_score += 1
            print("Wygrałes tę rundę")
        if figure == 'n':
            comp_score += 1
            print("Przegrałeś tę rundę")
        else:
            print("Remis")


def paper(comp_choice, figure):
    if comp_choice == 'p':
        if figure == 'k':
            comp_score += 1
            print("Przegrałeś tę rundę")
        if figure == 'n':
            user_score += 1
            print("Wygrałes tę rundę")
        else:
            print("Remis")

def winner(comp_choice,figure):
    paper(comp_choice,figure)
    shears(comp_choice,figure)
    stone(comp_choice,figure)

def translate (figure):
    if figure =='n':
        return ('nożyce')
    elif figure =='k':
        return ('kamień')
    elif figure =='p':
        return ('papier')
    else:
        return ("Nieznana figura")


# ----------------------------------
# main
comp_score = 0
user_score = 0
game_choice = ["k", "p", "n"]
rund_num = int(input("Podaj liczbę rund gry: "))


for i in range(0,rund_num,1):
    comp_choice = random.choice(game_choice)
    figure =choose_figure(i)
    winner(comp_choice,figure)



    print ("Twój wybór to ",translate(figure), " komputer wylosowal",translate(comp_choice))
print ("\nGra zakończyła się wynikiem: \n- gracz:",user_score,"\n- komputer: ",comp_score)


