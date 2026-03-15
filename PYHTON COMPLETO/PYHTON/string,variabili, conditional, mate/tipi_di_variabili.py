#prima PAGINA DI APPUNTI PER Python
#tipi di variabili
#booleane, interi, stringhe, floater

#esempio stringa
first_name = "Riccardo"
print(first_name)

#esempio striga formattata
second_name = "Cavallaro"
print(f"ciao {second_name}")


#interi 
age = 25
quantità = 3 
print(f"tu hai {age} anni")
print(f"tu hai comprato {quantità} oggetti")


#floater 
prezzo = 10.99
prezzo_maglietta = 15.45
print(f"il prezzo è {prezzo}")
print(f"questa maglietta cosa: {prezzo_maglietta} euro")


#booleane 
#vere o false

sono_studente = True
in_vendita = False
if in_vendita and sono_studente:
  print("Questo oggetto è in vendita")
elif not in_vendita and sono_studente:
  print("hai degli sconti su altri oggetti")
else:
  print("non puoi acquistare nulla")

#output: hai degli altri sconti su altri oggetti


#TYPECASTING, convertire una variabile di un tipo ad un altro tipo
name = "Riccardo"
age = 26 
gpa = 3.9
is_student = True

gpa = int(gpa)
print(f"ecco il tuo floater convertito in un intero: {gpa}")

age = float(age)
print(f"ecco il tuo intero convertito in un floater: {age}")

name = bool(name)
print(f"ecco la tua stringa convertita in una booleana: {name}")
#questo avraò due risultati: se scriviamo qualcosa dentro alla variabile name allora l'output sarà True, se non ci scriviamo niente dentro sarà False











