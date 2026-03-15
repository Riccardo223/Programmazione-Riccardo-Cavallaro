pwd = input("inserisci la tua password principale: ")

menu = """
-\-\-\-\-\-\-\-\-\-\-\-\-\-

MODALITA'
1) Inserire una nuova password
2) Entrare nella sezione password esistenti

-\-\-\-\-\-\-\-\-\-\-\-\-\-
"""
print(menu)

while True:
  try:
    mode = int(input("inserisci la modalità che preferisci: "))

    if mode == 1:
      print()
      break
    elif mode == 2:
      print()
      break
    else:
      print("errore, inserisci 1 o 2")
  
  except ValueError:
    print("errore")

