# una shortcut per l'if- else
# stampa o assegna 2 valori  in base ad una condizione

#esempio:

#num = 5
#print("positivo" if num > 0 else "negativo")

# alttro essempio:

#numero = 6 
#print("pari" if numero % 2 == 0 else "negativo")


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
  time.sleep(.5)

  interesse_finale = capitale_iniziale* pow((1 + tasso/100), tempo)
  pagare = interesse_finale - capitale_iniziale

  print(f"il tuo interesse dopo {tempo} anno/i ammonta a: {interesse_finale: .2f} $")
  print(f"devi alla banca: {pagare} $")

interesse()
  