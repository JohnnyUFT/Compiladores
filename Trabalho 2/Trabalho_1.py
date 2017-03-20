# !/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
'''
import string
import sys
from tkinter import messagebox

from Automato import*
import Automato as auto

# *******************************
# Aqui inicia-se o tratamento para transformar uma expressão infixa em posfixa.
# Implementação do Algoritmo nº 1
# *******************************


def getPosfixa(palavra):
    '''
    Transforma expressão infixa em posfixa.
    Esse algoritmo foi dado pelo profº Alexandre Rossini.
    :param palavra:
    :return: none
    '''
    # variáveis globais
    pilha = []  # pilha auxiliar
    posfixa = []  # para receber expressão posfixa
    operadores = ['*', '.', '+']  # em ordem de precedência
    cont = 0  # para controle dos parênteses

    # Verificação especial para simbolo de concatenação:
    palavra = trataConcatenacao(palavra)

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
            pilha.pop()  # desempilha '('

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
        posfixa.append(pilha.pop())

    # converte uma vetor de simbolos em uma string
    palavra = ''.join(posfixa)
    # a título de verificação
    print("Como string %s" %palavra)

    # if cont == 0:
    # retorna a expressão regular no formato polonesa reversa
    return posfixa
    # else:
    # return ''

# *******************************
# Implementação do Algoritmo nº 2:
# recebe a expressão posfixa e tenta montá-la (resolvê-la)
# *******************************

def montaPosfixa(posfixa):
    '''
    Tenta 'resolver' a expressão regular em sua forma posfixa.
    Obviamente, não deve conseguir fazer isso, e o resultado da
    resolução é apenas ignorado. Todavia, trata de verificar a
     expressão quanto ao correto uso de operandos e operadores.
    :param posfixa:
    :param cont:
    :return: none
    '''
    pilha = []
    operadores = ['*', '.', '+']  # em ordem de precedência

    for simbolo in posfixa:
        # se simbolo é um operando, faça-se a base
        if(simbolo not in operadores):

            # transforma simbolo em autômato
            base = auto.Automato(simbolo)
            print("teste base: %s"%base.getAlfabeto()) # a descartar

            # empilha a base
            pilha.append(base)
        else:
            # se simbolo é um operador binário
            if (simbolo == '.' or simbolo == '+') and pilha:
                # op1 e op2 são autômatos
                op2 = pilha.pop()
                if pilha:
                    op1 = pilha.pop()
                    # transforma op1 e op2 em um único autômato:
                    # valor é um autômato
                    if simbolo == '.':
                        valor = concatenacao(op1, op2)
                    elif simbolo == '+':
                        valor = uniao(op1, op2)
                    pilha.append(valor)
                else:
                    messagebox.showerror("Erro", "Falta operando!")

            # se simbolo é um operador unário: '*'
            else:
                if simbolo == '*' and pilha:
                    op1 = pilha.pop()
                    valor = fechoKleene(op1)
                    pilha.append(valor)
    op1 = pilha.pop()
    if not pilha:
        #  ed2.insert(0, palavra)
        # ed2 recebe mesmo a expressão posfixa
        messagebox.showinfo("Parabéns", "Expressão Aceita!")
        imprimeAFD(op1)

    else:
        messagebox.showerror("Erro", "Expresão Rejeitada!")

       
def trataConcatenacao(palavra):
    '''
    Verifica necessidade de explicitar os operadores
     de concatenação nas expressões dadas.
    :param palavra:
    :param operadores:
    :return: palavra
    '''
    # declaração das varíaveis
    operadores = ['*', '.', '+', '(', ')']  # em ordem de precedência
    i = 0
    j = len(palavra)-1

    while i < j:
        if palavra[i] not in operadores and palavra[i+1] not in operadores \
                or palavra[i] not in operadores and palavra[i+1] == '(' \
                or palavra[i] == '*' and palavra[i+1] not in operadores \
                or palavra[i] == ')' and palavra[i+1] not in operadores \
                or palavra[i] == '*' and palavra[i+1] == '(' \
                or palavra[i] == ')' and palavra[i+1] == '(':
            palavra = palavra[:i+1]+'.'+palavra[i+1:]  # funciona lindamente
            j = len(palavra)-1
        i += 1
    return palavra


def concatenacao(automatoA,automatoB):
    """
    De acordo com o algoritmo de Thompson,
    recebe 2 autômatos e junta-os em um só
    """
    # instancia novo autômato chamando-o de concatenacao
    concatenacao = auto.Automato()
    
    # seta atributos para concatenacao
    concatenacao.setAlfabeto(uneAlfabetos(automatoA, automatoB))
    concatenacao.setEstados(uneEstados(automatoA, automatoB, '.')) # (?)
    concatenacao.setEstadoInicial(automatoA.getEstadoInicial())
    concatenacao.setEstadosFinais(automatoB.getEstadosFinais())
    concatenacao.setfTransicao() # (?)
    concatenacao.setQtdEstados(automatoA.getQtdEstados() + automatoB.getQtdEstados())
    concatenacao.setQtdEstadosFinais() # (?)
    
    return concatenacao

#  recebe dois autômatos e retorna um terceiro
def uniao(automatoA,automatoB):
    """
        Implementa o algoritmo de Thompson para operação de união.
        retorna um autômato, isto é, uma quíntupla (instância de auto.Automato).
        """
    uniao = auto.Automato()
    # setar atributos para uniao
    return uniao

# recebe apenas um autômato e retorna um outro, de acordo com op1
# algoritmo de Thompson
def fechoKleene(automato):
    fechoKleene = auto.Automato()
    # setar atributos para fechoKleene
    return fechoKleene

# otimizar este método
def uneAlfabetos(automatoA, automatoB):
    '''
    Une os alfabetos em um único CONJUNTO.
    '''
    alfabetoFinal = []
    alfabetoA = automatoA.getAlfabeto()
    alfabetoB = automatoB.getAlfabeto()
    for simbolo in alfabetoA:
        alfabetoFinal = simbolo
    for simbolo in alfabetoB:
        if simbolo not in alfabetoFinal:
            alfabetoFinal = simbolo
    
    # insere palavra vazia ('&') entre os simbolos do alfabeto
    alfabetoFinal.append('&') # insere-a como último elemento

    return alfabetoFinal


def uneEstados(autoA, autoB, op):
    '''
    Recebe dois automatos e retorna uma lista com estados iguais
    á quantidade de estados de autoA + autoB.
    Parâmetro: op: refere-se a operação a ser realizada, a saber,
    concatenação, uniao, ou fechoKleene.
    # repensar sua utilização.
    '''

    if op == '.':
        qtdEstados = len(autoA.getQtdEstados()) + len(autoB.getQtdEstados())
    elif op == '+' or op == '*':
        qtdEstados = len(autoA.getQtdEstados()) + len(autoB.getQtdEstados()) + 2
    
    lEstados = [] # a receber a lista com estados unidos (Make America Great Again!)
    lEstados = range(qtdEstados) # cria lista com valores de 0 a qtdEstados-1
    
    return lEstados

# REFAZER utilizando GUI
def imprimeAFD(afd):
    print("\n Simbolos do Alfabeto: %s"%afd.getAlfabeto())
    print("\n Estados do Autômato Final: %s"%afd.getEstados())
    print("\n Matriz de Transição: %s"%afd.getmTransicao())
    print("\n Estado Inicial: %s"%afd.getEstadoInicial())
    print("\n Estados Finais: %s"%afd.getEstadosFinais())
    print("\n Quantidade de Estados: %s"%afd.getQtdEstados())
    print("\n Quantidade de Estados Finais: %s"%afd.getQtdEstadosFinais())
