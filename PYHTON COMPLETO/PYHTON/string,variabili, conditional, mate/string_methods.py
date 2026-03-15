#string methods esempio:

#name = input("dimmi il tuo nome completo: ")
#ecco i metodi 
#len ti permette di contare la lunghezza di ogni stringa:
#risultato = len(name)

#con .find possiamo trovare in una stringa la prima apparizione carattere che vogliamo:
#risultato = name.find(" ")

#se invece vogliamo l'ultima apparizione facciamo cosi:
#risultato = name.rfind("o")

#con .capitalize rendiamo maiuscola la prima lettera di una stringa:
#risultato = name.capitalize()
#con upper rendiamo tutta la stringa maiuscola
#risultato = name.upper()
# con lower invece tutta maiuscola 
#risulato = name.lower()

#con isdigit, restituendoci una booleana possiamo capire se la nostra stringa è formata da solo digite (numeri)
#risultato = name.isdigit()
# con isalpha l'incontrario, questo metodo però tiene conto degli spazi e non gli canta come caraterri 
#risultato = name.isalpha()

#con count possiamo contare quante volte un carattere numero o simbolo compare in una stringa 
#risultato = name.count("o")

#con replace possiamo sostituire qualsiasi carattare con un altro 

#risultato = name.replace("c", "@")

#con help possiamo conoscere ogni metodo utilizzabile su una stringa 

#risultato = help(str)

#print(risultato) 



#alcuni esercizi

def username():
  nome = """
    Per inserire uno username valido dovrai seguire queste regole:
    --------------------------------
    ( lo username non può essere più lungo di 12 caratteri. 
    ( lo username non può contenere numeri. 
    ( lo username non può contenere spazi.
    --------------------------------
  """
  print(nome)
  username = input("inserisce il tuo username: ")

  if len(username) > 12:
    print(f"mi dispiace, ma lo username: {username} ha più di 12 caratteri")
  elif not username.isalpha():
    print(f"mi dispiace, ma lo username: {username} contiene dei numeri ")
  elif not username.find(" ") == -1:
    print(f"mi dispiace, ma lo username: {username} contiene spazi")
  else:
    print(f"benvenuto, {username}")


#indentazione 
#possiamo accedere agli elementi di una sequenza, come i caratteri di una stringa, usando [].
#esempio

#credit_number = "323-345-83274-93784"
#print(credit_number[0])

#grazie alle parentesi quare possiamo selezionare anche più elementi assieme, definendo un range, seguendo questo schema
#[start : end : step]

#print(credit_number[0 : 3]) 
#print(credit_number[4: 7])
#print(credit_number[4:])

#con step possiamo selezionare gli elementi basandoci su uno schema
#per esempio:

#print(credit_number[:: 2])

#scrivendo così verranno selezionate la prima digita e poi avanti cosi di 2 a 2.


#alcuni esercizi 
#selezionare solo le ultime 4 digite di un codice bancario

def codice_bancario():
  codice = "1234-4569-3409-8371"
  ultime_cifre = codice[-4:]
  print(f"XXXX-XXXX-XXXX-{ultime_cifre}")

#con step -1 la nostra stringa verrà girata al contrario 

def stringa_girata():
   codice = "1234-4569-3409-8371"
   codice_contrario = codice[:: -1]
   print(f"ecco il tuo codice al contrario {codice_contrario}")



def esercizio():
  numeri = []
  
  while len(numeri) <= 5:
    domanda = float(input("inserisci dei numeri: "))
    numeri.append(domanda)
  numeri_contrario = numeri[:: -1]
  print(f"ecco i tuoi numeri al contrario: {numeri_contrario}")


#format specifiers 
#permettono di formattare una varibile mostrata come volgiamo noi 

#es
#possiamo formattare dei numeri floater a due cifre dopo la virgola in questo modo

prezzo1 = 3.1245
prezzo2 = -987.52425
prezzo3 = 12.34

print(f"valore prezzo 1: {prezzo1: .2f} ")
print(f"valore prezzo 2: {prezzo2: .2f} ")
print(f"valore prezzo 3: {prezzo3: .2f} ")

#es
#possiamo anche aggiungere spazio per scrivere la nostra varibile:

prezzo1 = 3.1245
prezzo2 = -987.52425
prezzo3 = 12.34

print(f"valore prezzo 1: {prezzo1: 10} ")
print(f"valore prezzo 2: {prezzo2: 10} ")
print(f"valore prezzo 3: {prezzo3: 10} ")

#con :< e :>  possiamo aggiustare il posizionamento della varibile a destra o sinistra 
# con :^ aggiustiamo al centro 
# con :+ possiamo mettere un segno più davanti ad ogni numero positivo e davanti ai numeri negativi verranno messi i segni meno 
# con :, mettiamo una virgola ai numeri che contengo le migliaia
#ovviamente possiamo anche mescolare tutti questi built in methods 




 