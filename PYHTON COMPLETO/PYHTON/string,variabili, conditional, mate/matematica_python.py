#esempio di addizione 
#amici = 5

#amici = amici + 1 
#possiamo accorciare la stringa 3 così:
#amici += 1 
#la stessa cosa varra se vogliamo fare una sottrazione
#amici -= 3
#amici = amici * 3
#amici*= 3
#amici = amici / 2
#amici /= 2

#potenze
#amici = amici**2
#amici **= 2

#divisoni con il resto
#resto = amici % 2

#print(amici)



#alcuni metodi matematici built-in:

#x= 3.14
#y= 4
#z= 5.67

#arrotonda il numero al suo intero più vicino
#result= round(z)
# con 'absolute' troviamo la distanza di un numero dallo zero
#result = abs(y)
# con power possiamo aggiungere una potenza ad una base che vogliamo 
#result = pow(y, 3)
# con maximun possiamo trovare il valore massimo tra alcuni valori, come in una lista o tra elementi
#result = max(x, y, z)
#ovviamente anche il minimo
#result = min(x, y, z)
#print(result)




#importando il modulo 'math' abbiamo altri metodi built in utili per svolgere operazioni di calibro più grande

#import math

#x = 9.9

#print(math.pi)
#print(math.e)
#square = math.sqrt(x)
#con ceil ogni numero numero floater inserito verra arrotondato per eccesso
#up = math.ceil(x)
#il contrario con floor
#down = math.floor(x)

#print(square)
#print(up)
#print(down)


#esercizi

def circonferenza():
  import math
  import time
  #chiediamo il numero 
  raggio = float(input("Dimmi un numero per il raggio per favore (numero positivo): "))
  #calcoliamo la circonferenza
  circonferenza = 2 * math.pi * raggio
  
  print("perfetto grazie!")
  print("stiamo analizzando")
  
  time.sleep(1)
  print(".")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print("...")

  #stampiamo tutto
  menu = """
  come vuoi la tua circonferenza?
  1) arrotondata
  2) non-arrotondata
""" 
  print(menu)
  scelta = input("come vorresti la tua circonferenza? (digita un numero) ")
  
  print("ottimo!! Stiamo analizzando la tua scelta!")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print("...")

  if scelta == '1':
    print(f"ecco il valore della circonferenza arrotondata: {round(circonferenza)}")
  elif scelta == '2':
    print(f"ecco la tua circonferenza non arrotondata: {circonferenza}")


#altro esercizio

def area():
  import math
  import time 
  raggio = float(input("Dimmi un numero per il raggio per favore (numero positivo): "))
  area = math.pi * (raggio**2)

  print("perfetto grazie!")
  print("stiamo analizzando")
  
  time.sleep(1)
  print(".")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print("...")

  #stampiamo tutto
  menu = """
  come vuoi la tua area?
  1) arrotondata
  2) non-arrotondata
""" 
  print(menu)
  scelta = input("come vorresti la tua area? (digita un numero) ")
  
  print("ottimo!! Stiamo analizzando la tua scelta!")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print("..")
  time.sleep(1)
  print("...")

  if scelta == '1':
    print(f"ecco il valore del'area arrotondata: {round(area, 2)}")
  elif scelta == '2':
    print(f"ecco la tua circonferenza non arrotondata: {area}")

#altro esercizio

def ipotenusa():
  import math 
  import time
  a = float(input("inserire lunghezza lato A: "))
  b = float(input("inserire lunghezza lato B: "))
  c = math.sqrt(pow(a, 2) + pow(b, 2))
  time.sleep(1)
  print("perfetto, stiamo calcolando!")
  time.sleep(1)
  print("_25%_")
  time.sleep(1)
  print("_50%_")
  time.sleep(1)
  print("_100%_")

  print(f"l'ipotenusa misura: {round(c, 2)} cm")
ipotenusa()




