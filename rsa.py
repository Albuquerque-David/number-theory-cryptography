import random
import time

#==================Dicionario==================
códigos_para_símbolos = {111: '0', 112: '1', 113: '2', 114: '3', 115: '4',
116: '5', 117: '6', 118: '7', 119: '8', 121: '9', 122: '=', 123: '+',
124: '-', 125: '/', 126: '*', 127: 'a', 128: 'b', 129: 'c', 131: 'd',
132: 'e', 133: 'f', 134: 'g', 135: 'h', 136: 'i', 137: 'j', 138: 'k',
139: 'l', 141: 'm', 142: 'n', 143: 'o', 144: 'p', 145: 'q', 146: 'r',
147: 's', 148: 't', 149: 'u', 151: 'v', 152: 'w', 153: 'x', 154: 'y',
155: 'z', 156: 'á', 157: 'à', 158: 'â', 159: 'ã', 161: 'é', 162: 'ê',
163: 'í', 164: 'ó', 165: 'ô', 166: 'õ', 167: 'ú', 168: 'ç', 169: 'A',
171: 'B', 172: 'C', 173: 'D', 174: 'E', 175: 'F', 176: 'G', 177: 'H',
178: 'I', 179: 'J', 181: 'K', 182: 'L', 183: 'M', 184: 'N', 185: 'O',
186: 'P', 187: 'Q', 188: 'R', 189: 'S', 191: 'T', 192: 'U', 193: 'V',
194: 'W', 195: 'X', 196: 'Y', 197: 'Z', 198: 'Á', 199: 'À', 211: 'Â',
212: 'Ã', 213: 'É', 214: 'Ê', 215: 'Í', 216: 'Ó', 217: 'Ô', 218: 'Õ',
219: 'Ú', 221: 'Ç', 222: ',', 223: '.', 224: '!', 225: '?', 226: ';',
227: ':', 228: '_', 229: '(', 231: ')', 232: '"', 233: '#', 234: '$',
235: '%', 236: '@', 237: ' ', 238: '\n'}

símbolos_para_códigos = {'0': 111, '1': 112, '2': 113, '3': 114, '4': 115,
'5': 116, '6': 117, '7': 118, '8': 119, '9': 121, '=': 122, '+': 123,
'-': 124, '/': 125, '*': 126, 'a': 127, 'b': 128, 'c': 129, 'd': 131,
'e': 132, 'f': 133, 'g': 134, 'h': 135, 'i': 136, 'j': 137, 'k': 138,
'l': 139, 'm': 141, 'n': 142, 'o': 143, 'p': 144, 'q': 145, 'r': 146,
's': 147, 't': 148, 'u': 149, 'v': 151, 'w': 152, 'x': 153, 'y': 154,
'z': 155, 'á': 156, 'à': 157, 'â': 158, 'ã': 159, 'é': 161, 'ê': 162,
'í': 163, 'ó': 164, 'ô': 165, 'õ': 166, 'ú': 167, 'ç': 168, 'A': 169,
'B': 171, 'C': 172, 'D': 173, 'E': 174, 'F': 175, 'G': 176, 'H': 177,
'I': 178, 'J': 179, 'K': 181, 'L': 182, 'M': 183, 'N': 184, 'O': 185,
'P': 186, 'Q': 187, 'R': 188, 'S': 189, 'T': 191, 'U': 192, 'V': 193,
'W': 194, 'X': 195, 'Y': 196, 'Z': 197, 'Á': 198, 'À': 199, 'Â': 211,
'Ã': 212, 'É': 213, 'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217, 'Õ': 218,
'Ú': 219, 'Ç': 221, ',': 222, '.': 223, '!': 224, '?': 225, ';': 226,
':': 227, '_': 228, '(': 229, ')': 231, '"': 232, '#': 233, '$': 234,
'%': 235, '@': 236, ' ': 237, '\n': 238}


#==============Funcoes Principais==============
def converte_texto(texto):
  """Converte o texto usando a tabela de conversão."""
  texto_convertido = str(texto)
  for simbolo, codigo in símbolos_para_códigos.items():
    texto_convertido = texto_convertido.replace(simbolo, str(codigo))

  return texto_convertido

