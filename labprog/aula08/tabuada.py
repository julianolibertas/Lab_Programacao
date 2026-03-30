# laço externo que percorre os numero de 1 a 10
for i in range(1,11):
  print("="*25)
  print(f"\nTabuado do {i}")
  # laço interno calcula a multiplicação
  for j in range(1,11):
    print(f"{i} x {j} = {i*j}")