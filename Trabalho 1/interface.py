# !/usr/bin/python3.5
# -*- coding: utf-8 -*-
'''
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: March 2017
'''
import PIL
import tkinter as tk
from tkinter import*
from PIL import ImageTk, Image
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import ttk


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
lb3 = Label(frame6, image=photo, bg="")

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
