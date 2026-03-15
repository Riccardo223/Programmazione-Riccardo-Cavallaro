def age():
  age = int(input("dimmi quanti anni hai? (solo numeri): "))
  age_in_year = age
  age_in_month = age * 12
  age_in_day = age * 365
  
  print(f" la tua età in anni: {age_in_year}, la tua età in mesi: {age_in_month}, la tua età in giorni: {age_in_day}")


def posizione_parole():
  #stringa contenente l'alfabeto
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  #chiedo all'utente di inserire una frase 
  sentence = input("inserisci una frase: ")
  sentence_senza_spazi = sentence.replace(" ","")
  len_sentence = len(sentence_senza_spazi)#trovo la lunghezza della frase inserita
  
  #adesso chiedo all'utente di segliere un numero tra il numero della lunghezza 
  domanda = int(input(f"la lungghezza della tua frase (senza gli spazi) è di {len_sentence}, seleziona un numero tra 0 e {len_sentence}: "))
  #ora cerco la lettera la quale equivale il numero scelto dall'utente:
  index = alphabet.find(sentence[domanda])
  print(index)

posizione_parole()



 





