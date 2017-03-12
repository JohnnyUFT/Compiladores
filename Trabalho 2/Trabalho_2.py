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

import main

# *******************************
#
# Interface gráfica do Trabalho 2
# encarrega-se de apresentar conteúdos e
# cuida da entrada de dados.
# Interface com usuário
#
# *******************************

Janela = tk.Tk()  # instancia da Janela Principal (mainWindow)
"""
        Implementação da interface gráfica.

        Posteriomente, separar este método em uma classe
        e trabalhar com implementação OO e GUI.

"""

#  principais frames (conteiners) da tela principal
frame1 = Frame(Janela, height=100, bg="")# top frame
frame2 = Frame(Janela, width=100, bg="")# right - margem
frame3 = Frame(Janela, height=100, bg="")# middle frame - contém 2 frames (frame 5 e frame 6)
frame4 = Frame(Janela, width=100, bg="")# left frame - margem

frame5 = Frame(frame3, height=70, bg="")# main frame - contém os widgets
frame6 = Frame(frame3, height=70, bg="")# image frame - contém a imagem

frame1.pack(side=TOP, fill=X)
frame2.pack(side=LEFT, fill=Y)
frame4.pack(side=RIGHT, fill=Y)
frame5.pack(side=TOP, fill=X)
frame6.pack(side=TOP, fill=X)
frame3.pack(fill=BOTH)

#  configuração de fonte, permanente para labels e outros
fonte1 = ('Monaco', '10')
fonte2 = ('Monaco', '16')

lb1 = Label(frame1, text='UNIVERSIDADE FEDERAL DO TOCANTINS \n Ciência da Computação',
            font=('Monaco', '12', 'bold'), height=6)
lb1.pack()

#  elementos contidos no frame 3 (o do meio)
lb1 = Label(frame5, text="Informe expressão regular: ", font=fonte1)
ed1 = Entry(frame5, text="", font=fonte2)# inserir texto sugestivo
btn = Button(frame5, text="Converter em AFN-e", font=fonte1, command='main.Converte')# chamar classe principal

# frame4 possui apenas uma imagem (caráter decorativo)
image = Image.open("content1.png")
photo = ImageTk.PhotoImage(image)
lb3 = Label(frame6, image=photo, bg="white")

#  disposição de todos os widgets do frame (conteiner) nº 5 (do meio)
lb1.grid(row=0, column=0)
ed1.grid(row=1, column=0)
btn.grid(row=2, column=0, stick=W)

# disposição do widget do frame6
lb3.pack() # teste

Janela.title("Compiladores - Trabalho #2")
#  Largura x Altura + Esquerda + Topo
Janela.geometry("750x450+300+100")
Janela.mainloop()
