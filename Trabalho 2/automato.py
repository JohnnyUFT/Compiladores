# !/usr/bin/python3.5
# -*- coding: utf-8 -*-

'''
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
'''

import string
import PIL
import sys
from tkinter import messagebox

# *******************************

# 1ª FASE DO PROCESSO
# Definição da classe principal Automato()
#  juntamente com seus métodos e atributos
#
# *******************************
class Automato:
    # método construtor
    def __init__(self):
        self.alfabeto = ""
        self.estados = 0
        self.matrizTransicao = []#era para ser uma matriz
        self.estadoInicial = 0
        self.estadosFinais = []

    # métodos genéricos:
    def getAlfabeto(self):
        return self.alfabeto    
    
    def getEstados(self):
        return self.estados

    def getTransicoes(self):
        # a corrigir
        return self.matrizTransicao

    def getEstadoInicial(self):
        return self.estadoInicial

    def getEstadosFinais(self):
        return self.estadosFinais

    def setAlfabeto(self,alfabeto):
        self.alfabeto = alfabeto

    def setEstados(self,estados):
        self.estados = estados 

    def setTransicoes(self,transicoes):
        # a corrigir
        self.matrizTransicao = transicoes

    def setEstadoInicial(self,estadoInicial):
        self.estadoInicial = estadoInicial

    def setEstadosFinais(self,estadosFinais):
        self.estadosFinais = estadosFinais

    messagebox.askquestion("Dúvida","Tudo bem aí?")