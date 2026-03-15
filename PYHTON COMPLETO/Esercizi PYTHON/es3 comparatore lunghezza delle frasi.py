def string_comparison():
    m= input("dimmi una frase ")
    s= input("dimmi un'altra frase ")

    if m.lower() == s.lower():
        print("le frasi sono uguali")
    else:
        print("mi dispiace, le frasi sono differenti")
string_comparison()
while True:
    command=input("inserire un comando per favore")
    if command in ["Exit","EXIT","ExIt", "exit"]:
        print("programma chiuso")
    break