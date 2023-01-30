from math import sqrt


def get_distancia_euclidiana(vetor1, vetor2):
    assert len(vetor1) == len(vetor2)
    
    qtd_coordenadas = len(vetor2)

    soma = 0

    for idx_coordenada in range(qtd_coordenadas):
        soma += (float(vetor1[idx_coordenada]) - float(vetor2[idx_coordenada])) ** 2

    distancia = sqrt(soma)
    return distancia