# !/usr/bin/python3.5
# -*- coding: utf-8 -*-

'''
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
'''
from tkinter import*
import tkinter as tk
import string
import PIL
from PIL import ImageTk, Image
from tkinter import PhotoImage
import sys
from tkinter import messagebox
from tkinter import ttk
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
    # atributos:
    pilha = []# instancia uma lista (pilha) vazia

    expressao = input("Infrome a expressão regular:\n")

    # chama getPosfixa do Trabalho_1
    # sobrescreve o valor de expressão com retorno de getPosfixa
    expressao = t1.getPosfixa(expressao)

    # chama montaPosfixa do Trabalho_1
    t1.montaPosfixa(expressao)

    # é necessário implementar esse cara!
    # precisa fazer isso aqui?
    def ehSimbolo(self, simbolo):
        pass

    def ehEstado(self, estado):
        pass

    messagebox.askquestion("Tudo","Tudo bem?")