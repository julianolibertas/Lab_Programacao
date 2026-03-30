# 1. Entrada de Dados
print("--- CALCULADORA DE IMC ---")
massa = float(input("Informe o peso (kg): "))
altura = float(input("Informe a altura (m): "))
# 2. Processamento: IMC = massa / altura²
imc = massa / (altura ** 2)
# 3. Classificação (Lógica IF-ELIF-ELSE)
if imc < 18.5:
    classificacao = "Abaixo do Peso"
elif imc <= 24.9:
    classificacao = "Saudável"
elif imc <= 29.9:
    classificacao = "Peso em excesso"
elif imc <= 34.9:
    classificacao = "Obesidade Grau I"
elif imc <= 39.9:
    classificacao = "Obesidade Grau II (severa)"
else:
    classificacao = "Obesidade Grau III (mórbida)"
# 4. Saída de Dados
print("-" * 30)
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")