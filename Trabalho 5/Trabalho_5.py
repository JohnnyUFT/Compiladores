# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: May 2017
"""
from tkinter import messagebox

import Automato as auto
from Automato import *
import numpy as np  # para manipulação das matrizes
from collections import Counter # para manipulação dos dicionários
# import seaborn as sns

# *******************************
# Implementação dos métodos First e Follow():
# *******************************


def first(A):
    """
    Implementa método First();
    :return: 
    """
    retorno = []
    for pi in arquivo:
        if pi in A:
            # CASO 1:
            if A > 'e':
                retorno.append('e')
            else:
                flag = True
                for simb in pi_imagem:
                    # CASO 2.1:
                    if terminal(simb):
                        retorno.append(simb)
                        flag = False
                        break
                    # CASO 2.2:
                    elif variavel(simb) and simb != A:
                        if 'e' not in first(simb):
                            retorno.append(first(simb))
                            flag = False
                            break
                        else:
                            retorno.append(retiraVazio(first(simb)))
                        # fim do if
                    # fim do if
                # fim do for
                if flag: # se flag == True
                    retorno.append('e')
                # fim do if
            # fim do if
        # fim do if
    # fim do for
    return retorno
# fim do método first().



def follow(A):
    """
    Implementa metodo follow para gramatica ll1.
    :param A: variavel da gramatica
    :return: lista com ...
    """
    retorno = []
    if ehInicial(A):
        retorno.append('$')
    for regra_pi in gramaticaG:
        for sj in imagemPI(regra_pi):
            if sj == A:
                flag = False
                k = j+1 # controlar isso aqui
                while k < n: # n é o total de simbolos de pj;
                    if terminal(sk):
                        retorno.append(sk)
                        flag = True
                        break
                    elif 'e' not in first(sk):
                        retorno.append(first(sk))
                        flag = True
                        break # finalizar laço do indice k
                    else:
                        retorno.append(retiraVazio(first(sk)))
                    # fim do if
                    k = j+1 # controlar isso aqui
                # fim do While
                if ((flag == False) and (dominioPJ(pj) != A)):
                    B = dominioPJ(pj)
                    retorno.append(follow(B))
                # fim do if
            # fim do if
        # fim do for
    # fim do for
    return retorno
# fim do metodo follow.


def terminal(simbolo):
    """
    Analisa se o simbolo recebido como parâmetro é ou
    não, terminal.
    :return: valor booleano.
    """
    if simbolo in terminal:
        return True
    return False


def variavel(simbolo):
    """
    Verifica se determinado simbolo é variavel ou não.
    :param simbolo:
    :return: valor booleano.
    """
    if simbolo in variavel:
        return True
    return False


def retiraVazio(retornoFirst):
    """
    Retira 'e' da lista retornada por first(sj), caso houver.
    :return: uma lista, sem 'e' como elemento.
    """
    if 'e' in retornoFirst:
        retornoFirst.remove('e')
    return retornoFirst


def ehInicial(simbolo):
    """
    Verifica se determinado simbolo é inicial, ou não;
    :param simbolo: simbolo variável; 
    :return: booleano.
    """
    if simbolo in inicio:
        return True
    return False

def imagemPI(p):
    """
    Constroi lista com imagens da regra de produção p;
    :return: 
    """
    for a in regras:
        pass

def dominioPJ(p):
   """
   Retorna domínio da regra p
   :param p: regra de producao na gramatica ll1;
   :return: lista, cujos elementos pertencem ao dominio de p.
   """
