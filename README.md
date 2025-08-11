# Calculadora de IMC

Este é um programa simples em Python que calcula o Índice de Massa Corporal (IMC) de um aluno com base no peso e altura informados pelo usuário.

## Como usar

1. Clone ou baixe o repositório.
2. Execute o script Python.
3. Informe seu nome, peso (em kg) e altura (em metros).
4. O programa exibirá o IMC calculado e uma mensagem indicando a classificação do peso.

----------------------------------------------------
## Código exemplo

```python
aluno = input("Digite seu nome: ")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc =  peso / (altura * altura)

print(f"nome do aluno: {aluno}, seu IMC é: {imc:.2f}")

if imc < 18.5:    
    print("ABAIXO DO PESO")
elif imc < 24.9:
    print("PESO NORMAL")
else: 
    print("PESO ACIMA DO NORMAL")
----------------------------------------------------

Classificação do IMC
Abaixo de 18.5: Abaixo do peso

Entre 18.5 e 24.9: Peso normal

Acima de 24.9: Peso acima do normal
