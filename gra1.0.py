# Zgadywanie liczby
# wersja 1.0
import time
import sys
from random import randint
def funkcja():
    print("Witaj w grze zgadywator liczbów")
    time.sleep(2)
    x = input("Czy chcesz w nią zagrać? t/n ")
    if x == "n":
        print("Nie to nie")
        print("Żegnam")
        time.sleep(1)
        sys.exit
    elif x == "t":
        y = int(input("Do jakiej największej liczby chcesz grać? "))
        a = randint(1, y)
        z = int(input("Dawaj liczbę "))
        while a != z:
            if z > a:
                print("Za dużo")
            else:
                print("Za mało")
            z = int(input("Dawaj liczbę ale tym razem dobrą "))
        print("Udało ci się")
        print("Gratulacje!")
        time.sleep(1)
        funkcja()
    else:
        print("Nieprawidłowe dane wejściowe")
        print("Autodestrukcja za 3 sekundy")
        time.sleep(3)
        sys.exit

funkcja()
