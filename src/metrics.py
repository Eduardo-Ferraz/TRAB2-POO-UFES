
from typing import List


def accuracy(true_classes: List[str], predicted_classes: List) -> float:
    """ Calcula o percentual de acerto """
    qtd_vetores = len(predicted_classes)
    acertos = sum(1 for i in range(qtd_vetores)
                  if predicted_classes[i] == true_classes[i])

    resultado = acertos / qtd_vetores

    return resultado
