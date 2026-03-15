
import random
def sassocartaforbice():

  scelte_complete = { 'S': 'SASSO 🪨', 'C': 'CARTA 📃', 'F': 'FORBICE ✂️'}
  scelte = ['S', 'C', 'F']
  while True:
    scelta_utente = input("sasso, carta o forbice? (S/C/F): ").upper()
    if scelta_utente not in scelte:
      print("mi dispiace, input non valido!")
      continue

    scelta_computer = random.choice(scelte)
    print(f"la tua scelta: {scelte_complete[scelta_utente]} ")
    print(f"la scelta del computer: {scelte_complete[scelta_computer]}")

    if scelta_utente == scelta_computer:
      print("è un pareggio!")
    elif (scelta_utente == 'S' and scelta_computer == 'F') or \
      (scelta_utente == 'C' and scelta_computer == 'S') or \
      (scelta_utente == 'F' and scelta_computer == 'C'):
      print("Complimenti, hai vinto!") 
    else:
      print("hai perso!")
    
    continuare = input("vuoi giocare di nuovo? (S/N): ").upper()
    if continuare == 'N':
      print("grazie per aver giocato!")
      break





