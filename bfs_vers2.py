from bintreeFile import Bintree
from string import ascii_lowercase
from linkedQFile import LinkedQ


def makechildren(nod, slutord, svenska, q, gamla):
    alfabet_lista = list(ascii_lowercase)
    alfabet_lista.extend(['å', 'ä', 'ö'])
    nya_ord = []
    gamla.put(nod)        # stoppar in noeden som dumbarn
    for i in range(0, 3):
        bokstavslista = list(nod)       # skapa en lista av ordet där varje element är en bokstav
        for j in alfabet_lista:
            bokstavslista[i] = j        # en bokstav byts ut i taget
            nya_ord.append(''.join(bokstavslista))
    for i in nya_ord:
        if i in svenska and i not in gamla:
            if i == slutord:
                return True
            else:
                gamla.put(i)
                q.enqueue(i)


def main():
    svenska = Bintree()
    gamla = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet not in svenska:
                svenska.put(ordet)
    startord = input('Ange ett startord: ')
    slutord = input('Ange ett slutord: ')
    q = LinkedQ()
    q.enqueue(startord)
    kedja = None
    while not q.isEmpty():
        nod = q.dequeue()
        kedja = makechildren(nod, slutord, svenska, q, gamla)
        if kedja is not None:
            break
    if kedja is None:
        print('Det finns ingen väg')
    else:
        print('Det finns en väg från', startord, 'till', slutord)


main()
