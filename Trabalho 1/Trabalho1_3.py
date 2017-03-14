# !/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
'''
import string
import sys

# *******************************
# Aqui inicia-se o tratamento para transformar uma expressão infixa em posfixa.
# Implementação do Algoritmo nº 1
# *******************************
def principal():
    '''
    Captura a expressão na forma infixa
    e envia-a para o método trataConcatenacao afim de verificar a
    necessidade de colocar o ponto de concatenação.
    Na sequência, chama algoritmo que transforma expressão infixa em posfixa.
    :return: none
    '''

    palavra = ed1.get()

    # Verificação especial para simbolo de concatenação:
    palavra = trataConcatenacao(palavra)

    getPosfixa(palavra)

def getPosfixa(palavra):
    '''
    Transforma expressão infixa em posfixa.
    Esse algoritmo foi dado pelo profº Alexandre Rossini.
    :param palavra:
    :return: none
    '''
    # variáveis globais
    pilha = []# pilha auxiliar
    posfixa = []# para receber expressão posfixa
    operadores = ['*', '.', '+']# em ordem de precedência
    cont = 0 # para controle dos parênteses

    # 1 - VARRER TODA A EXPRESSÃO CARACTERE POR CARACTERE ...
    for simbolo in palavra:

        # 1º caso: OPERANDO
        if simbolo not in operadores and simbolo != '(' and simbolo != ')':
            posfixa.append(simbolo)

        # 2º caso: PARÊNTESES ABRINDO
        elif simbolo == '(':
            cont += 1
            pilha.append(simbolo)


        # 3º caso: PARÊNTESES FECHANDO
        elif simbolo == ')':
            cont -= 1
            # caso a):
            while pilha:
                if pilha[-1] != '(':
                    posfixa.append(pilha.pop())
                else:
                    break
            # caso b):
            pilha.pop()# desempilha '('

        # 4º e último caso: OPERADOR
        elif simbolo in operadores:
            while pilha:
                if pilha[-1] == '*' and simbolo == '.'\
                    or pilha[-1] == '*' and simbolo == '+'\
                    or pilha[-1] == '.' and simbolo == '+'\
                    or simbolo == pilha[-1]:
                    posfixa.append(pilha.pop())
                else:
                    break
            pilha.append(simbolo)  # empilhar o operador atual


    # 2 - ENQUANTO HOUVER OPERADOR NA PILHA ...
    while pilha:
        print("Debugue manual %s"%pilha)
        posfixa.append(pilha.pop())


    # a título de verificação:
    print("Pilha: %s"%pilha)
    print("Palavra: %s"%palavra)
    print("Posfixa %s"%posfixa)

    # converte uma vetor de simbolos em uma string
    palavra = ''.join(posfixa)

    # a título de verificação
    print("Como string %s"%palavra)

    montaPosfixa(posfixa, operadores, palavra, cont)

# *******************************
# Implementação do Algoritmo nº 2:
# recebe a expressão posfixa e tenta montá-la (resolvê-la)
# *******************************

def montaPosfixa(posfixa, operadores, palavra, cont):
    '''
    Tenta 'resolver' a expressão regular em sua forma posfixa.
    Obviamente, não deve conseguir fazer isso, e o resultado da
    resolução é apenas ignorado. Todavia, trata de verificar a
     expressão quanto o correto uso de operandos e operadores.
    :param posfixa:
    :param operadores:
    :param palavra:
    :param cont:
    :return: none
    '''
    pilha = []

    for simbolo in posfixa:
        # se simbolo é um operando
        if(simbolo not in operadores):
            pilha.append(simbolo)
        else:
            # se simbolo é um operador binário
            if simbolo == '.' or simbolo == '+' and pilha:
                op2 = pilha.pop()
                if(pilha):
                    op1 = pilha.pop()
                    # transforma-os em uma única palavra (um único termo):
                    valor = op1+simbolo+op2
                    pilha.append(valor)
                else:
                    messagebox.showerror("Erro", "Falta operando.")

            # se simbolo é um operador unário: '*'
            else:
                if simbolo == '*' and pilha:
                    op1 = pilha.pop()
                    valor = op1+simbolo
                    pilha.append(valor)
    op1 = pilha.pop()
    if not pilha and cont == 0:
        ed2.insert(0, palavra)
        messagebox.showinfo("Muito bem", "Expressão Aceita.")

        print("Resultado: %s"%op1)

        # limpa os campos
        ed1.delete(0, END)
        ed2.delete(0, END)
    else:
        messagebox.showerror("Erro", "Expresão Rejeitada.")

        # limpa os campos
        ed1.delete(0, END)
        ed2.delete(0, END)


def trataConcatenacao(palavra):
    '''
    Verifica necessidade de explicitar os operadores
     de concatenação nas expressões dadas.
    :param palavra:
    :param operadores:
    :return: palavra
    '''
    # declaração das varíaveis
    operadores = ['*', '.', '+', '(', ')']# em ordem de precedência
    i = 0
    j = len(palavra)-1

    while i<j:
        if palavra[i] not in operadores and palavra[i+1] not in operadores \
                or palavra[i] not in operadores and palavra[i+1] == '(' \
                or palavra[i] == '*' and palavra[i+1] not in operadores \
                or palavra[i] == ')' and palavra[i+1] not in operadores \
                or palavra[i] == '*' and palavra[i+1] == '(' \
                or palavra[i] == ')' and palavra[i+1] == '(':
            palavra = palavra[:i+1]+'.'+palavra[i+1:]# funciona lindamente
            j = len(palavra)-1
        i+=1
    return palavra