def desconverte_texto(texto):
  """Desconverte o texto convertido utilizando a função converte_texto()."""
  texto_desconvertido = str(texto)
  texto_desconvertido = texto_desconvertido.replace("[","")
  texto_desconvertido = texto_desconvertido.replace("]","")
  texto_desconvertido = texto_desconvertido.replace(",","")
  texto_desconvertido = texto_desconvertido.replace(" ","")
  texto_desconvertido = [texto_desconvertido[i:i+3] for i in range(0, len(texto_desconvertido), 3)]
  for iterator, value in enumerate(texto_desconvertido):
    for codigo, simbolo in códigos_para_símbolos.items():
      if(str(value) == str(codigo)):
        texto_desconvertido[iterator] = simbolo
        break

  texto_desconvertido = ''.join(texto_desconvertido)
  
  return texto_desconvertido

def quebra_blocos(n,texto):
  """Quebra uma cadeia de caracteres ou números em blocos de tamanho n."""
  texto = str(texto)
  texto_blocos = [texto[i:i+n] for i in range(0, len(texto), n)]
  return texto_blocos

def desquebra_blocos(texto_blocos):
  """Junta os blocos resultante da quebra pela função quebra_blocos."""
  texto = ''.join(str(texto_blocos))
  return texto

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
    #print("============ A funcao gera_primos demorou: {} segundos ============".format(fim-ini))
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

    #Calcula o inverso ip de p mod(q)
    ip = euclides_estendido(p,q)
    if(ip < 0):
      ip += q

    #Calcula o inverso iq de q mod(p)
    iq = euclides_estendido(q,p)
    if(iq < 0)
      iq += p

    #Calcula as formas reduzidas de d mod p - 1 e q - 1
    pd = pow(d, 1, p-1)
    qd = pow(d, 1,q-1)

    #print("P: {}".format(p))
    #print("Q: {}".format(q))
    #print("Chave publica N: {}".format(n))
    #print("Phi: {}".format(phi))
    #print("Chave pubilca E: {}".format(e))
    #print("Chave privada D: {}".format(d))
    #print("Numero de digitos de P: {}".format(len(str(p))))
    #print("Numero de digitos de Q: {}".format(len(str(q))))
    #print("Numero de digitos de N: {}".format(len(str(n))))
    #print("Inverso p mod q: {}".format(ip))
    #print("Inverso q mod p: {}".format(iq))
    #print("Forma reduzida d mod p - 1: {}".format(pd))
    #print("Forma reduzida d mod q - 1: {}".format(qd))

    fim = time.time()
    #print("============ A funcao gera_chaves demorou: {} segundos ============".format(fim-ini))

    return n, e, d, p, q, ip, iq, pd, qd

def encriptar(texto,n,e):
    """Funcao responsavel por encriptar uma string texto em blocos usando as chaves publicas n (modulo) e e (expoente)."""
    print("=================")
    print("Encriptando texto")
    print("=================")
    texto_numero = converte_texto(texto)
    texto_numero_blocos = quebra_blocos(len(str(n))-1,texto_numero)
    for index, value in enumerate(texto_numero_blocos):
      texto_numero_blocos[index] = pow(int(value),e,n) 
    #print("Texto encriptado em blocos: {}".format(texto_numero_blocos))
    return texto_numero_blocos


def descriptar(texto, n, d):
    """Funcao responsavel por descriptar blocos de string encriptadas usando as chaves publicas n (modulo) e e (expoente)."""
    print("==================")
    print("Descriptando texto")
    print("==================")
    for index, value in enumerate(texto):
      texto[index] = pow(int(value), d, n)
    texto_desquebrado = desquebra_blocos(texto)
    #print("Texto desquebrado: {}".format(texto_desquebrado))
    texto_descriptado = desconverte_texto(texto_desquebrado)
    #print("Texto descriptado: {}".format(texto_descriptado))
    return texto_descriptado


def descriptar_rapido(texto, n, d, p, q, ip, iq, pd, qd):
  for index, value in enumerate(texto):
      texto[index] = (pow(int(value), pd, p) * q * iq) + (pow(int(value), qd, q) * p * ip)
  print("estou no descripta rapido")
  print(texto)
  texto_desquebrado = desquebra_blocos(texto)
  return texto_desquebrado

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
print(descriptar(encriptar("Hi! Im a simple message!", n, e), n, d))
print(descriptar(encriptar("oi", n, e), n, d, p, q, ip, iq, pd, qd))
fim = time.time()
print("O processo completo levou: {}".format(fim-ini))
print("=========================RSA=========================")

#print(quebra_blocos(2,1234567))
#print(desquebra_blocos(quebra_blocos(2, 1234567)))
