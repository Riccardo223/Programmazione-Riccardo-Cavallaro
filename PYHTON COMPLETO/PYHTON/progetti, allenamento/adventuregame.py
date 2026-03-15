nome = input("inserisci il tuo nome: ")
print(f"benvenuto nella tua avventura: {nome}!")

risposte = []


while True:
  try:
    direzione = input("Sei su una strada, la strada ha un bivio, destra o sinistra, da che parte andrai? ").lower()
    direzioni_possibili = ["destra", "sinistra"]

    if direzione not in direzioni_possibili:
      print("inserisci una direzione adeguata!")
      continue
    
    elif direzione == 'destra':
      risposte.append(direzione)
      while True: 
        try:
          domanda_2 = input("C'è un fiume, vuoi attraversarlo nuotandoci, o camminargli attorno (nuotare o camminare): ")
          risposte.append(domanda_2)

            
          domanda_2possibili = ['nuotare', 'camminare']
              
          if domanda_2 not in domanda_2possibili:
                print("inserire un azione adeguata!")
                continue
          elif domanda_2 == 'camminare':
                print("\n")
                print("hai camminato per tanto tempo, hai finito le scorte di cibo e acqua, hai perso il gioco!")
                break
          elif domanda_2 == 'nuotare':
                print("\n")
                print("nuotando, sei stato mangiato da un alligatore, hai perso!")
                break
              
        except Exception as e:
          print("errore in", e)
      break
    
    elif direzione == 'sinistra':
      risposte.append(direzione)
      while True: 
        try:
          domanda_2 = input("C'è un castello, vuoi entrarci o stai alla larga dall struttura (entrare o andare via): ")
          risposte.append(domanda_2)

            
          domanda_2possibili = ['entrare', 'andare via']
              
          if domanda_2 not in domanda_2possibili:
                print("inserire un azione adeguata!")
                continue
          elif domanda_2 == 'entarare':
                print("\n")
                print("entrando il castello la servitù ti ha nominato re, hai vinto il gioco e sei ricco!")
                break
          elif domanda_2 == 'andare via':
                print("\n")
                print("lasciando perdere il castello un gruppo di banditi ti ha assaltato credendo provenissi da li, hai perso il gioco!")
                break
              
        except Exception as e:
          print("errore in", e)
      break
  except Exception as e:
    print("errore in", e)
  
print(f"\n----RIEPILOGO AVVENTURA DI {nome.upper()}----")
for i in range(len(risposte)):
  print(f"scelta {i +1}: {risposte[i]}")
print()









