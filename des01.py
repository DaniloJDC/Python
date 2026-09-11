#3
vc = int(input("Qual o valor da casa? "))
sl = int(input("Qual o salrio do comporador? "))
pres = int(input("Ira dividir a parcela em quantas vezes? "))

men = vc/pres
fator = sl * 30/100

if men < fator:
    print("pode comprar")

elif men == fator:
    print("processo em analise")

else:
    print("Não foi autorizado o emprestimo")