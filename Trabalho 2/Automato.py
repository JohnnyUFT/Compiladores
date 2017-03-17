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
    # seria interessante construir um construtor típico para base?
    # a simples instanciação da classe já viria com a base pronta
    # que tal utilizar sobrecarga? é possível criar 2 construtores, para
    # instanciação da classe com e sem parâmetros?
    def __init__(self):
        #self.alfabeto = ""
        self.alfabeto = []# conjunto de simbolos
        self.estados = 0
        self.fTransicao = [[],[]]#matriz de duas dimensões
        self.estadoInicial = 0
        self.estadosFinais = []

    # métodos genéricos:
    def getAlfabeto(self):
        return self.alfabeto    
    
    def getEstados(self):
        return self.estados

    def getfTransicao(self):
        # a corrigir
        return self.matrizTransicao

    def getEstadoInicial(self):
        return self.estadoInicial

    def getEstadosFinais(self):
        return self.estadosFinais

    def setAlfabeto(self, alfabeto):
        self.alfabeto = alfabeto

    def setEstados(self, estados):
        self.estados = estados

    # deve receber todos os parâmetros necessários para que seja possível
    # modificar a função de transição:
    def setfTransicao(self, estados, alfabeto):
        # a corrigir
        #self.matrizTransicao = transicoes
        pass

    def setEstadoInicial(self, estadoInicial):
        self.estadoInicial = estadoInicial

    def setEstadosFinais(self, estadosFinais):
        self.estadosFinais = estadosFinais
    

    messagebox.askquestion("Dúvida","Tudo bem aí?")