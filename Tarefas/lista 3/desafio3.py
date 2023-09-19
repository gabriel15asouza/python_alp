#Exercício 1
numero = int(input('Digite um número natural: '))
l = 1
while numero > l*(l-1)*(l+1):
    l = l + 1
    if (numero = l*(l-1)*(l+1)) == True
        print('É Triangular')
    else:
        print('Não é triangular')

#Exercício 2
preco = int(input('Preço: '))
pago = int(input('Valor pago: '))
troco = pago - preco
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
nota_1 = 0

while True:
    if troco >= 50:
        troco = troco - 50
        nota_50 = nota_50 + 1

    elif troco >= 20:
        troco = troco - 20
        nota_20 = nota_20 + 1
        
    elif troco >= 10:
        troco = troco - 10
        nota_10 = nota_10 + 1
        
    elif troco >= 5:
        troco = troco - 5
        nota_5 = nota_5 + 1
        
    elif troco >= 2:
        troco = troco - 2
        nota_2 = nota_2 + 1
        
    elif troco >= 1:
        troco = troco - 1
        nota_1 = nota_1 + 1
        
    else:
        break
print(f'\tTroco = {pago - preco}')
print(f'\tNotas de 50 = {nota_50}')
print(f'\tNotas de 20 = {nota_20}')
print(f'\tNotas de 10 = {nota_10}')
print(f'\tNotas de 5 = {nota_5}')
print(f'\tNotas de 2 = {nota_2}')
print(f'\tNotas de 1 = {nota_1}')

#Exercício 3
numero = int(input('Digite um número natural: '))
divisor = 1
while True:
    divisor = divisor + 1
    if numero == 1:
        print('Não é primo')
        break
    elif numero == divisor:
        print('É primo')
        break
    elif numero % divisor == 0:
        print('Não é primo')
        break

#Exercício 4
numero = int(input('Digite um número natural: '))
fator = 1
divisor = 1
decomp = numero - divisor
while True:
    divisor = divisor + 1
    if divisor == fator
        divisor == 'primo'
        while True:
            if numero - divisor < 0 
                
            
    elif divisor % fator = 0
        divisor == 'não é primo'


        
#Exercício 5
numero = str(input('Digite um número natural: '))
termos = int(len(numero))
inverso = 0
while termos > 0:
    termos = termos - 1
    ordem = int(numero[termos])*10**(termos)
    ordem, inverso = inverso, ordem + inverso
print(inverso)