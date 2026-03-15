def shopping_list():
    n=[]
    while len(n) < 10:
        s = input(f"-aggiungi un item alla lista, puoi avere un massimo di 10 ITEM (se vuoi uscire scrivi 'exit') {len(n) + 1}/10:")
        if s == 'exit':
            print("grazie per aver usato il nostro programma")
            break

        s = s.lower()

        n.append(s)

        n= sorted(n, reverse=True)
    print("ecco la tua lista in ordine inverso, proprio come mi hai chiesto tu!")
    for item in n:
        print(f"- {item}")


def italian_verbs():
    n = []
    while len(n) < 5:
        s = input(f"- inserisci 5 verbi all'infinito (se vuoi uscire scrivi 'exit'){len(n) + 1}/5: ")
        s = s.lower()
        if s == 'exit':
            print("grazie per aver usato il nostro programma")
            break
        n.append(s)
    for item in n:
        if item[-1] == 'e' and item[-2] == 'r' and item[-3] == 'a':
            print("ecco i verbi in 'are': ", item)
        elif item[-1] == 'e' and item[-2] == 'r' and item[-3] == 'e':
            print("ecco i verbi in 'ere': ", item)
        elif item[-1] == 'e' and item[-2] == 'r' and item[-3] == 'i':
            print("ecco i verbi in 'ire': ", item)
        else:
            print("mhhh, questi non sono verbi mi dispiace: ", item)

def sorting_numbers():
    print("- Inserisci 5 numeri interi positivi, unici e diversi da zero.")

    numeri = []
    while len(numeri) < 5:
        try:
            num = int(input(f"Inserisci il numero {len(numeri) + 1}/5: "))

            if num <= 0:
                print(" Il numero deve essere positivo e diverso da zero. Riprova.")
            elif num in numeri:
                print(" Hai già inserito questo numero. Deve essere unico. Riprova.")
            else:
                numeri.append(num)
        except ValueError:
            print(" Inserisci un numero intero valido, per favore.")

    numeri_crescenti = sorted(numeri)
    numeri_decrescenti = sorted(numeri, reverse=True)

    print("fatto, attendi ancora un momento!")
    print("Numeri in ordine crescente:", numeri_crescenti)
    print("Numeri in ordine decrescente:", numeri_decrescenti)
    print("Numero maggiore:", max(numeri))
    print("Numero minore:", min(numeri))







menu="""
A - SHOPPING LIST
B - ITALIAN VERBS
C - SORTING NUMBERS
E - EXIT

"""
print(menu)
lettera=input("segli un elemento dal menu ")
lettera=lettera.upper()
if lettera == 'A':
    shopping_list()
if lettera == 'B':
    italian_verbs()
if lettera == 'C':
    sorting_numbers()
if lettera == 'E':
    print("ci vediamo presto amico mio")
    exit()


