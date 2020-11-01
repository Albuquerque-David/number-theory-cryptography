def primocomposto(n):
    """ Dados uma entrada natural 1 < n <= 100000, retorna se o numero e composto ou primo utilizando o Teste de Fermat."""
    x = pow(2%n, n, n)
    if(x != 2%n):
        return "Composto"

    x = pow(3%n, n, n)
    if(x != 3%n):
        return "Composto"
        
    fator = 2
    while (n % fator != 0 and fator*fator <= i):
        fator = fator + 1
    if(fator*fator <= n):
        return "Composto"
    else:
        return "Primo"

for i in range(2,100):
    print(i,":",primocomposto(i))
