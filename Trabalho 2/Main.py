# !/usr/bin/python3.5
# -*- coding: utf-8 -*-

'''
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
'''

import sys
from Trabalho_1 import*
import Trabalho_1 as t1

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

    expressao = input("Informe a expressão regular:\n")

    # chama getPosfixa do Trabalho_1
    # sobrescreve o valor de expressao com retorno de getPosfixa
    expressao = t1.getPosfixa(expressao)

    # chama montaPosfixa do Trabalho_1
    t1.montaPosfixa(expressao)

    
    # That's all folks!
