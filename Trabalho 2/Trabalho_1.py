# !/usr/bin/python3.5
# -*- coding: utf-8 -*-
"""
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
"""
from tkinter import messagebox

import Automato as auto
from Automato import *
import numpy as np  # para manipulação das matrizes
# import seaborn as sns

# *******************************
# Aqui inicia-se o tratamento para transformar uma expressão infixa em posfixa.
# Implementação do Algoritmo nº 1
# *******************************


def getPosfixa(palavra):
    """
    Transforma expressão infixa em posfixa;
    Algoritmo dado pelo profº Alexandre Rossini.
    :param palavra: expressão regular em sua forma infixa;
    :return: none.
    """
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
    # printar a mesma
    palavra = ''.join(posfixa)
    print("\nExpressão posfixa: %s\n"%palavra)

    # retorna a expressão regular no formato polonesa reversa
    return posfixa

# *******************************
# Implementação do Algoritmo nº 2:
# recebe a expressão posfixa e tenta montá-la (resolvê-la)
#  *******************************
def montaPosfixa(posfixa):
    """
    'Monta' a expressão posfixa utilizando a instância de autômatos
    como operando para as operações de # concatenação, união e fecho de Kleene.
    :param posfixa: expressão no formato polonesa reversa;
    :param cont: auxiliar para tratamento dos parênteses;
    :return: autômato resultante do tratamento de todas as operações presentes
    na expressão, através de seus respectivos operadores.
    """
    pilha = []
    operadores = ['*', '.', '+']  # em ordem de precedência

    for simbolo in posfixa:
        # se simbolo é um operando, faça-se a base
        if(simbolo not in operadores):

            # transforma simbolo em autômato
            afd = base(simbolo)

            # empilha a base
            pilha.append(afd)
        else:
            # se simbolo é um operador binário
            if (simbolo == '.' or simbolo == '+') and pilha:
                # op1 e op2 são autômatos
                op2 = pilha.pop()
                if pilha:
                    op1 = pilha.pop()
                    # transforma op1 e op2 em um único autômato:
                    # afd é o autômato resultante
                    if simbolo == '.':
                        afd = concatena(op1, op2)
                        pilha.append(afd)
                    elif simbolo == '+':
                        afd = une(op1, op2)
                        # corrigir nome e/ou identação
                        pilha.append(afd)
                else:
                    messagebox.showerror("Erro", "Falta operando!")

            # se simbolo é um operador unário: '*'
            else:
                if simbolo == '*' and pilha:
                    op1 = pilha.pop()
                    afd = fechoKleene(op1)
                    pilha.append(afd)
    op1 = pilha.pop()
    if not pilha:
        #  ed2.insert(0, palavra)
        # ed2 recebe mesmo a expressão posfixa
        messagebox.showinfo("Parabéns", "Expressão Aceita!")
        imprimeAFD(op1)

    else:
        messagebox.showerror("Erro", "Expresão Rejeitada!")


def trataConcatenacao(palavra):
    """
    Verifica necessidade de explicitar os operadores
     de concatenação nas expressões infixas fornecidas pelo usuário.
    :param palavra: expressão regular em sua forma infixa;
    :return: expressão regular com operador de ponto, explícito;
    """
    # declaração das varíaveis
    operadores = ['*', '.', '+', '(', ')']  # em ordem de precedência
    i = 0
    j = len(palavra) - 1

    while i < j:
        if palavra[i] not in operadores and palavra[i + 1] not in operadores \
                or palavra[i] not in operadores and palavra[i + 1] == '(' \
                or palavra[i] == '*' and palavra[i + 1] not in operadores \
                or palavra[i] == ')' and palavra[i + 1] not in operadores \
                or palavra[i] == '*' and palavra[i + 1] == '(' \
                or palavra[i] == ')' and palavra[i + 1] == '(':
            palavra = palavra[:i + 1] + '.' + palavra[i + 1:]
            j = len(palavra) - 1
        i += 1
    return palavra


def base(simbolo):
    """
    Base, segundo Thompson.
    :param simbolo: um simbolo da expressão posfixa;
    :return: um autômato que representa esse símbolo.
    """

    # instancía a classe autômato
    afd = auto.Automato()

    # seta a quíntupla da base
    afd.setAlfabeto([simbolo])

    b = np.zeros([2, 1], dtype=list)  # cria array de listas
    b[0][0] = [1]
    b[1][0] = []

    
    afd.setEstados([0, 1])
    afd.setEstadoInicial(0)
    afd.setEstadoFinal(1)
    afd.setmTransicao(b)

    return afd


