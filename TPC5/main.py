import re

def calculo_valor_total(valores):
  total = 0.00
  for i in valores:
    if i == '5c':
      total += 0.05
    elif i == '10c':
      total += 0.10
    elif i == '20c':
      total += 0.20
    elif i == '50c':
      total += 0.50
    elif i == '1e':
      total += 1.00
    elif i == '2e':
      total += 2.00
    else:
      print(f"moeda {i} invalida")
  print(f"maq:saldo = {total}")
  return total

def check_num(numero,saldo):
  # Verifica se o número é iniciado por "601" ou "641"
  if re.match(r'^(601|641)', str(numero)):
      print("Chamada bloqueada.")

  # Verifica se o número é uma chamada internacional iniciada por "00"
  elif re.match(r'^00', str(numero)):
      if saldo < 1.5:
          print("Saldo insuficiente.")
      else:
          print("Chamada internacional realizada. Custo: 1.5 euros.")
          saldo -= 1.5

  # Verifica se o número é uma chamada nacional iniciada por "2"
  elif re.match(r'^2', str(numero)):
      if saldo < 0.25:
          print("Saldo insuficiente.")
      else:
          print("Chamada nacional realizada. Custo: 0.25 euros.")
          saldo -= 0.25

  # Verifica se o número é uma chamada verde iniciada por "800"
  elif re.match(r'^800', str(numero)):
      print("Chamada verde realizada. Custo: 0 euros.")

  # Verifica se o número é uma chamada azul iniciada por "808"
  elif re.match(r'^808', str(numero)):
      print("Chamada azul realizada. Custo: 0.10 euros.")
      saldo -= 0.10

  # Se não for nenhum dos casos acima, a chamada é inválida
  else:
      print("Número de telefone inválido.")

  return saldo

def main():
  estados = ("LEVANTAR","MOEDA","POUSAR","T","ABORTAR")

  res = input()
  valor_total = 0
  estado_atual_maq = ""
  saldo_final = 0
  if re.match(r'(?i:LEVANTAR)',res):
    estado_atual_maq = estados[0]
    print("maq:\"inserir moedas!\"")
    res = input()
    if re.match(r'(?i:MOEDA)',res):
      valores = re.findall(r'\d+[ce]', res)
      valor_total = calculo_valor_total(valores)
      while valor_total > 0:
        res = input()
        if re.match(r'(?i:T)',res):
          numero = int(re.findall(r'\d+',res)[0])
          saldo_final = check_num(numero,valor_total)
          print(f"maq:\"saldo = {saldo_final}\"")
        if re.match(r'(?i:POUSAR)',res):
          print(f"maq: \"troco = {saldo_final}")
          break
        if re.match(r'(?i:ABANDONAR)',res):
            print("Abandonou a chamada")
            print(f"maq: {saldo_final}")
            break



if __name__ == "__main__":
  main()
