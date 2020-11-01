def pseudoprimos(base, limite, contador = False):
  """ Dados uma entrada natural base >=2 e limite <= 10^5, retorna uma lista contendo todos
  todos os pseudoprimos de Fermat entre 2 e o limite para a base dada. 
  O terceiro parametro e um booleano opcional. Se True, retorna a quantidade de pseudoprimos ate o limite. Se False,
  nao retorna essa contagem."""
  pseudoprimos = []
  cont = 0

  for i in range(3, limite+1):
      x = pow(base, i, i)
      if(x == base):

        if(i%2==0):
          pseudoprimos.append(i)
          cont+=1
          continue
        
        fator = 3
        while (i % fator != 0 and fator*fator <= i):
          fator = fator + 1
        if(fator*fator <= i):
          pseudoprimos.append(i)
          cont+=1

  print("Pseudoprimos: ",pseudoprimos)
  if(contador == True):
    print("Quantidade de pseudoprimos: ",cont)

pseudoprimos(7, 100000, True)
