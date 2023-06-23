num = []

while True:
    num2 = int(input("digite um numero"))

    if num2 in num:
        print("\nesse numero já existe!")
    else:
        num.append(num2)

    pare = int(input("\ndigite 0 para parar"))
    if pare == 0:
        break

num.sort()

print("estes são os valores unicos em ordem crescente", num)




