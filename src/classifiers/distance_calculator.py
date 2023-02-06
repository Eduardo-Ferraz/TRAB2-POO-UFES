from math import sqrt
import numpy as np


def get_distancia_euclidiana(vetor1, vetor2):
    qtd_coordenadas = max(len(vetor1), len(vetor2))
    vetor1 = vetor1 + [0] * (qtd_coordenadas - len(vetor1))
    vetor2 = vetor2 + [0] * (qtd_coordenadas - len(vetor2))

    soma = 0
    for idx_coordenada in range(qtd_coordenadas):
        soma += (float(vetor1[idx_coordenada]) - float(vetor2[idx_coordenada])) ** 2

    distancia = sqrt(soma)
    return distancia
