#Exercício1
n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
soma= n1+n2
print(f'Resultado: {soma}')

#Exercício2
metros=float(input('\nQual a sua altura em metros? '))
milimetros=metros*1000
print(f'Sua altura em milímetros é {milimetros}')

#Exercício3
dias=int(input('\nQuantidade de dias: '))
horas=int(input('Quantidade de horas: '))
minutos=int(input('Quantidade de minutos: '))
segundos=int(input('Quantidade de segundos: '))
total=24*3600*dias+3600*horas +60*minutos+segundos
print(f'Você está conectado há {total} segundos')

#Exercício4
salário=float(input('\nQual o valor do seu salário mensal? '))
porcent=float(input('Qual a porcentagem do aumento pelo qual seu salário irá passar(x/100)? '))
aumento = salário*porcent/100
novo_salário = salário+aumento
print(f'Seu salário passará por um aumento de {aumento:.2f} reais, totalizando assim em um total de {novo_salário:.2f} reais.')

#Exercício5
mercadoria=float(input('\nQual o preço da mercadoria? '))
percentual=float(input('Qual o percentual de desconto (x/100)? '))
desconto=mercadoria*percentual/100
novo_preço=mercadoria-desconto
print(f'Sua mercadoria teve um desconto de {desconto:.2f} reais em seu valor, totalizando assim em um novo preço de {novo_preço:.2f} reais.')

#Exercício6
distância=float(input('\nQual a distância em quilometros até o seu destino? '))
velocidade=float(input('Qual a velociade média em km/h esperada para a viagem? '))
tempo=distância/velocidade
print(f'Seu tempo de viagem será de {tempo} horas')

#Exercício7
celsius=float(input('\nIndique a temperatura em Celsius: '))
fahrenheit=9*celsius/5 +32
print(f'Essa temperatura em Fahrenheit equivale a {fahrenheit:.2f} graus Fahrenheit.')

#Exercício8
fahrenheit=float(input('\nIndique a temperatura em Fahrenheit: '))
celsius=(fahrenheit-32)*5/9
print(f'Essa temperatura em Celsius equivale a {celsius:.2f} graus Celsius.')

#Exercício9
km=float(input('\nQual foi a quilometragem percorrida pelo veículo? '))
dias=float(input('Qual é o período do aluguel em dias? '))
total=km*0.15 + dias*60
print(f'O valor total do aluguel será de {total:.2f} reais.')

#Exercício10
fumados_dia=float(input('\nQuantidade de cigarros fumados por dias: '))
anos=float(input('Quantidade de anos fumando: '))
cigarros_anos=365*fumados_dia*anos
redução_minutos=cigarros_anos*10
redução_dias=int((redução_minutos/(60*24)))
print(f'A quantidade de dias perdidos em decorrência do fumo será de {redução_dias} dias.\n')

#Exercício11
print(len(str(2**1000)))

