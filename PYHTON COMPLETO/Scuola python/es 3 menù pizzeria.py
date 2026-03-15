menu = """
Benvenuto alla Pizzeria!
Scegli un'opzione:
1. Visualizza il menu delle pizze
2. Ordina una pizza
3. Chiedi informazioni sugli ingredienti
4. Visualizza conto 
"""
print(menu)
scelta = input("Inserisci il numero dell'opzione: ")
if scelta == "1":
    print("Hai scelto di visualizzare il menu delle pizze.")
elif scelta == "2":
    pizze = """
            1. diavola
            2. margherita
            3. wurstel
            4. patatine
            5. quattro formaggi
            """
    print(pizze)
    tippizza= int(input("seleziona il numero di pizza che desideri "))
    if tippizza == 1:
        print("arriva subito")
        quantità= int(input("seleziona la quantità di pizze che vuoi, massimo 10 "))
        if quantità > 10:
            print("solo 10 ordinazioni")
        elif quantità == 1 or quantità <= 5:
            print("il prezzo è 20 euro")
        elif quantità == 10 or quantità <10:
            print("il presso è 40 euro")
    elif tippizza == 2:
        print("arriva subito")
        quantità= int(input("seleziona la quantità di pizze che vuoi, massimo 10 "))
        if quantità > 10:
            print("solo 10 ordinazioni")
        elif quantità == 1 or quantità <= 5:
            print("il prezzo è 20 euro")
        elif quantità == 10 or quantità <10:
            print("il presso è 40 euro")
    elif tippizza == 3:
        print("arriva subito")
        quantità= int(input("seleziona la quantità di pizze che vuoi, massimo 10 "))
        if quantità > 10:
            print("solo 10 ordinazioni")
        elif quantità == 1 or quantità <= 5:
            print("il prezzo è 20 euro")
        elif quantità == 10 or quantità <10:
            print("il presso è 40 euro")
    elif tippizza == 4:
        print("arriva subito")
        quantità= int(input("seleziona la quantità di pizze che vuoi, massimo 10 "))
        if quantità > 10:
            print("solo 10 ordinazioni")
        elif quantità == 1 or quantità <= 5:
            print("il prezzo è 20 euro")
        elif quantità == 10 or quantità <10:
            print("il presso è 40 euro")
    elif tippizza == 5:
        print("arriva subito")
        quantità= int(input("seleziona la quantità di pizze che vuoi, massimo 10 "))
        if quantità > 10:
            print("solo 10 ordinazioni")
        elif quantità == 1 or quantità <= 5:
            print("il prezzo è 20 euro")
        elif quantità == 10 or quantità <10:
            print("il presso è 40 euro")
    else:
        print("seleziona un numero da 1 a 5.")
elif scelta == "3":
    print("Hai scelto di chiedere informazioni sugli ingredienti.")
elif scelta == "4":
    print("il conto verrà portato al tavolo")
else: 
    print("selezione non valida, errore")

print("GRAZIE PER ESSERE NOSTRO CLIENTE")
