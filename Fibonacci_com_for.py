#pergunta para o usuario
pergunta = int(input("Digite um número:"))
# começo do loop/loop para quando digita 0
while pergunta != 0:
    # laços condicionais
    if pergunta == 1:
        print (0)
    elif pergunta == 2:
        print (0)
        print (1)
    else:
        #variaveis
        num1 = 0
        num2 = 1
        num3 = num1 + num2
        #primeiros prints
        print (num1)
        print (num2)
        print (num1, "+", num2, "=", num3)
    #quebra cabeça/loop for
    for p in range (4, pergunta + 1):
        num1 = num2
        num2 = num3

        num3 = num1 + num2
        #mostrar conta p usuario
        print ( num2, "+", num1, "=", num3)
        #pergunta para continuar ou nao continuar
    pergunta = int(input("Digite outro número ou digite \"0\" para encerrar:"))

print( "-" * 60 )
print ("\n\tFim do programa, Obrigada!")