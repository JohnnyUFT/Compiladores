# !/usr/bin/python3.5
# -*- coding: utf-8 -*-
# shift+ctrl+b - to run code in atom
'''
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
'''
import PIL
import tkinter as tk
from tkinter import*
import string
from PIL import ImageTk, Image
from tkinter import PhotoImage
import sys
from tkinter import messagebox
from tkinter import ttk

# *******************************
# Aqui inicia-se o tratamento para transformar uma expressão infixa em posfixa.
# Implementação do Algoritmo nº 1
# *******************************
def principal():
    '''
    Captura a expressão na forma infixa
    e envia-a para o método trataConcatenacao afim de verificar a
    necessidade de colocar o ponto de concatenação.
    Na sequência, chama algoritmo que transforma expressão infixa em posfixa.
    :return: none
    '''

    palavra = ed1.get()

    # Verificação especial para simbolo de concatenação:
    palavra = trataConcatenacao(palavra)

    getPosfixa(palavra)

def getPosfixa(palavra):
    '''
    Transforma expressão infixa em posfixa.
    Esse algoritmo foi dado pelo profº Alexandre Rossini.
    :param palavra:
    :return: none
    '''
    # variáveis globais
    pilha = []# pilha auxiliar
    posfixa = []# para receber expressão posfixa
    operadores = ['*', '.', '+']# em ordem de precedência
    cont = 0 # para controle dos parêntesis

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
            while pilha:
                if pilha[-1] != '(':
                    posfixa.append(pilha.pop())
                else:
                    pilha.pop()

        # 4º e último caso: OPERADOR
        elif simbolo in operadores:
            while pilha:
                if simbolo == '+' and pilha[-1] == '.'\
                    or simbolo == '+' and pilha[-1] == '*'\
                    or simbolo == '.' and pilha[-1] == '*'\
                    or simbolo == pilha[-1]:
                    posfixa.append(pilha.pop())
                else:
                    break
            pilha.append(simbolo)  # empilhar o operador atual


    # 2 - ENQUANTO HOUVER OPERADOR NA PILHA ...
    while pilha:
        print("Debugue manual %s"%pilha)
        posfixa.append(pilha.pop())


    # a título de verificação:
    print("Pilha: %s"%pilha)
    print("Palavra: %s"%palavra)
    print("Posfixa %s"%posfixa)

    # converte uma vetor de simbolos em uma string
    palavra = ''.join(posfixa)

    # a título de verificação
    print("Como string %s"%palavra)

    montaPosfixa(posfixa, operadores, palavra, cont)

# *******************************
# Implementação do Algoritmo nº 2:
# recebe a expressão posfixa e tenta montá-la (resolvê-la)
# *******************************

def montaPosfixa(posfixa, operadores, palavra, cont):
    '''
    Tenta 'resolver' a expressão regular em sua forma posfixa.
    Obviamente, não deve conseguir fazer isso, e o resultado da
    resolução é apenas ignorado. Todavia, trata de verificar a
     expressão quanto o correto uso de operandos e operadores.
    :param posfixa:
    :param operadores:
    :param palavra:
    :param cont:
    :return: none
    '''
    pilha = []

    for simbolo in posfixa:
        # se simbolo é um operando
        if(simbolo not in operadores):
            pilha.append(simbolo)
        else:
            # se simbolo é um operador binário
            if simbolo == '.' or simbolo == '+' and pilha:
                op2 = pilha.pop()
                if(pilha):
                    op1 = pilha.pop()
                    # transforma-os em uma única palavra (um único termo):
                    valor = op1+simbolo+op2
                    pilha.append(valor)
                else:
                    messagebox.showerror("Erro", "Falta operando.")

            # se simbolo é um operador unário: '*'
            else:
                if simbolo == '*' and pilha:
                    op1 = pilha.pop()
                    valor = op1+simbolo
                    pilha.append(valor)
    op1 = pilha.pop()
    if not pilha and cont == 0:
        ed2.insert(0, palavra)
        messagebox.showinfo("Muito bem", "Expressão Aceita.")

        print("Resultado: %s"%op1)

        # limpa os campos
        ed1.delete(0, END)
        ed2.delete(0, END)
    else:
        messagebox.showerror("Erro", "Expresão Rejeitada.")

        # limpa os campos
        ed1.delete(0, END)
        ed2.delete(0, END)


