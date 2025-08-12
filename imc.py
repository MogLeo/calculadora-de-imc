aluno = input("Digite seu nome: ")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc =  peso / (altura * altura)

print(f"nome do aluno: {aluno}, seu IMC é: {imc:.2f}")

if imc < 18.5:    
    print("ABAIXO DO PESO💀💀💀")
elif imc < 24.9:
    print("PESO NORMAL😁😁😁")
else: 
    print("PESO ACIMA DO NORMAL🤢🤢🤢")