import math
perimetro = float(input("dimmi un perimetro: "))
n = int(input("dimmi un numero per n: "))

def area(N):
  area_n = (perimetro**2) / (4*N*math.tan(math.pi/N))
  return area_n
print("area al variare di n" )
for x in range(3, n +1):

  print(f"area poligono con lati {x}: ", round(area(x), 3))

area_cerchio = (perimetro**2) / (4 * math.pi)

# Stampa dei risultati arrotondati a 3 decimali
print("Area del cerchio:", round(area_cerchio, 3))


