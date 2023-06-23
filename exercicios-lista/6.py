num = []
numeros = 0

while True:
    num.append(int(input("digite um numero")))
    pare = int(input("digite 0 para parar"))
    if pare == 0:
        break
    else:
        numeros += 1

print("esta é a quantidade de numeros digitados:", numeros)

num.sort(reverse=True)

print("estes são os numeros em ordem decrecente:", num)

for five in num:
    if five == 5:
        print("não possui o numero 5")
        break
    else:
        print("possui o numero 5")
        break
