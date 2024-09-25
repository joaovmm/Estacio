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

nomes = []
pesos = []
alturas = []

continuar = True

while continuar:
    nome = input("Digite o nome da pessoa: ")
    peso = float(input(f"Digite o peso de {nome} (em kg): "))
    altura = float(input(f"Digite a altura de {nome} (em metros): "))

    nomes.append(nome)
    pesos.append(peso)
    alturas.append(altura)

    resposta = input("Deseja continuar? (Sim ou Não): ").strip().lower()
    if resposta != "sim":
        continuar = False

imcs = [calcular_imc(peso, altura) for peso, altura in zip(pesos, alturas)]

for i in range(len(nomes)):
    print("\nResultado para", nomes[i])
    print(f"IMC: {imcs[i]:.2f}")
    print(f"Classificação de peso: {classificar_peso(imcs[i])}")

maior_imc = max(imcs)
menor_imc = min(imcs)
indice_maior_imc = imcs.index(maior_imc)
indice_menor_imc = imcs.index(menor_imc)

print("\nPessoa com maior IMC:", nomes[indice_maior_imc], f"IMC: {maior_imc:.2f}")
print("Pessoa com menor IMC:", nomes[indice_menor_imc], f"IMC: {menor_imc:.2f}")
