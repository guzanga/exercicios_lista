num = []
mult = 1

while True:
    num.append(int(input("digite um numero")))
    pare = int(input("digite 0 para parar"))
    if pare == 0:
        break

for c in num:
    mult = mult * c

print("estes são os numeros:", num)
soma = sum(num)
print("esta é a soma dos numeros:", soma)
print("esta é a multiplicação:", mult)
maior = max(num)
menor = min(num)
print(" este é o maior numero:" ,maior)
print("este é o menor numero",menor)

