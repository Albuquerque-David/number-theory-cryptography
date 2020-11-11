def parte_par(m):
  """Retorna k e q tais que m = (2**k)*q com q impar"""
  k = 0
  q = m
  while q % 2 == 0:
    k += 1  # equivalente a k = k + 1
    q //= 2  # equivalente a q = q // 2
  return k, q


def teste_de_Miller_Rabin(n, base):
  """Recebe n impar e base com 1<base<n e retorna
  'composto' ou 'inconclusivo' de acordo com o Teste de Miller-Rabin"""
  k, q = parte_par(n-1)
  i = 0
  r = pow(base, q, n)

  if r in (1, n-1):
    return "inconclusivo"

  while i < k:
    i += 1
    r = pow(r, 2, n)
    if r == n-1:
      return "inconclusivo"
    elif r == 1:
      return "composto"

  return "composto"
