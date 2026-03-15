import random

# Definizione delle liste
alfabeto = ["abcdefghijklmnopqrstuvwxyz"]
alfabeto = list(alfabeto[0])

n = ["1234567890"]
n = list(n[0])

caratteri = ["!£$%&"]
caratteri = list(caratteri[0])

# Ciclo per ottenere input validi
while True:
    try:
        lunghezza = int(input("Inserire la lunghezza della password: "))
        numero_parole = int(input("Inserire numero di lettere nella tua password: "))
        numeri = int(input("Inserire quanti numeri vuoi nella tua password: "))
        caratteri_speciali = int(input("Inserire quanti caratteri speciali nella tua password: "))
        
        # Verifica che gli input siano non negativi
        if lunghezza < 0 or numero_parole < 0 or numeri < 0 or caratteri_speciali < 0:
            print("Errore: i valori non possono essere negativi. Riprova.")
            print("\n")
            continue
        
        # Calcola il conteggio totale
        conteggio = numero_parole + numeri + caratteri_speciali
        
        # Verifica se il conteggio è uguale alla lunghezza
        if conteggio != lunghezza:
            print(f"Errore: la somma di lettere ({numero_parole}), numeri ({numeri}) e caratteri speciali ({caratteri_speciali}) è {conteggio}, ma la lunghezza deve essere {lunghezza}. Riprova.")
            print("\n")
            continue
        
        # Se il conteggio è corretto, esci dal ciclo
        break
    
    except ValueError:
        print("Errore: inserisci solo numeri interi. Riprova.")
        print("\n")

# Stampa la composizione della password
print("\n")
print(f"Password composta da: \n{lunghezza}: lunghezza totale password. \n{numero_parole}: lettere. \n{numeri}: numeri. \n{caratteri_speciali}: caratteri speciali.")

# Genera la password
password = []

# Aggiungi lettere casuali
for _ in range(numero_parole):
    password.append(random.choice(alfabeto))

# Aggiungi numeri casuali
for _ in range(numeri):
    password.append(random.choice(n))

# Aggiungi caratteri speciali casuali
for _ in range(caratteri_speciali):
    password.append(random.choice(caratteri))

# Mescola i caratteri
random.shuffle(password)

# Unisci i caratteri in una stringa
password = ''.join(password)

# Stampa la password
print(f"Ecco la tua password: {password}")