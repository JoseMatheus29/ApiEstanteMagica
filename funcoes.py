from string import ascii_uppercase
from random import choice


def gerarCodigo():
    """=>A função gera o codigo automatico de cada livro 
        Não recebe paranmetro 
        Retorna o codigo"""
    letras = ascii_uppercase
    codigo = ''
    for i in range(0,6):
        codigo += choice(letras)
        i+=1
    return codigo