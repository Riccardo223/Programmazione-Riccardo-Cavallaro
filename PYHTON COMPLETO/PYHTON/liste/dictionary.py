#un dizionario è un collezione disposta a paia: {key:values}, i dizionari sono ordinabili e cambiabili, ma non duplicabili
#esempi

capitali= { "USA": "Washington D.C.",
           "INDIA": "New Dehli",
           "CHINA": "Beijing",
           "RUSSIA": "Mosca"}

#per prendere il valore key:
print(capitali.get('USA'))
print(capitali.get('INDIA'))

#come controllare se un valore è nel dizionario

if capitali.get("JAPAN"):
  print("true")
else:
  print("false")

#aggiungere key value:

capitali.update({"GERMANIA": "Berlino"})
print(capitali)

#per rimuovere tutto, solo un elemento o l'ultimo:
#capitali.popitem() #per rimuovere l'ultimo 
#capitali.clear() #per rimuovere tutto
#capitali.pop("CHINA") #per rimuovere un elemento che vuoi tu
#print(capitali)

#esiste un built in methods che ti permettere di prendere tutte le keys ma non le values in un dizionario:

keys = capitali.keys()
print(keys)

for key in capitali.keys():
  print(key)


#esempio
def chiavi():
  parola = input("dimmi uno stato: ").upper()

  for key in capitali.keys():
    if parola in key:
      print(capitali.get(parola))
    else:
      print(f"{parola} non si trova nel dizionario")


#ovviamente si può fare la stessa cosa con le values

value = capitali.values()
print(value)

for value in capitali.values():
  print(value)


#item

items = capitali.items()
print(items)
#per rendere meno complicato capitali.items() possiamo iterarlo con un for loop:
for values, keys in capitali.items():
  print(f"{keys}: {values}")

#esemprio
score = 0
for value in capitali.values():
  stato = input(f"Dimmi lo stato di questa capitale: {value}: ").upper()
  for key, val in capitali.items():
    if val == value and key == stato:
      score += 1

print(f"risultato = {score}/{len(capitali)}")










