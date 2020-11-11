
import random
import time

#==============Funcoes Principais==============
def gera_primos(n):
    """Funcao responsavel por gerar um numero primo de tamanho n atraves de tentativas pelo teste de Miller-Rabin."""
    ini = time.time()
    
    print("====================")
    print("Gerando numero primo")
    print("====================")
    i = 0
    while(i <= 10):
        i = 0
        primo = random.randrange(pow(10,n-1), pow(10,n))

        if(primo % 2 == 0):
            continue

        for j in range(1,10+2):
            base = random.randrange(1, primo)
            if(Miller_Rabin(primo,base) == "inconclusivo"):
                i+=1
    fim = time.time()
    print("============ A funcao gera_primos demorou: {} segundos ============".format(fim-ini))
    return primo

def gera_chaves(dp,dq):
    """Funcao responsavel por gerar as chaves do RSA. Dp e o numero de digitos de P e Dq e o numero de digitos de Q"""
    ini = time.time()
    print("==============")
    print("Gerando chaves")
    print("==============")

    #Gera os primos P e Q
    p = gera_primos(dp)
    q = gera_primos(dq)
    n = p*q

    phi = (p-1)*(q-1)
    e = 0
    i = 2
    #Calcula um numero e inversivel modulo phi
    while(e == 0):
      if(euclides(i,phi) == 1):
          e = i
      else:
        i+=1
      

    #Calcula o inverso d de e mod(phi)
    d = euclides_estendido(e,phi)
    d += phi

    print("P: {}".format(p))
    print("Q: {}".format(q))
    print("Chave publica N: {}".format(n))
    print("Phi: {}".format(phi))
    print("Chave pubilca E: {}".format(e))
    print("Chave privada D: {}".format(d))
    print("Numero de digitos de P: {}".format(len(str(p))))
    print("Numero de digitos de Q: {}".format(len(str(q))))

    n = p*q

    fim = time.time()
    print("============ A funcao gera_chaves demorou: {} segundos ============".format(fim-ini))

    return n, e, d
    #return p,q

def encriptar(texto,n,e):
    """Funcao responsavel por encriptar uma string texto usando as chaves publicas n (modulo) e e (expoente)."""
    print("=================")
    print("Encriptando texto")
    print("=================")
    texto_numero = texto
    texto_encriptado = pow(texto_numero,e,n) 
    print("Texto encriptado: {}".format(texto_encriptado))
    return texto_encriptado


def descriptar(texto, n, d):
    """Funcao responsavel por descriptar uma string texto usando as chaves publicas n (modulo) e e (expoente)."""
    print("==================")
    print("Descriptando texto")
    print("==================")
    texto_numero = texto
    texto_descriptado = pow(texto_numero, d, n)
    print("Texto descriptado: {}".format(texto_descriptado))
    return texto_descriptado

#==============Algoritmos Auxiliares==============
def parte_par(m):
  """Retorna k e q tais que m = (2**k)*q com q impar"""
  k = 0
  q = m
  while q % 2 == 0:
    k += 1  # equivalente a k = k + 1
    q //= 2  # equivalente a q = q // 2
  return k, q


def Miller_Rabin(n, base):
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


def euclides_estendido(a, b):
    """Retorna o inverso multiplicativo de a atraves do euclidiano estendido"""
    divisor, resto = a, b
    x_ant, x_novo = 1, 0
    y_ant, y_novo = 0, 1
    while resto != 0:
        dividendo, divisor = divisor, resto
        quociente, resto = dividendo//divisor, dividendo % divisor
        x_ant, x_novo = x_novo, x_ant - (x_novo*quociente)
        y_ant, y_novo = y_novo, y_ant - (y_novo*quociente)
        #print("dividendo:", dividendo, ", divisor: ", divisor, ", quociente:", quociente, ", resto: ",
        #     resto, ", x_ant: ", x_ant, ", y_ant: ", y_ant, ", x_novo: ", x_novo, ", y_novo: ", y_novo)
    return x_ant


#Main

print("=========================RSA=========================")
ini = time.time()
n, e, d = gera_chaves(50, 100)
descriptar(encriptar(123456789, n, e), n, d)
fim = time.time()
print("O processo completo levou: {}".format(fim-ini))
print("=========================RSA=========================")
