print("Benvenuto nella mia calcolatrice virtuale")
print("Ecco le figure disponibili:")
print("1) TRIANGOLO")
print("2) QUADRATO")
print("3) RETTANGOLO")

# Selezione dell'utente
ans = int(input("Seleziona il numero della figura che vuoi calcolare: "))

if ans == 1:  # Triangolo
    base = int(input("Dimmi una misura per la base: "))
    altezza = int(input("Dimmi una misura per l'altezza: "))
    if base > 100 or altezza > 100:
        print("Devi selezionare una misura uguale o minore di 100.")
    else:
        area = (base * altezza) / 2
        print("L'area del triangolo è:", area)

elif ans == 2:  # Quadrato
    lato = int(input("Dimmi una misura per il lato: "))
    if lato > 100:
        print("Devi selezionare una misura uguale o minore di 100.")
    else:
        area = lato * lato
        print("L'area del quadrato è:", area)

elif ans == 3:  # Rettangolo
    base = int(input("Dimmi una misura per la base: "))
    altezza = int(input("Dimmi una misura per l'altezza: "))
    if base > 100 or altezza > 100:
        print("Devi selezionare una misura uguale o minore di 100.")
    else:
        area = base * altezza
        print("L'area del rettangolo è:", area)

else:
    print("Opzione non valida. Seleziona un numero tra 1 e 3.")
