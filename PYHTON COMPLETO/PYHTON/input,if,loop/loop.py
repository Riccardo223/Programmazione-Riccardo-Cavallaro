#while loop 
#un loop che esegue qualcosa mentre una condizione è vera

#es 
def es1():
  nome = input("inserisci il tuo nome: ")

  while nome == "":
    print("non hai inserito il tuo nome!")
    nome = input("inserisci il tuo nome: ")

  print(f"hello {nome}")


def es2():
  food = input("inserisci un cibo che ti piace (premi q per uscire): ")

  while not food == "q":
    print(f"ti piace {food}")
    food = input("inserisci un altro cibo che ti piace (premi q per uscire): ")

  print("arrivederci!")


def es3():
  numero = int(input("inserisci un numero tra 1 e 10: "))
  while numero < 1 or numero > 10:
    print(f"il numero {numero} non è valido, mi dispiace, inserisci un numero compreso tra 1 e 10")
    numero = int(input("inserisci un numero tra 1 e 10: "))
  
  print("ok grazie, ora analizzo: ")
  if numero >= 1 and numero <= 5:
    print(f"il numero {numero} è fortunato.")
  elif numero > 5 and numero <= 10:
    print(f"il numero {numero} è sfortunato. ")
  else:
    print("mi dispiace non sono riuscito ad analizzare")





#foor loop 

#esempio, contare fino a 10 

#for x in range(1, 11):
  #print(x)

#l'ultio numero che inseriamo nel range non viene contato 
#esercizio orologio
def nigga():

  import time 
  for counter in range(1,11):
    time.sleep(1)
    print(counter)
    
  print("nigger, nigger, niggersss")


#ovviamente il conteggio si puo fare anche all'incontrario 
def nigger():
  import time 
  for counter in reversed(range(1,11)):
    time.sleep(1)
    print(counter)
  
  print("fuck nigger, fuck nigger")





#esercizi

def timer():
  import time 
  tempo = int(input("Impostare il timer in secondi a: "))
  time.sleep(1)
  print(f"il tuo timer è stato impostato a: {tempo} secondi ")

  for x in range(tempo, 0, -1):
    secondi = x % 60
    minuti = int(x / 60) % 60
    ore = int(x / 3600)
    print(f"{ore:02}:{minuti:02}:{secondi:02}")
    time.sleep(1)
  print("Tempo SCADUTO!!")


