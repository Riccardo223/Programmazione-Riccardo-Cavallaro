def spiegazione():
              #index 0   #index 1  #index 2
  fruits =     ['apple', 'orange', 'banana'] #index 0
  vegetables = ['carote', 'patate', 'piselli'] #index 1
  meats =      ['pollo', 'cavallo', 'mucca'] #index 2

  groceries = [fruits, vegetables, meats ]

  #per creare una lista 2d bastra creare una lista ad una dimensione e scriverci dentro i nomi delle altre liste che abbiamo creato

  print(groceries[0])
  print()
  print(groceries[1])
  print()
  print(groceries[2])

  print()
  print(groceries[0][1])
  print()
  print(groceries[2][2])

  #altro metodo per scrivere le liste 2d

  groceries= {'uno' : ['apple', 'orange', 'banana'],
              'due' : ['carote', 'patate', 'piselli'],
              'tre' : ['pollo', 'cavallo', 'mucca']}

  parola = 'cavallo'
  for collection in groceries:
    for food in groceries[collection]:
      if parola in food:
        print(f"la parola cavallo si trova in: {collection}")
      else:
        pass




def esercizio():
  num = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
    ('*',0,'#')
  )

  for riga in num:
    for n in riga:
      print(n, end= ' ')
    print()



def lista_spesa_intelligente():

  categorie = {
    "frutta": "mela",
    "verdura": "spinaci",
    "tuberi": "patate",
  }
  spesa = []
  while True:
    oggetto= input("dimmi cosa vuoi aggiungere al tua carello della spesa (premi 'e' per uscire): ").lower()
    spesa.append(oggetto)
    if oggetto == 'e':
      print("perfetto, analizzero il tuo carello!")
      spesa.pop()
      break
  
  trovati = {}
  non_trovati = []
  
  #controlla ogni item dentro alla lista spesa
  for item in spesa:
    trovato = False #setta ogni volta trovato = False, così da iniziallizare ogni elemento
    for categoria, elementi in categorie.items(): #per ogni {"categoria": "elementi"} in categoria.items, ovvero una restituzione delle copie del dizionario iterabili da un foor loop
      if item in elementi: #se l'item che stiamo iterando corrisponde all'elemento di una certa categoria
         if categoria not in trovati: #controlliamo se la categoria è già stata realizzata nel dizionario trovati
          trovati[categoria] = [] #se non è stata già creta allora la creaiamo
         trovati[categoria].append(item) #e poi ci aggiungiamo l'item corrispondente
         trovato = True #settimao trovato = True, così da bypassare l'ultimo if
         break
    if not trovato: #se trovato = False
      non_trovati.append(item) #allaro aggiungiamo l'item nella lista dei non trovati
  
  print("------------TROVATI-------------")
  for x, y in trovati.items():
    print(f"{x}: {' -'.join(y)}") #.join serve per scrivere in modo più elegante delle variabili su una stringa ' separa '.join(x)
  print("------------NON-TROVATI-------------")
  for x in non_trovati:
    print(f"oggetti non trovati: {x}")


lista_spesa_intelligente()  



