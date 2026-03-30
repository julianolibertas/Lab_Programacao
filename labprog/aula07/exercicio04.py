op = input("Deseja somar (S) ou multiplicar (M)? ")
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
if (op == 'S'):
  r = x + y
  print('O resultado da soma é ', r)
else:
  r = x * y
  print('O resultado da multiplicação é ', r)