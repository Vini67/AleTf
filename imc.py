def calcular_imc(peso, altura):
    if peso is None or altura is None or peso == "" or altura == "":
        raise ValueError("Erro: peso e altura não podem ser nulos ou vazios.")
    
    try:
        peso = float(peso)
        altura = float(altura)
    except ValueError:
        raise ValueError("Erro: peso e altura devem ser números válidos.")
    
    if altura <= 0:
        raise ValueError("Erro: altura deve ser maior que zero.")
    if peso <= 0:
        raise ValueError("Erro: peso deve ser maior que zero.")
    
    imc = peso / (altura ** 2)
    return round(imc, 2)


# Programa principal
try:
    peso = input("Digite seu peso (kg): ").strip()
    altura = input("Digite sua altura (m): ").strip()

    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("Classificação: Peso normal")
    elif 25 <= imc < 29.9:
        print("Classificação: Sobrepeso")
    elif 30 <= imc < 39.9:
        print("Classificação: Obesidade")
    else:
        print("Classificação: Obesidade grave")

except ValueError as e:
    print(e)
