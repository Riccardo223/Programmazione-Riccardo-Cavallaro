numero= int(input("seleziona un numero intero"))
incremento = int(input("seleziona un'altro numero da aggiungere, sempre intero"))

numero += incremento

print("ecco il valore aggiornato", numero)
if numero % 2 == 0:
    print("il tuo numero è pari")
else:
    print("il tuo numero è dispari")
