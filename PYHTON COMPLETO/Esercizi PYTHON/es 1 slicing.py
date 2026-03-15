while True:
    s= input("dimmi una frase, per terminare il programma premi 'E': ")
    s=s.upper()
    if s== 'E':
        print("ci vediamo alla prossima volta: ")
        break
    while True:

        a= int(input("dammi un numero per favore: "))
        b= int(input("dammi un'altro numero: "))
        if a < 0 or len(s) < b or a > b:
            print("mi dispiace hai sbagliato qualcosa: ")
        else:
            print("ecco il tuo risultato:", s[a:b])
            break

