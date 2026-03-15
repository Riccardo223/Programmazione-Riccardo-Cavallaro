def slicing():
    frase = input("-dimmi un frase per favore: ")
    frase= frase.lower()

    posizioni_dispari = frase[1::2]
    mezzo = frase[1:-1]
    ultimi_3 = frase[-3:]

    print("(- ecco le posizioni dispari:", posizioni_dispari)
    print("(- ecco la frase senza la prima e ultima posizione:", mezzo)
    print("(- ecco la frase senza le ultime tre posizioni:", ultimi_3)


def square1():

    num = [3,4,5,6,7,8]
    sqr_num = []

    for l in num:
        sqr_num.append(l**2)
    print("(- ecco i quadrati:")
    for l in sqr_num:
        print(l)

def square2():
    num = []
    sqr1_num= []
    while len(num)<6:
        numeri = int(input(f"inserisci dei numeri per favore, puoi inserirse {len(num) + 1}/6: "))
        num.append(numeri)

    for l in num:
        sqr1_num.append(l ** 2)
        print("(- ecco i quadrati:")
    for l in sqr1_num:
        print(l)

def numbers():
    numeri= []

    while True:
        num= int(input("(- inserisci dei numeri per favore, (se vuoi continuare inserisci un numero negativo): "))

        if num < 0:
            print("ok si comincia")
            break
        numeri.append(num)
    numeri_divisi_5= []
    for l in  numeri:
        if l%5 == 0:
            numeri_divisi_5.append(l)


    if len(numeri_divisi_5)>0:
        print("(- ecco i numeri multipli di 5:", numeri_divisi_5)
    else:
        print("(- nessun numero multiplo di 5 è stato inserito:")


def string_processor():

        parole_input = input("Inserisci una sequenza di parole separate da spazi: ")
        parole = parole_input.split()

        parole_lunghe = []
        for parola in parole:
            if len(parola) > 4:
                parole_lunghe.append(parola)

        if parole_lunghe:
            print("Parole con più di 4 caratteri:", parole_lunghe)
        else:
            print("Non ci sono parole con più di 4 caratteri.")

menu="""
A - slicing
B - square1
C - square2
D - numbers
E - string processor
F - exit

"""
print(menu)
lettera=input("segli un elemento dal menu ")
lettera=lettera.upper()
if lettera == 'A':
    slicing()
if lettera == 'B':
    square1()
if lettera == 'C':
    square2()
if lettera == 'D':
    numbers()
if lettera == 'E':
    string_processor()
if lettera == 'F':
    print("ci vediamo presto amico mio")
    exit()