def concatena(automatoA, automatoB):
    """
    De acordo com o algoritmo de Thompson,
    recebe 2 autômatos e junta-os em um só.
    :param automatoA: operando A;
    :param automatoB: operando B;
    :return: um autômato resultante da operação de concatenação.
    """
    # instancía novo autômato chamando-o de concatenacao
    concatenacao = auto.Automato()

    concatenacao.setEstadoInicial(automatoA.getEstadoInicial())
    # captura tamanho
    t1 = uneEstados(automatoA, automatoB)
    tam = []
    for i in range(t1):
        tam.append(i)
    concatenacao.setEstados(tam)

    estados = concatenacao.getEstados()
    concatenacao.setEstadoFinal(estados[-1])

    concatenacao.setAlfabeto(uneAlfabetos(automatoA, automatoB))
    matR = preencheMatriz(concatenacao.getEstados(), concatenacao.getAlfabeto())
    concatenacao.setmTransicao(matR)

    fTransicao1(concatenacao, automatoA, automatoB)

    return concatenacao


def une(automatoA, automatoB):
    """
    Implementa o algoritmo de Thompson para operação de união.
    :param automatoA: operando A;
    :param automatoB: operando B;
    :return: um autômato, isto é, uma quíntupla (instância de auto.Automato()).
    """
    uniao = auto.Automato()

    # captura tamanho
    t1 = uneEstados(automatoA, automatoB)
    t1 += 2
    tam = []
    for i in range(t1):
        tam.append(i)
    uniao.setEstados(tam) # conjunto de estados

    estados = uniao.getEstados()

    uniao.setEstadoInicial(estados[0]) # estado inicial
    uniao.setEstadoFinal(estados[-1]) # estado final
    uniao.setAlfabeto(uneAlfabetos(automatoA, automatoB)) # alfabeto

    matR = preencheMatriz(uniao.getEstados(), uniao.getAlfabeto())
    uniao.setmTransicao(matR)

    fTransicao2(uniao, automatoA, automatoB)

    return uniao



def fechoKleene(automato):
    """
    Recebe apenas um autômato e aplica sobre o mesmo, o 
    algoritmo de Thompson para o caso de haver fecho de Kleene.
    :param automato: instância de autômato(). É uma base.
    :return: um autômato, que é o fecho kleene aplicado á base. 
    """
    fechoK = auto.Automato()
    # setar atributos para fechoKleene
    t1 = len(automato.getEstados())
    t1 += 2
    tam = []
    for i in range(t1):
        tam.append(i)
    fechoK.setEstados(tam)  # conjunto de estados

    estados = fechoK.getEstados()

    fechoK.setEstadoInicial(estados[0])  # estado inicial
    fechoK.setEstadoFinal(estados[-1])  # estado final
    # necessário por acrecentar '&' ao alfabeto
    fechoK.setAlfabeto(uneAlfabetos(automato, automato)) # alfabeto

    matR = preencheMatriz(fechoK.getEstados(), fechoK.getAlfabeto())
    fechoK.setmTransicao(matR)

    fTransicao3(fechoK, automato)

    return fechoK

# otimizar este método


def uneAlfabetos(autoA, autoB):
    """
    Une os alfabetos em um único CONJUNTO.
    Refazer utilizando set() i.e conjunto.
    """

    lAlfab = autoA.getAlfabeto()
    # necessário utilizar copy() pois lAlfab 'é um ponteiro'
    # e todas as alterações em lAlfab refletem diretamente
    # no atributo alfabeto do autômato A
    lAlfabeto = lAlfab.copy()

    for simbolo in autoB.getAlfabeto():
        if simbolo not in lAlfabeto:
            lAlfabeto.append(simbolo)

    # o '&' deve obrigatoriamente ficar ao final da lista
    if '&' not in lAlfabeto:
        lAlfabeto.append('&')  # insere o '&' ao final do alfabeto
    else:
        # necessário ordenar sem trazer o '&' para primeira posição
        for i in range(len(lAlfabeto)):
            if lAlfabeto[i] == '&':
                lAlfabeto.pop(i)  # utilizar remove('&')
                break
        lAlfabeto.append('&')

    return lAlfabeto


def uneEstados(autoA, autoB):
    """
    Recebe dois autômatos e retorna uma lista com estados iguais
    á quantidade de estados de autoA + autoB.
    # refazer para Trabalho 3
    """
    estadosA = autoA.getEstados()
    estadosB = autoB.getEstados()

    t1 = len(estadosA)+len(estadosB)

    return t1


def preencheMatriz(estados, alfabeto):
    """
    Cria uma matriz dinamicamente para ser utilizada no Automato
    """
    qtdEstados = len(estados)
    qtdSimbolos = len(alfabeto)

    b = np.zeros([qtdEstados, qtdSimbolos], dtype=list)  # cria array de listas
    for i in range(qtdEstados):
        for j in range(qtdSimbolos):
            b[i][j] = []  # cria células formadas por listas vazias

    return b


