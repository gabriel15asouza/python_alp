#Exercício 1
import random
lista = random.sample(range(1,101), 10)
print(lista)

k = 9
x = 0
while k != x:
    if lista[k] > lista[x]:
        x = x + 1
    else:
        k= k - 1
print(f'O maior número é {lista[k]}.\n')

k = 9
x = 0
while k != x:
    if lista[k] < lista[x]:
        x = x + 1
    else:
        k= k - 1
print(f'O menor número é {lista[k]}.\n')

#Exercício 2
import random
lista = random.sample(range(1,101), 20)
par = []
impar = []

for x in lista:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print(f'Lista:\n{lista}')
print(f'\nPar:\n{par}')
print(f'\nÍmpar:\n{impar}\n')

#Exercício 3
import random

vetor_1 = random.sample(range(1,101), 10)
vetor_2 = random.sample(range(1,101), 10)
vetor_3 = []

x = 20
v1 = 0
v2 = 0
while x > 0:
    x = x - 1
    if x % 2 == 0:
        vetor_3.append(vetor_1[v1])
        v1 = v1 + 1
    else:
        vetor_3.append(vetor_2[v2])
        v2 = v2 + 1
        
print(f'Vetor 1: {vetor_1}')
print(f'Vetor 2: {vetor_2}')
print(f'Vetor 3: {vetor_3}')



#Exercício 4
statement = '''
The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''

statement = statement.lower()
lista = statement.split()
print(f'\nLista:{lista}')

resultante = []
for x in lista:
    if x[0] in 'python':
        resultante.append(x)
    elif x[-1] in 'python':
        resultante.append(x)
        
print(f'\nResultante:{resultante}\n')

#Exercício 5

statement = '''
The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''

statement = statement.lower()
lista = statement.split()

resultante = []
for x in lista:
    if len(x) > 4:
        resultante.append(x)

for x in resultante:
    if x not in 'python':
        resultante.remove(x)

print(resultante)
print(f'\n{len(resultante)} se encaixam nos requisitos')
        
    








