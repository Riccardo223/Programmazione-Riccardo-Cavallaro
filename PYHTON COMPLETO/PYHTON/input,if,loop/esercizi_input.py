#tutti gli esercizi sono divisi per funzioni, per utilizzarli chiamre la funzione
#input user 
def nome():
  name = input("dimmi come ti chiami: ")
  age = int(input("quanti anni hai? "))
  age = age + 1

  print(f"ciao {name}")
  print("buon compleanno!")
  print(f"adesso hai {age} anni!")


#esercizio
def area():
  import time

  lato_corto = float(input("inserisci la lunghezza del lato corto: "))

  time.sleep(1)

  print("ok grazie!")
  lato_lungo = float(input("inserisci la lunghezza del lato lungo: "))

  time.sleep(1)

  area = lato_corto * lato_lungo
  print("stiamo analizzando, attendi per 3 secondi")
  time.sleep(1)
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  print(f"ecco fatto, l'area del tuo rettangolo è: {area}")

#altro esercizio

def totale():
  import time
  oggetto = input("cosa vorresti comprare oggi? ")
  prezzo = float(input("quale è il costo dell'oggetto? "))
  quantita = float(input(f"quanti ne hai comprati di {oggetto}? "))

  totale = prezzo * quantita
  time.sleep(1)
  print("stiamo analizzando...")
  print(".")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print("...")
  print(f"in totale hai speso: {totale}")

#altro esercizio
def testo_da_riempire():
  aggettivo1 = input("inserire un aggettivo che serva per descrivere qualcosa: ")
  nome_comune1 =  input("inserisci un nome comunue (persona, animale o cosa): ")
  aggettivo2 = input("inserire un aggettivo che serva per descrivere qualcosa: ")
  verbo = input("inserisci un verbo che finisca per 'ando': ")
  aggettivo3 = input("inserire un aggettivo che serva per descrivere qualcosa:")
  print(f"oggi sono andatto in un {aggettivo1} zoo ")
  print(f"in un esibizione ho visto un {nome_comune1}")
  print(f"{nome_comune1} era {aggettivo2} e stava {verbo}")
  print(f"ero {aggettivo3}!")


#altro esercizio

def interesse():
  import time   

  capitale_iniziale = 0
  tasso = 0
  tempo = 0 

  while capitale_iniziale <= 0:
    capitale_iniziale = float(input("inserisci per favore il tuo capitale iniziale: "))
    if capitale_iniziale <= 0:
      print(f"mi dispiace ma {capitale_iniziale} è un numero uguale o minore di zero")
  
  print("perfetto attenda 1 secondo")
  time.sleep(1)
  
  while tasso <= 0:
    tasso = float(input("inserisci per favore il tasso di interesse: "))
    if tasso <= 0:
      print(f"mi dispiace ma {tasso} non è un tasso di interesse valido")

  print("perfetto attenda un istante")
  time.sleep(1.5)

  while tempo <= 0:
    tempo = int(input("inserisci per favore la durata del periodo trascorso in anni: "))
    if tempo <= 0:
      print(f"mi dispiace ma {tempo} non è un numero valido su cui lavorare")

  print("perfetto attenda ancora un attimo")
  time.sleep(1)
  print("stiamo calcolando il suo interesse!")
  time.sleep(2)
  print("perfetto, abbiamo finito!")

  interesse_finale = capitale_iniziale* pow((1 + tasso/100), tempo)

  print(f"il tuo interesse dopo {tempo} anno/i ammonta a: {interesse_finale} $")

interesse()
