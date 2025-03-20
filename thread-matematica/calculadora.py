def calculadora(conta):
    conta = conta.replace(",",".")

    if "+" in conta:
        n1, n2 = conta.split("+")
        valor = float(n1) + float(n2)

    elif "-" in conta:
        n1, n2 = conta.split("-")
        valor = float(n1) - float(n2)
    
    elif "*" in conta:
        n1, n2 = conta.split("*")
        valor = float(n1) * float(n2)
    
    elif "/" in conta:
        n1, n2 = conta.split("/")
        valor = float(n1) / float(n2)
    
    else:
        valor = "Operação inválida."

    return valor