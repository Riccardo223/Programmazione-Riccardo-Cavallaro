primi= []
for _ in range(3):
    num = int(input("Inserisci un numero: "))
    primi.append(num)
for item in primi:
    if item > 1:
        is_prime = True
        for i in range(2, item):
            if item % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{item} è un numero primo!")
        else:
            print(f"{item} NON è un numero primo.")
    else:
        print("Un numero primo deve essere maggiore di 1.")
