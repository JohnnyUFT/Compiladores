# !/usr/bin/python3.5
# -*- coding: utf-8 -*-

'''
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: February 2017
'''
import string
# outros imports aqui

def main():
    # variáveis globais
    pilha = []# pilha auxiliar
    posfixa = []# para receber expressão posfixa
    operadores = ['*','.','+']# em ordem de precedência

    palavra = input("Inforome a expressão regular: ")

    # 1 - VARRER TODA A EXPRESSÃO CARACTERE POR CARACTERE ...
    for simbolo in palavra:
        # 1º caso: OPERANDO
        if(simbolo not in operadores and simbolo != '(' and simbolo != ')'):
            posfixa.append(simbolo)

        # 2º caso: PARÊNTESIS ABRINDO
        elif(simbolo == '('):
            pilha.append(simbolo)

        # 3º caso: PARÊNTESIS FECHANDO
        elif(simbolo == ')'):
            i = len(pilha)-1# -1
            if pilha:# o mesmo que pilha not NULL
                while i > 0 and pilha[i] != '(':
                    posfixa.append(pilha.pop())
                    i-=1
                pilha.pop()# a remover o '(' - desempilhar e descartar

        # 4º e último caso: OPERADOR
        else:
            while pilha:
                print("Pilha: %s"%pilha)# teste
                if(simbolo == '*' and pilha[-1] == '.' ):# or
                    pass
                posfixa.append(pilha.pop())
            pilha.append(simbolo)# empilhar o operador atual
            print("Teste\n")

    # 2 - ENQUANTO HOUVER OPERADOR NA PILHA ...
    while pilha:
        posfixa.append(pilha.pop())
        print("Teste\n")

    print("Pilha: %s"%pilha)
    print("Palavra: %s"%palavra)
    print("Posfixa %s"%posfixa)
    palavra = ''.join(posfixa)
    print("Como string %s"%palavra)

# para uso da função main. Contexto global.
if __name__ == "__main__":
    main()
