#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: November 2016

"""
from lib2to3.pgen2.tokenize import Whitespace

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import string

def automato():
    """
    Recebe a palavra informada, retira espaços e a envia para processamento em 'q0'.

    Este método trabalha como se fosse o método principal
    do projeto, ele recebe a palavra, já trabalhada sobre os espaços e envia a mesma
    para a função que verifica se há repetições, estando tudo certo, envia a palavra
     para o estado 'q0'.
    :return: void
    """
    alfabeto1 = removeEspacos() # remove os espaços em branco
    repetidos = verRepeticao(alfabeto1) # verifica repetição de símbolos
    if(not repetidos):
        q0(alfabeto1)  # começa pelo q0() pois é o estado inicial
    else:
        qErro()

def obterAlfabeto():
    """
    Captura a palavra que estiver na Entry e guarda-a numa String.

    Posteriormente, retorna a palavra para o método que a chamou.
    :return: str
    """
    print(ed1.get())  # teste dispensável
    alfabeto = ed1.get()  # guarda conteúdo lido numa string
    return alfabeto

def q0(alfabeto):
    """
    Implementa toda lógica necessária ao controle do estado inicial 'q0'.

    O primeiro símbolo do alfabeto deve ser, necessariamente
    um 'abre-chaves', do contrário, a entrada já é considerada errada.
    :param alfabeto: str
    :return: void
    """
    i = 0  # marca índice da string (cadeia de simbolos da fita)
    print("i em q0: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if ((alfabeto[i] == '{') and len(alfabeto) > 1):
        q1(alfabeto, i + 1)
    else:
        qErro()


def q1(alfabeto, i):
    """
    Implementação do estado 'q1'.

    Se o alfabeto informado estiver correto,
    o símbolo informado aqui, deverá ser exclusivamente alfanumérico.
    :param alfabeto: str
    :param i: int
    :return: void
    """
    print("i em q1: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if i <= len(alfabeto)-2:
        if verAlfaNumerico(alfabeto, i):
            q2(alfabeto, i+1)
        else:
            qErro()
    else:
        qErro()


def q2(alfabeto, i):
    """
    Implementação das regras definidas para estado 'q2'.

    Se o alfabeto informado estiver correto, o símbolo processado aqui
    deverá ser uma vírgula.
    :param alfabeto: str
    :param i: int
    :return: void
    """
    print("i em q2: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if i <= len(alfabeto)-1:
        if alfabeto[i] == ',' and i < len(alfabeto)-1:
            q1(alfabeto, i + 1)
        elif alfabeto[i] == '}' and i == len(alfabeto)-1: # não há mais simbolos na 'fita'
            q3(alfabeto, i) # chegamos ao último símbolo e este é uma vírgula
        else:
            qErro()
    else:
        qErro()


def q3(alfabeto, i):
    """
    Implementação das regras definidas para estado 'q3'.

    Este é o estado de aceitação. É nele que está contido o teste
    para confirmar se o alfabeto informado é aceito ou rejeitado.
    :param alfabeto: str
    :param i: int
    :return: void
    """
    print("i em q3: %i, alfabeto %s, simbolo %s" % (i, alfabeto, alfabeto[i]))
    if i == len(alfabeto)-1:
        messagebox.showinfo("Informação", "Alfabeto aceito!")
        # empilhando alfabeto dentro do listbox:
        indice = 0
        lbox1.insert(END, alfabeto)# falta colocar índice
        indice += indice
    else:
        qErro()


def qErro():
    """
    Estado de erro.

    Não faz nada a não ser, mostrar esta mensagem na tela e interromper
    o processo de transições entre os estados.
    :return: void
    """
    messagebox.showerror("Erro", "Faltam ou sobram parâmetros")

def removeEspacos():
    """
    Procura por todos os espaços e encontrando-os,
    troca-os por 'nada'.
    :return: str
    """
    alfabeto = obterAlfabeto().replace(" ", "")
    return alfabeto

def verRepeticao(alfabeto):
    """
    Verifica se há alfanuméricos repetidos no alfabeto.
    :param: alfabeto
    :return: boolean
    """
    tam = len(alfabeto)-1
    for i in range(tam):
        for j in range(i+1,tam,1):
            if(alfabeto[i] == alfabeto[j] and alfabeto[i] != ','):
                return True # encontrou símbolos repetidos
    return False # não encontrou repetição

def verAlfaNumerico(alfabeto, i):
    """
    Verifica se o símbolo recebido é alfanumérico.

    Este método testa se o símbolo está entre A,...,Z
                                           ou a,...,z
                                           ou 0,...,9
    :param alfabeto: str
    :param i: int
    :return: boolean
    """
    #print("Em verAlphaNumeric: %s, %d "%(alfabeto, i))
    if (ord(alfabeto[i]) >= 65 and ord(alfabeto[i]) <= 90) \
            or (ord(alfabeto[i]) >= 97 and ord(alfabeto[i]) <= 122) \
            or (ord(alfabeto[i]) >= 48 and ord(alfabeto[i]) <= 57):
        return True
    return False

def unirAlfabetos():
    """
    Refazer essa bagaça aqui.
    """
    i = lbox1.size()
    tupla1 = lbox1.get(0, i)# captura primeiro ao último elemento da lista
    palavra = str(tupla1)

    # tratamento para novo alfabeto:
    lista2 = []# declara lista vazia
    for i in range(len(palavra)):
        if (verAlfaNumerico(palavra, i)):
            lista2.append(palavra[i])
    conjunto1 = set(lista2)# garante a não repetição de elementos
    print(type(conjunto1))
    print(conjunto1)
    novaPalavra = '{' + ', '.join(conjunto1) + '}'
    # insere a uniao de símbolos, de volta á listbox
    lbox1.insert(END, novaPalavra)

def verificaPalavra():
    """
    Captura a palavra informada pelo usuário e verifica a quais alfabetos
    a mesma pertence.
    :return: void
    """
    # converte a palavra em um "conjunto" de caracteres, separados.
    palavra = ed2.get()
    i = lbox1.size() # captura o comprimento da listbox
    lista1 = lbox1.get(0, i)# captura tudo que há na listbox

    lista2 = []# apenas para guadar os indices dos alfabetos
    i = 1 # marca indice dos alfabetos
    for alfabeto in lista1:
        lidoOk = 0 # marca indice na palavra
        for simbolo in palavra:
            if(simbolo in alfabeto):
                lidoOk+=1
            if(lidoOk==len(palavra)):
                    lista2.append(i)
        i+=1
    if(lista2):
        messagebox.showinfo("Pertence", "Palavra pertence a %s"%lista2)
    else:
        messagebox.showerror("Não Pertence", "Palavra pertence a nenhum")

def prefixos():
    """
    Imprime os prefixos da palavra informada.
    :return: void
    """
    palavra = ed2.get()
    lista = [chr(38)]
    for i in range(1,len(palavra)+1):
        #print(palavra[:i])
        lista.append(palavra[:i])
    lista2 = sorted(set(lista), key=len)
    messagebox.showinfo("Prefixos", lista2)


def sufixos():
    """
    Imprime os sufixos da palavra informada.
    :return: void
    """
    palavra = ed2.get()
    lista = [chr(38)]
    for i in range(len(palavra)-1, -1, -1):
        lista.append(palavra[i:])
    # set: remove repetidos, sorted: ordena, por tamanho (key=len).
    lista2 = sorted(set(lista), key=len)
    messagebox.showinfo("Sufixos", lista2)

def subpalavras():
    """
    Imprime as subpalavras da palavra informada.
    :return: void
    """
    palavra = ed2.get()
    comp = len(palavra)
    lista = [chr(38)]
    for i in range(comp):
      for j in range(i,comp):
        lista.append(palavra[i:j+1])
    lista2 = sorted(set(lista), key=len)# elimina os repetidos e ordena por tamanho
    messagebox.showinfo("Subpalavras", lista2)

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
frame4 = Frame(Janela, width=100, bg="")

frame1.pack(side=TOP, fill=X)
frame2.pack(side=LEFT, fill=Y)
frame4.pack(side=RIGHT, fill=Y)
frame3.pack(fill=BOTH)

#  configuração de fonte, permanente para labels e outros
fonte1 = ('Monaco', '10')

lb1 = Label(frame1, text='UNIVERSIDADE FEDERAL DO TOCANTINS \n Ciência da Computação',
            font=('Monaco', '12', 'bold'), height=6)
lb1.pack()

#  elementos contidos no frame 3 (o do meio)
lb3 = Label(frame3, text="Entrada (alfabeto): ", font=fonte1)
ed1 = Entry(frame3, text="", font=fonte1)  # trabalhar a função obterAlfabeto - em outro arquivo, de preferência
bt1 = Button(frame3, text="Inserir", font=fonte1, command=automato)
lb4 = Label(frame3, text="Lista de alfabetos: ", font=fonte1)
lbox1 = Listbox(frame3, width=25, height=7)
bt2 = Button(frame3, text="Unir alfabetos ", font=fonte1, command=unirAlfabetos)
lb5 = Label(frame3, text="Palavra: ", font=fonte1)
ed2 = Entry(frame3, text="", font=fonte1)
bt3 = Button(frame3, text="Verificar", font=fonte1, command=verificaPalavra)
bt4 = Button(frame3, text="Prefixos", font=fonte1, command=prefixos)
bt5 = Button(frame3, text="Sufixos", font=fonte1, command=sufixos)
bt6 = Button(frame3, text="Subpalavras", font=fonte1, command=subpalavras)

#  disposição de todos os widgets do frame (conteiner) nº 3 (do meio)
lb3.grid(row=0, column=0, stick=W)
ed1.grid(row=1, column=0)
bt1.grid(row=1, column=1)
lb4.grid(row=2, column=0, stick=W)
lbox1.grid(row=3, column=0)
bt2.grid(row=4, column=0)  # as linhas do litbox não interferem nesta contagem
lb5.grid(row=5, column=0, stick=W)
ed2.grid(row=6, column=0)
bt3.grid(row=6, column=1)
bt4.grid(row=7, column=0, stick=W)
bt5.grid(row=7, column=1)
bt6.grid(row=7, column=2, stick=E)

Janela.title("Linguagens Formais & Autômatos - Trabalho #1")
#  Largura x Altura + Esquerda + Topo
Janela.geometry("620x510+300+100")
Janela.mainloop()
