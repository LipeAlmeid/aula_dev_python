# Modificar de FANTASTICO para F A N T A S T I C O

palavra = "FANTASTICO"

for spaco in palavra: 
    print(f' {spaco}', end = '')



# 
'''
Criar um retangulo de 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''

linhas = 6
colunas = 6
simbolo = "@"

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end = "")
    print()


# While Loops 
# Excelente para loops dependentes de uma condição .
# Criar uma promoção para um produto no valor de R$100, na qual o valor nao fique abaixo de 20 reais e diminua 5 reais a cada dia
 
valor = 100
dia = 1

while valor > 20:
    dia += 1
    print(f' dia {dia}')
    print(f' o valor do produto corresponde a: R${valor}')
    valor -= 5


# Operador ternario
# Crie um codigo que mostre a idade da pessoa. Se a pessoa tiver idade maior ou igual a 16 anos pode votar, caso contrario, nao pode

idade = 16 

if idade >= 16:
    resultado = print("Essa pessoa pode votar")
else:
    resultado = print("Essa pessoa nao pode votar")      


resultado = "Voto permitido" if idade >= 16 else "Voto não permitido"

print(resultado)


# While Loops
# Excelente para loops dependentes de uma condição. 
# Publicar um produto com comissão de 10% se for acima de R$20

valor = int(input("Digite o valor do seu produto em R$: "))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de R${valor}')
    break