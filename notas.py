#!/usr/bin/env python3
TOTAL=(0)
CONTADOR_NOTAS=(0)
user_input=(0)
#definindo as variáveis TOTAL, CONTADOR_NOTAS e as das entradas do usuário (user_input), como zero
while CONTADOR_NOTAS <10:
#criando um while para fazer a somatória e divisão das notas entradas pelo usuário
    try:
#utilizando um try para controlar a entrada do usuário, ao digitar algo que não seja número no terminal
        user_input =float(input("Digite a nota:"))
        #definindo a entrada do usuário
        if user_input > 10:
            print("Coloque uma nota com o valor entre 0 e 10")
        elif user_input < 0:
            print("Coloque uma nota com o valor entre 0 e 10")
        else:
        #colocando exceções e fazendo o controle das entradas do usuário utilizando if, elif e else
            TOTAL=TOTAL+user_input
            CONTADOR_NOTAS=CONTADOR_NOTAS+1
        #somando as notas entradas pelo usuário
    except:
        print("coloque um valor numérico entre 0 e 10, ou que a casa decimal seja separado por \".\" como: 5.6")
    #caso não tenha se entrado com valores adequador o except entrará em ação
TOTAL=TOTAL/10
#fazendo o calculo da média obtida pelo usuário
print("Média:",TOTAL)
