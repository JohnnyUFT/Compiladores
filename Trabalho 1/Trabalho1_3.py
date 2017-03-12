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
    operadores = {'*':42,'.':43,'+':46}# simbolo : precedência
    print(operadores['*'])

    palavra = input("Inforome a expressão regular: ")

    # 1 - VARRER TODA A EXPRESSÃO CARACTERE POR CARACTERE ...
    for simbolo in palavra:
        # 1º caso: OPERANDO
        if(simbolo not in operadores and simbolo != '(' and simbolo != ')'):
            posfixa.append(simbolo)
            print("Posfixa aqui %s"%posfixa)

        # 2º caso: PARÊNTESIS ABRINDO
        elif(simbolo == '('):
            pilha.append(simbolo)

        # 3º caso: PARÊNTESIS FECHANDO
        elif(simbolo == ')'):
            i = len(pilha)-1# -1
            if pilha:# o mesmo que pilha not NULL
                while i >= 0 and pilha[i] != '(':
                    posfixa.append(pilha.pop())
                    i-=1
                pilha.pop()# a remover o '(' - desempilhar e descartar

        # 4º e último caso: OPERADOR
        else:
            while pilha:
                if not simbolo:#################
                    posfixa.append(pilha.pop())
            pilha.append(simbolo)# empilhar o operador atual

    # 2 - ENQUANTO HOUVER OPERADOR NA PILHA ...
    if pilha:
        while operadores in pilha:
            posfixa.append(pilha.pop())

    print("Pilha: %s"%pilha)
    print("Palavra: %s"%palavra)
    print("Posfixa %s"%posfixa)

# para uso da função main. Contexto global.
if __name__ == "__main__":
    main()
