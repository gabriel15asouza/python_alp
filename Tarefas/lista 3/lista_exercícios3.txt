#Exercício 1
while True:
    nota=int(input('Digite uma nota entre 0 e 10: '))
    if 0<=nota<=10:
        print(f'Valor válido! Nota {nota} foi atribuída.\n')
        break
    else:
        print('Valor inválido! Tente outro valor.\n')

#Exercício 2
while True:
    usuario = str(input('Usuário: '))
    senha = str(input('Senha (diferente do seu usuário): '))
    if usuario == senha:
        print('Cadastro não autorizado. Redefina seu usuário ou senha.\n')
    else:
        print('Cadastro completo!\n')
        break

#Exercício 3
ano = 0
pais_a = 80000
taxa_a = 3/100
pais_b = 200000
taxa_b = 1.5/100

while (pais_a < pais_b):
    pais_a = pais_a + pais_a*taxa_a
    pais_b = pais_b + pais_b*taxa_b
    ano = ano + 1
print(f'Ano: {ano}\n')

#Exercício 4
termo = int(input('Qual termo da sequência você deseja? '))
a = 0
b = 1
index = 0
while True:
    a, b = b, a + b
    index = index + 1
    if termo <=2:
        print(f'Termo {termo}: {1}')
        break
    elif index == termo:
        print(f'Termo {termo}: {a}')
        break
        

#Exercício 5
n1 = int(input('\nDigite um numero: '))
n2 = int(input('Digite um numero menor: '))
salvar = 0
while True:
    salvar = n2
    n2 = n1%n2
    n1 = salvar
    if (n1==0 or n2 == 0):
        print(f'MDC: {n1}')
        break