def trataConcatenacao(palavra):
    '''
    Verifica necessidade de explicitar os operadores
     de concatenação nas expressões dadas.
    :param palavra:
    :param operadores:
    :return: palavra
    '''
    # declaração das varíaveis
    operadores = ['*', '.', '+', '(', ')']# em ordem de precedência
    i = 0
    j = len(palavra)-1

    while i<j:
        if palavra[i] not in operadores and palavra[i+1] not in operadores \
                or palavra[i] not in operadores and palavra[i+1] == '(' \
                or palavra[i] == '*' and palavra[i+1] not in operadores \
                or palavra[i] == ')' and palavra[i+1] not in operadores \
                or palavra[i] == '*' and palavra[i+1] == '(' \
                or palavra[i] == ')' and palavra[i+1] == '(':
            palavra = palavra[:i+1]+'.'+palavra[i+1:]# funciona lindamente
            j = len(palavra)-1
        i+=1
    return palavra

# *******************************
# INTERFACE GRÁFICA DO PROGRAMA, QUE É A FUNCAO PRINCIPAL
# *******************************
Janela = tk.Tk()  # instancia da Janela Principal (mainWindow)
"""
        Implementação da interface gráfica.

        Posteriomente, separar este método em uma classe
        e trabalhar com implementação OO e GUI.

"""

#  principais frames (conteiners) da tela principal
frame1 = Frame(Janela, height=100, bg="")
frame2 = Frame(Janela, width=100, bg="")
frame3 = Frame(Janela, height=100, bg="")
frame4 = Frame(Janela, width=100, bg="")  # frame externo delimitador principal

frame5 = Frame(frame3, height=70, bg="")  # frame5 interno (principal mesmo)
frame6 = Frame(frame3, height=70, bg="")  # frame6 imagem

frame1.pack(side=TOP, fill=X)
frame2.pack(side=LEFT, fill=Y)
frame4.pack(side=RIGHT, fill=Y)
frame5.pack(side=TOP, fill=X)  # para pegar tudo que puder, em relação ao eixo X do pai (frame 3)
frame6.pack(side=TOP, fill=X)
frame3.pack(fill=BOTH)

    #  configuração de fonte, permanente para labels e outros
fonte1 = ('Monaco', '10')
fonte2 = ('Monaco', '16')

lb1 = Label(frame1, text='UNIVERSIDADE FEDERAL DO TOCANTINS \n Ciência da Computação',
                font=('Monaco', '12', 'bold'), height=6)
lb1.pack()

    #  elementos contidos no frame 3 (o do meio)
lb1 = Label(frame5, text="Infixa: ", font=fonte1)
lb2 = Label(frame5, text="Posfixa: ", font=fonte1)
ed1 = Entry(frame5, text="", font=fonte2)
ed2 = Entry(frame5, text="", font=fonte2)
btn = Button(frame5, text="Converter", font=fonte1, command=principal)

# frame4 possui apenas uma imagem (caráter decorativo)
image = Image.open('cinema.png')
photo = ImageTk.PhotoImage(image)
lb3 = Label(frame6, image=photo, bg="white")

#  disposição de todos os widgets do frame (conteiner) nº 5 (do meio)
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
btn.grid(row=1, column=2, stick=W)

# disposição do widget do frame6
lb3.pack()

Janela.title("Compiladores - Trabalho #1")
    #  Largura x Altura + Esquerda + Topo
Janela.geometry("650x510+300+100")
Janela.mainloop()
