#50
s = 0
for c in range(0,6):
    n = int(input("Qual numeros pares deseja somar? "))

    if n % 2 != 0:
        n = 0

    else:
        s += n

print("A soma dos numeros é:", s)