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

# *******************************

# 1ª FASE DO PROCESSO
# Aqui inicia-se o tratamento para transformar uma expressão infixa em posfixa.
# Implementação do Algoritmo nº 1

# *******************************
def expPosfixa():
    # variáveis globais
    pilha = []# pilha auxiliar
    posfixa = []# para receber expressão posfixa
    operadores = ['*','.','+']# em ordem de precedência

    palavra = ed1.get()

    # Verificação especial para simbolo de concatenação:
    # repare que a atribuição substitui o conteúdo anterior
    palavra = trataConcatenacao(palavra, operadores)
    #messagebox.showinfo("operador .","%s"%posf)


    # 1 - VARRER TODA A EXPRESSÃO CARACTERE POR CARACTERE ...
    for simbolo in palavra:
        # 1º caso: OPERANDO
        if(simbolo not in operadores and simbolo != '(' and simbolo != ')'):
            posfixa.append(simbolo)

        # 2º caso: PARÊNTESIS ABRINDO
        elif(simbolo == '('):
            pilha.append(simbolo)

        # 3º caso: PARÊNTESIS FECHANDO
        elif(simbolo == ')'):
            if pilha:# o mesmo que pilha not NULL
                while pilha[-1] != '(':
                    posfixa.append(pilha.pop())
                pilha.pop()
            else:# pilha está vazia
                messagebox.showinfo("Erro","Reveja parêntesis")
                # fechar aplicação
                Janela.quit()

        # 4º e último caso: OPERADOR
        else:
            while pilha:
                # teste de pecedência
                if(simbolo == '+' and pilha[-1] == '.' \
                   or simbolo == '+' and pilha[-1] == '*' \
                   or simbolo == '.' and pilha[-1] == '*' \
                   or simbolo == pilha[-1]):# pilha[-1] é o topo da pilha
                    posfixa.append(pilha.pop())
                else:
                    break
            pilha.append(simbolo)# empilhar o operador atual


    # 2 - ENQUANTO HOUVER OPERADOR NA PILHA ...
    while pilha and pilha[-1] in operadores:
        posfixa.append(pilha.pop())
    if(pilha):
        messagebox.showinfo("Erro", "Verifique os simbolos utilizados")
        # encerra execução do código
        Janela.quit()

    # a título de verificação:
    print("Pilha: %s"%pilha)
    print("Palavra: %s"%palavra)
    print("Posfixa %s"%posfixa)

    # converte uma vetor de simbolos em uma string
    palavra = ''.join(posfixa)

    # a título de verificação
    print("Como string %s"%palavra)

    ed2.insert(0,palavra)

    if(pilha):# se não está vazia, algo está errado
        messagebox.showerror("Erro", "Sobram operadores na pilha.")
        Janela.quit()
    else:
        print("Partindo para segunda fase...\n")

        segundoAlgoritmo(posfixa, operadores)

# *******************************

# A PARTIR DAQUI, INICIA-SE A FASE 2 DO PROCESSO
# Implementação do Algoritmo nº 2:

# *******************************

def segundoAlgoritmo(posfixa, operadores):
    pilha = []

    for simbolo in posfixa:
        # se simbolo é um operando
        if(simbolo not in operadores):
            pilha.append(simbolo)
        else:
            # se simbolo é um operador binário
            if(simbolo == '.' or simbolo == '+' and pilha):
                op2 = pilha.pop()
                if(pilha):
                    op1 = pilha.pop()
                    # transforma-os em uma única palavra (um único termo):
                    valor = op1+simbolo+op2
                    pilha.append(valor)
                else:
                    messagebox.showerror("Erro", "Falta operando.")
                    Janela.destroy()
            # se simbolo é um operador unário: '*'
            elif(simbolo == '*' and pilha):
                op1 = pilha.pop()
                valor = op1+simbolo
                pilha.append(valor)
    op1 = pilha.pop()
    if(not pilha):# isso está certo? if(pilha == null) ou if(not pilha)
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


def trataConcatenacao(palavra, operadores):
    '''
    Aqui a parada ficou sinistra,
    até altas horas!
    :param palavra:
    :param operadores:
    :return: palavra
    '''
    operadores.append('(')
    operadores.append(')')# acrescenta '(' e ')' aos operadores
    i = 0
    j = len(palavra)-1
    while(i<j):
        if(palavra[i] not in operadores and palavra[i+1] not in operadores \
                or palavra[i] not in operadores and palavra[i+1] == '(' \
                or palavra[i] == '*' and palavra[i+1] not in operadores \
                or palavra[i] == ')' and palavra[i+1] not in operadores \
                or palavra[i] == '*' and palavra[i+1] == '(' \
                or palavra[i] == ')' and palavra[i+1] == '('):
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
btn = Button(frame5, text="Converter", font=fonte1, command=expPosfixa)

# frame4 possui apenas uma imagem (caráter decorativo)
image = Image.open("cinema.png")
photo = ImageTk.PhotoImage(image)
lb3 = Label(frame6, image=photo, bg="white")

#  disposição de todos os widgets do frame (conteiner) nº 5 (do meio)
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
btn.grid(row=1, column=2, stick=W)

# disposição do widget do frame6
lb3.pack() # teste

Janela.title("Compiladores - Trabalho #1")
    #  Largura x Altura + Esquerda + Topo
Janela.geometry("650x510+300+100")
Janela.mainloop()
