"""
###Exercio 1 - Para verificar se um número é impar ou par, você pode fazer essa estrutura condicional###
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

"""

"""
###Exercicio 2 - Condicionais que informará a idade em categorias###

idade = int(input('Digite sua idade: '))

if 0 < idade <=12:
    print ('Criança')
elif 12 < idade < 18:
    print ('Adolescente')
elif idade > 18:
    print ('Adulto')
else:
    print('Valor inválido!') """

"""
#Exercicio 3 - Confirmação de usuário

usuario_correto = "alura"
senha_correta = "alura123"

usuario = input ("Digite o nome de usuário: ")
senha = input ("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
   print("Login bem sucedido!")
else:
   print("Credenciais inválidas. Tente novamente.")"""

"""
Exercicio 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.

"""

"""
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x> 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrente.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x >  0 and y < 0:
    print("O ponto está no quarto quadrente.")
else:
    print("O ponto está sobre um eixo ou na origem.")

"""
