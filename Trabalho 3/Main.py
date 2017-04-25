#/usr/lib64/python3.5
# -*- coding: utf-8 -*-

'''
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
'''

import Trabalho_3 as t1
from Trabalho_3 import *


# *******************************
#
# Definição da CLASSE PRINCIPAL do projeto:
# Classe responsável, entre outras coisas, por instanciar a classe Automato()
# e, de acordo com os passos do Algoritmo de Thompson, realizar a conversão
# de uma expressão regular posfixa em Autômato Finito Não Determinístico com
# Movimento Vazio (AFND-e).
#
# Deve entregar uma matriz pronta para ser apresentada pela GUI como sendo
# o resultado da conversão acima citada.
#
# *******************************


class Converte():
    '''
    Responsável por receber a expressão regular infixa informada
     pelo usuário e convertê-la em expressão posfixa, também chamada
      de polonesa reversa.
    '''

    # atributos:
    pilha = []  # instancia uma lista (pilha) vazia

    expressao = input("\nInforme a expressão regular:\n")

    # chama getPosfixa do arquivo Trabalho_3.py
    # sobrescreve o valor de expressao com retorno de getPosfixa
    expressao = t1.getPosfixa(expressao)

    # chama montaPosfixa do arquivo Trabalho_3.py
    t1.montaPosfixa(expressao)
    # That's all folks!