def fTransicao1(atual, autoA, autoB):
    """
	Implementa a função de transição para concatenação de autômatos;
	Todo o trabalho é feito dinamicamente;
		
		:param atual: Autômato resultante pós-operação;
		:param autoA: operando (autômato) A da expressão;
		:param autoB: operando (autômato) B da expressão;
		:return: autômato resultante, aqui referenciado como atual/R.
		"""
    # referenciam os objetos retornados
    matA = autoA.getmTransicao() # matriz de transicao do autômato A
    matB = autoB.getmTransicao() # matriz de transicao do autômato B
    matR = atual.getmTransicao() # matriz de transicao do autômato R

    # final1 + atual2 + 1
    alfaA = autoA.getAlfabeto() # lista de simbolos do alfabeto do autômato A
    alfaB = autoB.getAlfabeto() # lista de simbolos do alfabeto do autômato B
    estA = autoA.getEstados() # lista de estados do autômato A
    estB = autoB.getEstados() # lista de estados do autômato B
    alfaR = atual.getAlfabeto() # lista de simbolos do alfabeto do autômato R
    estR = atual.getEstados() # lista de estados do autômato R

    # para matriz A:
    for simbolo in alfaA:
        posSimboloA = getPosicaoSimbolo(simbolo, alfaA)
        posSimboloR = getPosicaoSimbolo(simbolo, alfaR)
        for estado in estA:
            if matA[estado][posSimboloA]:
                celula = matA[estado][posSimboloA]
                for elemento in celula:
                    if elemento not in matR[estado][posSimboloR]:
                        matR[estado][posSimboloR].append(elemento)

    # para matriz B:
    for simbolo in alfaB:
        posSimboloB = getPosicaoSimbolo(simbolo, alfaB)
        for estado in estB:
            if matB[estado][posSimboloB]:
                posSimboloB = getPosicaoSimbolo(simbolo, alfaB)
                #posicaoEstadoB = getPosicaoEstado(simbolo, autoB)
                celula = matB[estado][posSimboloB]
                for elemento in celula:
                    # atualiza posicao do estado de B em relacao a R
                    posEstadoR = estado + estA.index(estA[-1]) + 1
                    posSimboloR = getPosicaoSimbolo(simbolo, alfaR)
                    # atualiza valor do elemento em R:
                    k = elemento + estA.index(estA[-1]) + 1
                    # possível já haver estados lá, então:
                    if k not in matR[posEstadoR][posSimboloR]:
                        matR[posEstadoR][posSimboloR].append(k)

    # estado final de A, leva ao inicial de B, através de '&'
    # i.e, fTransicao(estadoFinalA, '&'): estadoInicialB

    # i = posição do estado final de A
    i = estA.index(estA[-1])
    # j recebe posição do simbolo '&' na matriz resultante
    #j = getPosicaoSimbolo('&', alfaR) # desnecessário, pois sabemos
    # que o '&' está, indubitavelmente, na última posicao.
    j = alfaR.index(alfaR[-1])
    # k = posição do estado inicial de B
    k = estB.index(estB[0])
    # setando célula da matriz
    matR[i][j].append(i + k + 1)
    # na primeira iteração, fica assim:
    #matR[1][1].append(1 + 0 + 1)

    # NÃO NECESSITA RETORNO
    return matR



