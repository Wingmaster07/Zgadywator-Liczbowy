# Zgadywanie liczby
# wersja 1.4

import time
import sys
from random import randint
import pickle

print("Witaj w grze zgadywator liczbów")

def funkcja():
    w = pickle.load(open("wynik.pickle", "rb"))
    u = str(pickle.load(open("wynik.pickle", "rb")))
    u = u.replace("{", " ")
    u = u.replace("}", "")
    u = u.replace("(", "")
    u = u.replace(")", "")
    u = u.replace("'", "")
    u = u.replace(",", "\n")
    time.sleep(0.5)
    print("Wpisz [G] aby grać!")
    print("Wpisz [N] aby nie grać!")
    print("Wpisz [W] aby zobaczyć wyniki!")
    x = input("Twój wybór? > ")
    if x == "n":
        print("Nie to nie")
        print("Żegnam")
        time.sleep(0.5)
        sys.exit(0)

    elif x == "g":
        try:
            y = int(input("Do jakiej największej liczby chcesz grać? > "))
        except ValueError:
            print("Ty wiesz w ogóle co to liczba normalna?")
            time.sleep(0.5)
            print("Nie no odpalam od nowa bo z tobą to się nie da")
            time.sleep(0.5)
            funkcja()

        try:
            a = randint(1, y)
        except ValueError:
            print("Liczba musi być większa jak 0 no jak ty se to wyobrażasz?")
            time.sleep(0.5)
            print("Nie no od nowa odpalam")
            time.sleep(0.5)
            funkcja()

        def funkcja1():
            try:
                z = int(input("Dawaj liczbę > "))
            except ValueError:
                print("Ale ty rozumiesz co to jest liczba zwykła czy tak niezbyt?")
                print("debil")
                funkcja1()
            while a != z:
                if (z > a) and (z < y):
                    print("Za dużo")
                elif (z > a) and (z > y):
                    print(
                        "No ja nie moge jaki dekiel no skoro wybrałeś że chcesz od 1 do",
                        y,
                        "no to wiadomo że nie będzie więcej jak",
                        y,
                        "a ty uważasz że",
                        z,
                        "to więcej jak",
                        y,
                        "no myśl trochę",
                    )
                elif z < 1:
                    print(
                        "Najmniejsza liczba jaka się mogła wylosować to 1 a",
                        z,
                        "to jest mniej niż 1 no",
                    )
                elif z < a:
                    print("Za mało")
                elif (z == y) and (z != a):
                    print("Za dużo")

                try:
                    z = int(input("Dawaj liczbę ale tym razem dobrą > "))
                except ValueError:
                    print("Ale z ciebie śmieszek to liczba nie jest")
                    funkcja1()
            print("Udało ci się")
            print("Gratulacje!")
            g = input("Czy chciałbyś zapisać swój wynik? (pamiętaj że jedno imię może mieć tylko 1 wynik) t/n > ")
            if g == "t":
                i = input("W takim razie podaj swoje imię. > ")
                w[i] = y
                with open('wynik.pickle', 'wb') as f:
                    pickle.dump(w, f)
            else:
                print("To nie")
            print("Odpalam od nowa")
            time.sleep(1)
            funkcja()

    elif x == "w":
        print(u)
        funkcja()
    else:
        print("Nieprawidłowe dane wejściowe")
        time.sleep(0.5)
        print("Odpalanie od nowa")
        time.sleep(0.5)
        funkcja()
    funkcja1()


funkcja()
