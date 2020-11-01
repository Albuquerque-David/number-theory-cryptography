def euclides_estendido(a,b):
    divisor, resto = a,b
    x_ant, x_novo = 1,0
    y_ant, y_novo = 0,1
    while resto != 0:
        dividendo, divisor = divisor, resto
        quociente, resto = dividendo//divisor, dividendo%divisor
        x_ant, x_novo = x_novo, x_ant - (x_novo*quociente)
        y_ant, y_novo = y_novo, y_ant - (y_novo*quociente)
        print("dividendo:" ,dividendo,", divisor: ",divisor,", quociente:" ,quociente,", resto: ",resto,", x_ant: ",x_ant,", y_ant: ",y_ant,", x_novo: ",x_novo,", y_novo: ",y_novo)
    return divisor, x_ant, y_ant

euclides_estendido(137,2887)