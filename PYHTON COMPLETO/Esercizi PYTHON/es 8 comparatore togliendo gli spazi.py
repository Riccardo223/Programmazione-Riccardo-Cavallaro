def lenght_comparison():
    str1= input("dimmi una frase ")
    str2= input("dimmi un'altra frase ")

    if len(str1.replace(" ","")) == len(str2.replace(" ","")):
        print("compimenti, le frasi sono uguali")
    else:
        print("le frasi hanno una lunghezza differente")
lenght_comparison()

while True:
    command=input("inserire un comando per favore")
    if command in ["Exit","EXIT","ExIt", "exit"]:
        print("programma chiuso")
    break