def fTransicao2(atual, autoA, autoB):
    """
    Função de transição para a operação de UNIAO.
    :param atual: autômato resultante pós-operação de união;
    :param autoA: operando A: instância de auto.Automato();
    :param autoB: operando B: instância de auto.Automato();
    :return: autômato resultante.
    """
    # referenciam os objetos retornados
    matA = autoA.getmTransicao()  # matriz de transicao do autômato A
    matB = autoB.getmTransicao()  # matriz de transicao do autômato B
    matR = atual.getmTransicao()  # matriz de transicao do autômato R

    # final1 + atual2 + 1
    alfaA = autoA.getAlfabeto()  # lista de simbolos do alfabeto do autômato A
    alfaB = autoB.getAlfabeto()  # lista de simbolos do alfabeto do autômato B
    estA = autoA.getEstados()  # lista de estados do autômato A
    estB = autoB.getEstados()  # lista de estados do autômato B
    alfaR = atual.getAlfabeto()  # lista de simbolos do alfabeto do autômato R
    estR = atual.getEstados()  # lista de estados do autômato R

    # para matriz A:
    for simbolo in alfaA:
        posSimboloA = getPosicaoSimbolo(simbolo, alfaA)
        posSimboloR = getPosicaoSimbolo(simbolo, alfaR)
        for estado in estA:
            if matA[estado][posSimboloA]:
                celula = matA[estado][posSimboloA]
                for elemento in celula:
                    # estados em A são deslocados em +1 em R
                    if elemento not in matR[estado+1][posSimboloR]:
                        # elemento é referência a um estado e por isso, +1
                        matR[estado+1][posSimboloR].append(elemento + 1)

    # para matriz B:
    for simbolo in alfaB:
        posSimboloB = getPosicaoSimbolo(simbolo, alfaB)
        for estado in estB:
            if matB[estado][posSimboloB]:
                posSimboloB = getPosicaoSimbolo(simbolo, alfaB)
                #posicaoEstadoB = getPosicaoEstado(simbolo, autoB)
                celula = matB[estado][posSimboloB]
                for elemento in celula:
                    # atualiza posicao do estado de R em relacao a B
                    posEstadoR = estado + (estA[-1] + 1) + 1
                    posSimboloR = getPosicaoSimbolo(simbolo, alfaR)
                    # possível já haver estados lá, então:
                    if elemento not in matR[posEstadoR][posSimboloR]:
                        # estados em B são deslocados: estB + estA[-1] + 1
                        k = elemento + (estA[-1] + 1) + 1
                        matR[posEstadoR][posSimboloR].append(k)

    #i = estA[0]
    # j recebe a posicao de '&'
    j = alfaR.index(alfaR[-1])
    #k = estB.index(estB[0])
    matR[0][j].append(estA[0] + 1)
    matR[0][j].append(estB[0] + (estA[-1] + 1) + 1)

    matR[estA[-1] + 1][j].append(estR[-1])
    matR[estB[-1] + (estA[-1] + 1) + 1][j].append(estR[-1])

    # desnecessário, pois as alterações já foram feitas
    return matR


def fTransicao3(fechoK, autoA):
    """
    Aplica transições para fecho de Kleene ao autômato 
    recebido como parâmetro.
    # Autômato resultante referenciado como autômato R.
    :param fechoK: autômato #Resultante da operação;
    :param autoA: base para aplicação do fecho Kleene; 
    :return: autômato resultante (fechoK).
    """

    matA = autoA.getmTransicao()  # matriz de transicao do autômato A
    matR = fechoK.getmTransicao()  # matriz de transicao do autômato R

    alfaA = autoA.getAlfabeto()  # lista de simbolos do alfabeto do autômato A
    estA = autoA.getEstados()  # lista de estados do autômato A
    alfaR = fechoK.getAlfabeto()  # lista de simbolos do alfabeto do autômato R
    estR = fechoK.getEstados()  # lista de estados do autômato R

    # para matriz A:
    for simbolo in alfaA:
        posSimboloA = getPosicaoSimbolo(simbolo, alfaA)
        posSimboloR = getPosicaoSimbolo(simbolo, alfaR)
        for estado in estA:
            if matA[estado][posSimboloA]:
                celula = matA[estado][posSimboloA]
                for elemento in celula:
                    # estados em A são deslocados em +1 em R
                    if elemento not in matR[estado + 1][posSimboloR]:
                        # elemento é referência a um estado e por isso, +1
                        matR[estado + 1][posSimboloR].append(elemento + 1)

    # transições vazias:

    # posicao de '&' na matriz
    j = alfaR.index(alfaR[-1])

    matR[0][j].append(estA[0] + 1)
    matR[0][j].append(estR[-1])

    matR[estA[-1] + 1][j].append(estA[0] + 1)
    matR[estA[-1] + 1][j].append(estR[-1])
    


def getPosicaoSimbolo(simbolo, alfabeto):
    """
    retorna a posição do simbolo no alfabeto (lista).
    :param simbolo: caractere da expressão posfixa;
    :param alfabeto: lista contendo simbolos da 'fita';
    :return: posicao = índice do símbolo na lista.
    """
    posicao = -1
    for caractere in alfabeto:
        if simbolo == caractere:
            # captura posição do simbolo na lista
            posicao = alfabeto.index(simbolo)

    return posicao



# REFAZER utilizando GUI
def imprimeAFD(afd):
    print("\n Simbolos do Alfabeto: %s" % afd.getAlfabeto())

    print("\n Estados do Autômato Resultante: ")
    for i in range(len(afd.getEstados())):
        print("q%s"%i)
    print("\n Matriz de Transição: \n%s" % afd.getmTransicao())
    print("\n Estado Inicial: ->q%s" % afd.getEstadoInicial())
    print("\n Estado Final: *q%s\n" % afd.getEstadoFinal())

