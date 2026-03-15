#age = int(input("quanti anni hai? "))
#if age >= 100:
  #print("ciaoo vecchietto!")
#elif age >= 18:
  # print("perfetto, puoi accedere")
#elif age <= 0:
 # print("hahah, non sei ancora nato!")
#else:
 # print("mi dispiace, non puoi accedere!")

#bisogna prestare attenzione all'ordine in cui si mettono le condizioni


# if statement con dati booleani

#in_vendita = True 

#if in_vendita:
 # print("quest'oggetto è in vendita")
#else:
  #print("quest'oggetto non è in vendita! ")

# operatori logici:
#or: almeno una condizione deve essere vera:
# and: entrambe le condizioni devono essere vere:
# not: inverte le condizioni, es/ not False, not True


#esercizio, matematica calcolatrice:
def calcolatrice():
  import time
  operazione = input("inserisci l'operazione che vuoi eseguire (+, -,  /, *): ")
  print("ok, si comincia!")
  time.sleep(1)
  numero1 = float(input("inserisci il primo numero: "))
  numero2 = float(input("inserisci il secondo numero: "))
  print("ok, stiamo analizzando!")
  print("__25%__")
  time.sleep(1)
  print("__50%__")
  time.sleep(1)
  print("__75%__")
  time.sleep(1)
  print("__100%__")

  if operazione == '+':
    print(f"Risultato: {numero1 + numero2} ")
  elif operazione == '-':
    print(f"Risultato: {numero1 - numero2}")
  elif operazione == '/':
    print(f"Risultato: {numero1 / numero2}")
  elif operazione == '*':
    print(f"Risultato: {numero1 * numero2}")
  else:
    print(f"{operazione}, non esiste, mi dispiace.")
 


def convertitore_pesi():
  import time
  peso = float(input("inserisci il tuo peso: "))
  unità = input("in che unità hai misurato il tuo peso, chilogrammi o pound? (K / L): ")
  unità = unità.upper()
  
  print("ok, stiamo analizzando!")
  print("--> 25% <--")
  time.sleep(1)
  print("--> 50% <--")
  time.sleep(1)
  print("--> 75% <--")
  time.sleep(1)
  print("--> 100% <--")

  if unità == 'K':
    peso = peso * 2.205
    unità = "lb"
    print(f"il tuo peso è di: {peso} {unità} .")
  elif unità == 'L':
    peso  = peso / 2.205
    unità = "kg"
    print(f"il tuo peso è di: {peso} {unità} .")
  else: 
    print(f"{unità}? non ho mai sentito parlare di questa unità di misura, mi dispiace.")



def convertitore_temperature():
  import time 
  unità = input("la temperatura misurata è in celsius o fahrenheit? (C / F): ")
  unità = unità.upper()
  time.sleep(1)
  print("perfetto! Un ultima domanda:")
  time.sleep(0.5)
  temperatura = float(input("inserisci il valore della temperatura: "))
  time.sleep(1)
  print("Perfetto, analizzazione in corso")
  time.sleep(2.5)
  
  if unità == 'C':
    temperatura = round((9 * temperatura) / 5 + 32, 1)
    unità = "F"
    print(f"la temperatura in fahreinheit è di: {temperatura} {unità}")
  elif unità == 'F':
    temperatura = round((temperatura - 32) * 5 / 9, 1)
    unità = 'C'
    print(f"la temperatura in celsius è di: {temperatura} {unità}")
  else:
    print(f"{unità} non rientra nelle unità di misura conosciute.")
convertitore_temperature()