nivel = float(input("Informe o nível atual do reservatório (%) "))
if nivel >= 90:
  status = "CRÍTICO: Risco de transbordamento"
elif nivel >=50:
  status = "ADEQUADO: Fluxo normal"
elif nivel >=20:
  status = "ATENÇÃO: Nível baixo"
else:
  status = "PERIGO: Nível mínimo atingido!"

print(f"Status do sistema: {status}")
