#/usr/lib64/python3.5
# -*- coding: utf-8 -*-

'''
author: Eufrázio Alexandre & Johnny Pereira
email: (eufrazius,johnnyuft)@gmail.com
last modified: May 2017
'''

import Trabalho_5 as t5
from Trabalho_5 import *


# *******************************
#
#
# *******************************


class main():
    """
    Controla fluxo de informações para métodos First() e Follow();
    Inclui tratamentos sobre arquivo lido.
    """
    fout = open('ll1.txt', 'rt') # abre arquivo ll1, no modo 'r'ead 't'ext
