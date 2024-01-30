import os
import random as rand

hasla = [
    "AUDI",
    "BMW",
    "MERCEDES",
    "RENAULT",
    "HONDA",
    "NISSAN",
    "FORD",
    "HYUNDAI",
    "VOLKSWAGEN",
    "TOYOTA"
]


SZUBIENICA = ['''






''', '''






=========''', '''
  
      |
      |
      |
      |
      |
=========''', '''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def wisielec(szanse):
    os.system("cls")
    print(SZUBIENICA[szanse])


def losowanie_hasla():
    wylosowane_haslo = rand.choice(hasla)
    return wylosowane_haslo


def narysuj_haslo(haslo, znaki):
    for i in range(len(haslo)):
        if haslo[i] in znaki:
            print(haslo[i], end=" ")
        else:
            print("_", end=" ")
    print()


def main():
    wylosowane_haslo = losowanie_hasla()
    gra(wylosowane_haslo)


def gra(wylosowane_haslo):

    dlugosc = wylosowane_haslo.__len__()
    wisielec(0)
    print("Witaj w grze wisielec")
    print("Twoje haslo ma", dlugosc, "liter")
    print("Powodzenia")
    print()
    znaki = set()
    szanse = 0
    while szanse < 10:

        narysuj_haslo(wylosowane_haslo, znaki)
        print("Podaj litere:")
        litera = input().upper()
        if litera in znaki:
            print("Ta litera juz byla")
        elif litera in wylosowane_haslo:
            print("Zgadles")
            znaki.add(litera)
            if znaki == set(wylosowane_haslo):
                print("Brawo wygrales")
                break
        else:
            print("Nie zgadles")
            szanse += 1
            wisielec(szanse)
            znaki.add(litera)
