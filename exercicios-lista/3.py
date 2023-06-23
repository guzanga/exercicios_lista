num = []

while True:
    num.append(int(input("digite um numero")))
    pare = int(input("digite 0 para parar"))
    if pare == 0:
        break

soma = sum(num)
print("esta é a soma dos numeros:", soma)
menor = min(num)
print("este é o menor numero",menor)