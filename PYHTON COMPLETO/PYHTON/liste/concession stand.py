menu = {"pizza": 7.00,
        "popcorn": 3.00,
        "nachos": 4.50,
        "patatine": 1.25,
        "coca cola": 2.00,
        "fanta": 2.00,
        "lemon soda": 1.75,}

carrello = []
totale = 0

for key, values in menu.items():
  print(f"{key:10}: {values:.2f} €")


while True:
  try:
    food = input("seleziona un cibo o bevanda dal menu (q per uscire): ").lower()
    if food == 'q':
      print("grazie per aver acquistato!")
      break
    
    elif menu.get(food) is not None:
      carrello.append(food)
      continue

    elif menu.get(food) is None:
      print("selezionare un cibo dal menu!")
      continue
  
  except Exception as e:
    print(f"errore in {e}")


for food in carrello:
  totale += menu.get(food)
  print(F"{food},", end = " ")

print()
print(f"totale: {totale}")




