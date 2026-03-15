#nested loop, un loop dentro ad un altro loop
def esempio():
  for y in range(3):#bisogna senpre stare attenti che i counter di for siano diversi nei 2 loop:
    for x in range(1,10):
      print(x, end="") #con end possiamo decidere come scrivere x, se sulla stessa linea, con un trattino in mezzo ai numeri, etc etc
    print()#con questo print facciamo si che i numeri dall'1 al 9 successivi vengano scritti su una nuova linea



def rettangolo():
  righe = int(input("quante righe vuoi che abbia il tuo rettangolo?: "))
  colonne = int(input("quanti colonne vuoi?: "))
  simbolo = input("che simbolo vuoi usare?: ")
  colonne += 1
  for y in range(righe):
    for x in range(colonne):
      print( simbolo, end="")
    print()
rettangolo()


