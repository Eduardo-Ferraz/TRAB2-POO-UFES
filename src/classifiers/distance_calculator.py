from math import sqrt
from random import triangular


def get_distancia_euclidiana(colecao_treino, colecao_predict):
    if (type(colecao_treino) == type([])):
        return get_dist_entre_vetores(colecao_treino, colecao_predict)
    
    else:
        return get_dist_entre_dicionarios(colecao_treino, colecao_predict)
    
    # são dicionarios
     

def get_dist_entre_dicionarios(treino: dict, predict: dict):
    soma = 0
    
    # set palavras inexistentes no predict
    for word in treino:
        if word not in predict:
            predict[word] = 0
    
    for word in predict:
        if word not in treino:
            treino[word] = 0
    
    for word in predict:
        soma += (float(treino[word]) - float(predict[word])) ** 2

    distancia = sqrt(soma)
    
    return distancia

def get_dist_entre_vetores(vetor1, vetor2):
    assert len(vetor1) == len(vetor2)
    
    qtd_coordenadas = len(vetor2)

    soma = 0

    for idx_coordenada in range(qtd_coordenadas):
        soma += (float(vetor1[idx_coordenada]) - float(vetor2[idx_coordenada])) ** 2

    distancia = sqrt(soma)
    return distancia
