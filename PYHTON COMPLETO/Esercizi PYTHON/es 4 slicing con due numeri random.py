while True:
    s = input("Inserisci una frase o scrivi 'E' per terminare il programma: ")
    if s == 'E':
        print("Ci vediamo!")
        break

    while True:
        try:
            a = int(input("Inserisci un valore per la variabile A: "))
            break
        except ValueError:
            print("Errore: devi inserire un numero intero per A, riprova!")

    while True:
        try:
            b = int(input("Inserisci un valore per la variabile b: "))

            if a < 0 or b > len(s) or a > b:
                print("Mi dispiace, i valori sembrano essere sbagliati. Riprova.")
            else:
                print("Il risultato è...", s[a:b])
            break
        except ValueError:
            print("Errore: devi inserire un numero intero per 'b', riprova!")
