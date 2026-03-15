#le liste sono come una singola variabile, ma utilizzata per immaggazinare molte cose 
# 3 tipi di lista
#list = []
#Set = {}
#tuple = ()

frutta = ['mela', 'pera', 'banana']
print(frutta)


frutta = ['mela', 'pera', 'banana']
print(frutta[::-1])

for x in frutta:
  if x[0] == 'm':
    print(x)
  else:
    print("questa parola non comincia per M")


#con dir(lista) possiamo accedere a tutti i built-in methods per le liste
#con help(lista) invece possiamo farci spiegare a cosa servono i methods 

#ti dice se un item si trova o no in una lista 
print("mela" in frutta)

#riassegna il primo elemento di frutta
#frutta[0] = 'niggers'

#aggiunge un elemento
frutta.append("melone")
#rimuove un elemento
frutta.remove("banana")
#inserisce al posto che vuoi tu un elemento
frutta.insert(1, 'negro')
#sistema gli oggetti in ordine alfabetico
frutta.sort()
#scrive la lista al contrario
frutta.reverse()
#ti scrive l'indice del elemento che vuoi tu:
print(frutta.index('mela'))
#conta i duplicati in una lista:
print(frutta.count('mela'))
#elimina gli oggetti della lista 
frutta.clear()

#print(frutta)



#set 

negro = {'mela', 'pera','cazzo', 'gay'}
print(negro)

negro.add('polizia')
negro.remove('mela')
#rimuove il primo elemento, quindi un eliminazione randomica
negro.pop()
negro.clear()
print(negro)



#tuple 

tup = ('mela', 'pera', 'banana', 'negro')

print(len(tup))
print('negri' in tup)

print(tup.index('mela'))
print(tup.count('negro'))






