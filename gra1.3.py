# Zgadywanie liczby
# wersja 1.3

import time
import sys
from random import randint



def funkcja():
    print("Witaj w grze zgadywator liczbów")
    time.sleep(0.5)
    x = input("Czy chcesz w nią zagrać? t/n > ")
    if x == "n":
        print("Nie to nie")
        print("Żegnam")
        time.sleep(0.5)
        sys.exit(0)

    elif x == "t":
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
                elif (z == y) and (z != a):
                    print("Za dużo")
                else:
                    print("Za mało")
                try:
                    z = int(input("Dawaj liczbę ale tym razem dobrą > "))
                except ValueError:
                    print("Ale z ciebie śmieszek to liczba nie jest")
                    funkcja1()
            print("Udało ci się")
            print("Gratulacje!")
            print("Odpalam od nowa")
            time.sleep(1)
            funkcja()

    else:
        print("Nieprawidłowe dane wejściowe")
        time.sleep(0.5)
        print("Odpalanie od nowa")
        time.sleep(0.5)
        funkcja()
    funkcja1()


funkcja()
