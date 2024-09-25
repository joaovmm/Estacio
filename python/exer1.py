def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_peso(imc):
    if imc < 18.5:
        return "Magro"
    elif imc < 24.9:
        return "Peso Normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade Grau I"
    elif imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

maior_imc = 0
menor_imc = float('inf')
nome_maior_imc = ""
nome_menor_imc = ""

for i in range(1, 51):
    nome = input(f"Digite o nome da pessoa {i}: ")
    peso = float(input(f"Digite o peso de {nome} (em kg): "))
    altura = float(input(f"Digite a altura de {nome} (em metros): "))
    
    imc = calcular_imc(peso, altura)
    classificacao = classificar_peso(imc)
    
    if imc > maior_imc:
        maior_imc = imc
        nome_maior_imc = nome
    
    if imc < menor_imc:
        menor_imc = imc
        nome_menor_imc = nome

    print(f"Nome: {nome}")
    print(f"IMC: {imc:.2f}")
    print(f"Classificação de peso: {classificacao}\n")

print("Pessoa com o maior IMC:")
print(f"Nome: {nome_maior_imc}")
print(f"IMC: {maior_imc:.2f}\n")

print("Pessoa com o menor IMC:")
print(f"Nome: {nome_menor_imc}")
print(f"IMC: {menor_imc:.2f}\n")
