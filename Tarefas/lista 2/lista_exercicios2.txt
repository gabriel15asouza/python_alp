#Exercício 1
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if l1<l2+l3 and l2<l1+l3 and l3<l2+l1:
    print('É triângulo')
    if (l1==l2==l3):
        print('Equilátero\n')
    elif (l1==l2 or l2==l3 or l1==l3):
        print('Isósceles\n')
    else:
        print('Escaleno\n')
else:
    print('Não é triângulo\n')

#Exercício 2
ano = int(input('Digite o ano: '))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('É bissexto\n')
else:
    print('Não é bissexto\n')

#Exercício 3
peso= float(input('Digite o peso em Kg: '))
if peso <= 50:
    taxa = 0
    print(f'Peso permitido. Taxa igual a R$ {taxa}.\n')

else:
    excesso = peso - 50
    taxa = 4*excesso
    print(f'Peso excedido em {excesso:.2f}. Valor a ser pago igual a R${taxa:.2f}.\n')

#Exercício 4
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
if n1>n2 and n1>n3:
    print(f'O maior número é {n1}\n')
if n2>n1 and n2>n3:
    print(f'O maior número é {n2}\n')
if n3>n2 and n3>n1:
    print(f'O maior número é {n3}\n')

#Exercício 5
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

if n1>n2 and n1>n3:
    print(f'O maior número é {n1}')
    if n3>n2:
        print(f'O menor número é {n2}\n')
    if n2>n3:
        print(f'O menor número é {n3}\n')

if n2>n1 and n2>n3:
    print(f'O maior número é {n2}')
    if n1>n3:
        print(f'O menor número é {n3}\n')
    if n3>n1:
        print(f'O menor número é {n1}\n')

if n3>n2 and n3>n1:
    print(f'O maior número é {n3}')
    if n1>n2:
        print(f'O menor número é {n2}\n')
    if n2>n1:
        print(f'O menor número é {n1}\n')

#Exercício 6
salario_hora = float(input('Salário por hora: '))
hora = int(input('Horas: '))
salario_bruto = salario_hora*hora
sindicato = 0.05*salario_bruto
imp_renda = 0.08*salario_bruto
inss = 0.11*salario_bruto
descontos = sindicato + imp_renda + inss
salario_liquido = salario_bruto - descontos
print(f'\ta. + Salário Bruto : R${salario_bruto}\n\tb.-IR (11%) : R${imp_renda}\n\tc.-INSS (8%) : R${inss}\n\td.-Sindicato ( 5%) : R${sindicato}\n\t e.= Salário Liquido : R${salario_liquido}\n\t')

#Exercício 7
area = float(input('Área em metros quadrados: '))
litros = area/3
latas = litros//18
resto = litros/18
if resto != 0:
    print(f'Comprar {latas + 1} latas de tinta.')
else:
    print(f'Comprar {latas} lata(s) de tinta.')
