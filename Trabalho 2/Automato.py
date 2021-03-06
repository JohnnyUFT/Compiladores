# !/usr/bin/python3.5
# -*- coding: utf-8 -*-
"""
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
"""
import numpy as np

# *******************************
# 1ª FASE DO PROCESSO
# Definição da classe principal Automato()
#  juntamente com seus métodos e atributos#
# *******************************


class Automato:
    """
    Determina características intrínsecas do autômato: sendo este uma
    quíntupla, possui 5 atributos principais e outros 2 para controle de
    operações. Acompanha 'getters' para captura de valores e 'setters'
    para alteração dos valores anteriormente definidos.
    """

    # construtor
    def __init__(self):
        """
        Construtor padrão.
        """
        self.alfabeto = []  # conjunto de simbolos
        self.estados = []  # conjunto de estados
        self.mTransicao = np.matrix((None, None))  # matriz
        self.estadoInicial = 0
        self.estadoFinal = 1
        # self.qtdEstados = 0  # registra a quantidade de estados
        # self.qtdEstadoFinal = 0  # registra a quant. de estados finais

    # métodos genéricos:

    # definições para os getters:
    def getAlfabeto(self):
        return self.alfabeto

    def getEstados(self):
        return self.estados

    def getmTransicao(self):
        return self.mTransicao

    def getEstadoInicial(self):
        return self.estadoInicial

    def getEstadoFinal(self):
        return self.estadoFinal

    # def getQtdEstados(self):
    #    return self.qtdEstados

    # def getQtdEstadosFinais(self):
    #    return self.qtdEstadosFinais

    # definições para os setters:
    def setAlfabeto(self, alfabeto):
        self.alfabeto = alfabeto

    def setEstados(self, estados):
        self.estados = estados

    # modifica os valores da matriz de transição:
    def setmTransicao(self, mTransicao):
        self.mTransicao = mTransicao

    def setEstadoInicial(self, estadoInicial):
        self.estadoInicial = estadoInicial

    def setEstadoFinal(self, estadoFinal):
        self.estadoFinal = estadoFinal

    # def setQtdEstados(self, qtdEstados):
    #    self.qtdEstados = qtdEstados

    # def setQtdEstadosFinais(self, qtdEstadosFinais):
    #    self.qtdEstadosFinais = qtdEstadosFinais

    # métodos especiais:

    # necessário para controle da fTransicao
    def ehSimbolo(self, simbolo):
        """
        Recebe um simbolo e retorna a posição deste na 'coluna'
         de simbolos do alfabeto. Caso não exista tal simbolo na lista,
          retorna -1
        """
        for i in range(len(self.alfabeto)):
            if simbolo == self.alfabeto[i]:
                return i
        # só retorna -1 se não encontrar simbolo equivalente
        return -1

    def ehEstado(self, estado):
        """
        Recebe um estado como parâmetro e verifica se este pertence
        á lista de estados, caso verdade, retorna posição deste na lista,
        caso falso, retorna -1.
        """

        for i in range(len(self.estados)):
            if estado == self.estados[i]:
                return i
        # só retorna -1 se não encontrar estado equivalente
        return -1

    # VERIFICAR se está correto
    def ehEstadoFinal(self, estado):
        if estado in self.estadoFinal:
            return True
        else:
            return False

    def fTransicao(self, estado, simbolo):
        i = self.ehEstado(estado)
        j = self.ehSimbolo(simbolo)
        if (i and j) != -1:
            return self.mTransicao[[i], [j]]
        else:
            listaVazia = []
            # a corrigir
            return listaVazia

    # That's all folks!
