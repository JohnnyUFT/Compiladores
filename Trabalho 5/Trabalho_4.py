# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
"""
from tkinter import messagebox
import Trabalho_3 as t3
import Main as principal
import Automato as auto
from Automato import *
import numpy as np  # para manipulação das matrizes
from collections import Counter # para manipulação dos dicionários
# import seaborn as sns

# *******************************
# Inicia-se o tratamento para classificar a entrada (código do usuário) em tokens;
# Esses tokens estão associados a estados finais de autômatos previamente definidos atra-
# vés de expressões regulares, já processadas pelos trabalhos 1, 2 e 3.
# *******************************

class getPalavras():
    print("Insira as palavras a serem classificadas:")
    palavra = input()
    print(palavra)





