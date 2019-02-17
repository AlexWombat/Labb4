from bintreeFile import Bintree
from string import ascii_lowercase


def makechildren(startord, svenska, gamla):
    alfabet_lista = list(ascii_lowercase)
    alfabet_lista.extend(['å', 'ä', 'ö'])
    nya_ord = []
    for i in range(0, 3):
        bokstavslista = list(startord)
        for j in alfabet_lista:
            bokstavslista[i] = j
            nya_ord.append(''.join(bokstavslista))
    gamla.put(startord)
    for nytt_ord in nya_ord:
        if nytt_ord in svenska and nytt_ord not in gamla:
            gamla.put(nytt_ord)
            print(nytt_ord)


def main():
    svenska = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet not in svenska:
                svenska.put(ordet)
    gamla = Bintree()
    startord = 'söt'
    slutord = 'sur'
    makechildren(startord, svenska, gamla)


main()





