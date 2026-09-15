#59
while True:

    d = input("[1] somar\n" 
    "[2] multiplicar\n" 
    "[3] subtração\n" 
    "[4] divisão\n" \
    "[5] sair\n" 
    "Oq deseja fazer? ")

    o = float(input("Qual o primeiro valor? "))
    o2 = float(input("Qual o segundo valor? "))

    if d == "1":
        print(o + o2)

    elif d == "2":
        print(o * o2)

    elif d == "3":
        print(o - o2)

    elif d == "4":
        print(o/o2)

    else:
        break
