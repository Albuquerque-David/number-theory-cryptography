def euclides(a, b):
  """Calcula o mdc(a,b), com a,b naturais e b>0, pelo algoritmo de Euclides"""
  dividendo, divisor = a, b
  resto = dividendo % divisor  # resto da divisao de dividendo por divisor
  #print(dividendo, divisor, resto)
  while resto != 0:
    dividendo, divisor = divisor, resto
    resto = dividendo % divisor
    # ou, de uma vez so:
    # dividendo, divisor, resto = divisor, resto, divisor%resto
    #print(dividendo, divisor, resto)
  return divisor
