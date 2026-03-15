import random 
import string

characters = ''

while True:
    try:
      lunghezza = int(input("inserisci la lunghezza della password che vuoi creare: ") )

      maiuscole = bool(int(input("1 se vuoi lettere maiuscole, 0 se non le vuoi: ")))
      if maiuscole:
        characters += string .ascii_uppercase

      minuscole = bool(int(input("1 se vuoi lettere minuscole, 0 se non le vuoi: ")))
      if minuscole:
        characters += string .ascii_lowercase

      speciali = bool(int(input("1 se vuoi caratteri speciali, 0 se non le vuoi: ")))
      if speciali:
        characters += string.punctuation
      
      break
    except ValueError:
      print("inserire solo numeri interi:")
      print("\n")

print(f"Lunghezza password: {lunghezza}")
print(f"Maisucole: {maiuscole}")
print(f"Minuscole {minuscole}")
print(f"Caratteri speciali: {speciali}")
print("\n")


password = ''.join(random.choice(list(characters)) for x in range(lunghezza))
print(f"ecco la tua password: {password}")

