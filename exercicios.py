import math

# Faça um programa que peça dois números inteiros e imprima a divisão do primeiro pelo segundo.
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir um numero inteiro: "))

resultado = numero_01 // numero_02

print(resultado)

# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}")
