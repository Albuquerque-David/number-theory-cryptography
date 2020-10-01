def altamente_compostos(n = 1):
    """ Entrada: Um número inteiro positivo.
        Saída: Escreve todos os números altamente compostos de 1 até n."""
    
    #Lista de divisores de um inteiro [i], i diferente de 0. Exemplo: [8] armazenará os divisores de 8 
    quant_divisores_numero = [0]

    for i in range(1,n+1):
        quant_divisores = 0
        for j in range(1,i+1):
            if(i%j==0):
                quant_divisores = quant_divisores + 1
        quant_divisores_numero.append(quant_divisores)

    #Checa pra todo número <= n se é altamente composto 

    for i in range(1,n+1):
        aux = 0
        quant_divisores_i = quant_divisores_numero[i]
        for j in range(1,i):
            if(quant_divisores_numero[j] >= quant_divisores_i):
                aux = aux + 1
        if(aux == 0):
            print("O número",i,"é altamente composto")
        
altamente_compostos(5000)
