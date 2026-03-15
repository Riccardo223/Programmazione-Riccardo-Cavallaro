def pari():
   numero_intero = 0
   while numero_intero <= 0:
      
      numero_intero = int(input("inserisci un numero intero: "))
      if numero_intero <= 0:
         print("mi dispiace non posso lavorare con questi numeri")

   print("\nNUMERI PARI:")
   for x in range(numero_intero):
      if x % 2 == 0:
         print(x)

   print("\nNUMERI DISPARI:")
   for x in range(numero_intero):
      if x % 2 == 0:
         print(x)


def dado():
   import random 
   while True:
      scelta = input("Lancia il dado! (S/N): ").upper()
      if scelta == "S":
         n1 = random.randint(1, 6)
         n2 = random.randint(1, 6)
         print(f"{n1}, {n2}")
         if n1 + n2 == 6:
            print("EVVIVA HAI VINTO!!!")
            break
      elif scelta == "N":
         print("grazie per aver giocato!")
         break
      else:
         print(f"({scelta}) non è un opzione valida!")


def numero():

   import random 
   num = random.randint(1, 100)
   while True:
      try:
         scelta = int(input("inserisci un numero tra 1 e 100: ")) 
         
         if scelta > num:
            print("troppo alto!")
         elif scelta < num:
            print("troppo basso!")
         else:
            print("HAI VINTOOO!!")
            break
         
      except ValueError:
         print(f"({scelta}) non è un numero valido")




#allenamento liste, set, tuple 

def shopping_cart():
   food = []
   price = []
   total = 0

   while True:
      try:
         food_to_buy = input("Che cibo vorresti comprare? (premi 'e' per uscire): ").lower()
         if food_to_buy == 'e':
            print("perfetto, adesso calcolo il totale!")
            break
         else:
            prezzo = float(input(f"Prezzo {food_to_buy}: $"))
            food.append(food_to_buy)
            price.append(prezzo)
      except ValueError:
         print("inserisci correttamente i valori.")
   
   print("-----il tuo carrello della spesa-----")
   print("\n")
   for x in food:
      print(f"(- {x}")
      print("\n")
   
   print("\n")
   print("-----TOTALE-----")
   for y in price:
      total += y
   print("\n")
   print(f"{total} $")



def quiz_game():
   domande = ("Qual è la capitale dell'Italia?",
              "Quanti pianeti ci sono nel nostro Sistema Solare?",
              "Quale animale è noto come 'il migliore amico dell'uomo'?",
              "In che anno è stata scoperta l'America da Cristoforo Colombo?",
              "Qual è il colore del cielo in una giornata serena?",
              "Viva la _ _ _ _"
              )
   opzioni = (("a) Milano","b) Roma", "c) Firenze", "d) Napoli"),
              ("a) Sette", "b) Otto", "c) Nove", "d) Dieci"),
              ("a) Gatto", "b) Cavallo", "c) Cane", "d) Coniglio"),
              ("a) 1492", "b) 1453", "c) 1519", "d) 1607"),
              ("a) Verde", "b) Rosso", "c) Blu", "d) Giallo"),
              ("a) Minchia", "b) Sborra", "c) Mandorla", "d) Figa "))
   
   risposte = ("b", "b", "c", "a", "c", "d")
   risposte_utente = []

   score_num = 0

   
   for numero_domande,domanda in enumerate(domande):
      print(f"----/ domanda {numero_domande +1}  /----- ")
      print(domanda)
      for option in opzioni[numero_domande]:
         print(option)
      
      while True:
         try:
            risposta = input("Scegli (a,b,c,d): ").lower()
            if risposta not in ['a', 'b', 'c', 'd',]:
                    print("Errore: inserisci solo una lettera tra a, b, c, d.")
                    continue
            risposte_utente.append(risposta)
            if risposta == risposte[numero_domande]:
               print("risposta corretta!")
               score_num += 1
            else:
               print("risposta errata!")
            break
         except Exception as e:
            print(f"Errore: {e}")
   score = int(score_num/len(domande)*100)
   print("----FINE DEL GIOCO----")
   print(f"punteggio: {score_num}/{len(domande)} ")
   print(f"punteggio in %: {score}%")


def niggers():
   import time
   nome = input("dimmi il tuo nome: ").upper()
   for x in reversed(range(11)):
      time.sleep(1)
      print(x)
   print("LEVANATANSEE")
   time.sleep(1)
   print(f"fuckk niggerzzz {nome}")
niggers()




