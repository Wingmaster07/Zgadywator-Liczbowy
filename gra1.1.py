# Zgadywanie liczby
# wersja 1.1

import time
import sys
from random import randint


def funkcja():
    print("Witaj w grze zgadywator liczbów")
    time.sleep(0.5)
    x = input("Czy chcesz w nią zagrać? t/n > ")
    if x == "n":
        # Zamknięcie okna gry
        print("Nie to nie")
        print("Żegnam")
        time.sleep(0.5)
        sys.exit
    elif x == "t":
        try:
            y = int(input("Do jakiej największej liczby chcesz grać? > "))
        except ValueError:
            # Jeśli największa potencjalnie wylosowana liczba nie jest liczbą
            print("Ty wiesz w ogóle co to liczba normalna?")
            time.sleep(0.5)
            print("Nie no odpalam od nowa bo z tobą to się nie da")
            time.sleep(0.5)
            funkcja()
        try:
            a = randint(1, y)
        except ValueError:
            # Jeśli największa potencjalnie wylosowana liczba jest mniejsza od 1
            print("Liczba musi być większa jak 0 no jak ty se to wyobrażasz?")
            time.sleep(0.5)
            print("Nie no od nowa odpalam")
            time.sleep(0.5)
            funkcja()

        def funkcja1():
            try:
                z = int(input("Dawaj liczbę > "))
            except ValueError:
                # Jeśli wpisana zostałą nie liczba lub ułamek
                print("Ale ty rozumiesz co to jest liczba zwykła czy tak niezbyt?")
                funkcja1()
                print("debil")
            while a != z:
                if (z > a) and (z < y):
                    # Jeśli wpisana liczba jest większa od wylosowanej
                    print("Za dużo")
                elif (z > a) and (z > y):
                    # Jeśli wpisana liczba jest większa od najwyższej potencjalnie wylosowanej
                    print(
                        "No ja nie moge jaki jakie dekiel no skoro wybrałeś że chcesz od 1 do",
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
                    # Jeśli wpisana liczba jest mniejsza niż 1
                    print(
                        "Najmniejsza liczba jaka się mogła wylosować to 1 a",
                        z,
                        "to jest mniej niż 1 no",
                    )
                else:
                    # Jeśli wpisana liczba jest mniejsza od wylosowanej
                    print("Za mało")
                try:
                    z = int(input("Dawaj liczbę ale tym razem dobrą > "))
                except ValueError:
                    # Jeśli została wpisana nie liczba lub ułamek
                    print("Ale z ciebie śmieszek to liczba nie jest")
            # Jeśli wpisana liczba równa się liczbie wylosowanej
            print("Udało ci się")
            print("Gratulacje!")
            print("Odpalam od nowa")
            time.sleep(1)
            funkcja()

    else:
        # Jeśli dane wejściowe są inne niż t lub n
        print("Nieprawidłowe dane wejściowe")
        print("Odpalanie od nowa")
        time.sleep(1)
        funkcja()
    funkcja1()


funkcja()
