#creare una lista con delle parole a caso
#il computer sceglie una parola a caso dalla lista 
#il player ha 5 tentativi per indovinare la parola del giorno

import requests
import random

# Chiama l'API per una parola casuale
lista_parole = [
    'casa',    # 4 
    'libro',   # 5
    'sole',    # 4
    'mare',    # 4
    'fiore',   # 5
    'notte',   # 5
    'albero',  # 6
    'cane',    # 4
    'gatto',   # 5
    'fiume',   # 5
    'monti',   # 5
    'stella',  # 6
    'porta',   # 5
    'luna',    # 4
    'vento'    # 5
    ]

try:
  scelta_ai = ''
  while True:
    response = requests.get('https://random-word-api.herokuapp.com/word?')#entra nel server, prendendo una risposta
    scelta_ai = response.json()[0] # Prende la prima (e unica) parola dalla risposta
    if len(scelta_ai) <= 6:
      scelta_ai = scelta_ai.lower() # La rende tutta minuscola, come nel tuo codice
      break
    else:
      pass
except:
    print("Ops, problema con internet o API. Prenderò una parola a caso manualmente")
    scelta_ai = random.choice(lista_parole)  # Backup se l'API non funziona

tentativi = 0 #numero di tentativi di partenze 
tenativi_massimi = 5 #numero di tentativi massimi


while tentativi < tenativi_massimi:
  print(f"lunghezza parola scelta = {len(scelta_ai)}.") #printa la lunghezza della parola scelta dall'ai
  
  utente = input(f"\nScegli una parola in {tenativi_massimi}. \nTentivo: {tentativi + 1}/{tenativi_massimi}: ") #input dell'utente

  rimanenti = [] #lista per la seconda passatta del ciclo for, per i caratteri rimanenti delle parole
  parola = list(scelta_ai)  #divide la parola scelta dall'ai in caratterri, salvando in parola

  if utente == scelta_ai: 
    print("Complimenti, hai vinto!!") #se l'utente indovina la parola viene printato un messaggio di vittoria
    break
  
  if len(utente) != len(scelta_ai): #se la lunghezza della parola dell'utente supera quella dell'ai, allora printa un messaggio e fa ripartire il loop
    print("\nla lunghezza della parola deve essere uguale alla lunghezza della parola scelta dall'AI")
  else:
    utente = utente.lower().strip() #formatta la parola dell'utente in minuscolo e la divide in caratteri
    for char in range(len(scelta_ai)): #controlla ogni carattere con ogni carattere della parola scelta dall'ai
      if utente[char] == scelta_ai[char]: #se il carattere dell'utente è uguale a quello dell'ai:
        rimanenti.append('✓') #allora il carattere è quello e si trova al posto giusto
        parola[char] = None #cancella quel carattere dalla lista
      else:
        rimanenti.append('F') #i caratteri rimanenti li cataloga per la seconda passata
    
    for char in range(len(scelta_ai)):
      if rimanenti[char] == 'F': 
        if utente[char] in parola: #se i caratteri rimanenti si trovano nella lista
          rimanenti[char] = "•" #allora cataloga i caratteri giusti ma nella posizione sbagliata
          posizione = parola.index(utente[char]) #dopo trova il carattere nella lista 
          parola[char] = None #e lo elimina
        else:
          rimanenti[char] = '✗' #se invece il carattere è sbagliato completamente, mette una x
  
  #print delle parole e dei pallini 
  print(f"Parola: {utente}") 
  print(f"\nRisultato: {" ".join(rimanenti)}")

  #spiegazioni dei caratteri
  print("\n✓: carattere presente ed al posto giusto")
  print("•: carattere presente ma al posto sbagliato")
  print("✗: carattere non presente")
  
  #aggiunge un tentativo alla fine del loop
  tentativi +=1

#esce dal loop se hai esaurito i tentivi e se non hai indovinato la parola
if tentativi == tenativi_massimi and utente != scelta_ai:
  print("\nmi dispiace, hai perso")
  print(f"la parola era: {scelta_ai}")








    




