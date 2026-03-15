
n=[]
for _ in range(3):

    parole= input("dammi 1 parola, la lunghezza di questa parola deve essere di 4 ")
    n.append(parole)

print(n)
for parole in n:
    if len(parole) == 4 and parole[0] == parole[-1] and parole[1] == parole[-2]:
        print("ecco le parole palindrome:", parole)
    elif len(parole) != 4:
        print("queste parole sono della lunghezza sbagliata: ", parole)
    else:
        print("ecco le parole che non sono palindrome:", parole)
