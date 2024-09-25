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

maior_imc = None
menor_imc = None
nome_maior_imc = ""
nome_menor_imc = ""

continuar = True

while continuar:
    nome = input("Digite o nome da pessoa: ")
    peso = float(input(f"Digite o peso de {nome} (em kg): "))
    altura = float(input(f"Digite a altura de {nome} (em metros): "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_peso(imc)

    print(f"Nome: {nome}")
    print(f"IMC: {imc:.2f}")
    print(f"Classificação de peso: {classificacao}\n")

    if maior_imc is None or imc > maior_imc:
        maior_imc = imc
        nome_maior_imc = nome
    if menor_imc is None or imc < menor_imc:
        menor_imc = imc
        nome_menor_imc = nome

    resposta = input("Deseja continuar? (Sim ou Não): ").strip().lower()
    if resposta != "sim":
        continuar = False

print("\nResumo:")
print(f"Pessoa com maior IMC: {nome_maior_imc} (IMC: {maior_imc:.2f})")
print(f"Pessoa com menor IMC: {nome_menor_imc} (IMC: {menor_imc:.2f})")
