
from math import sqrt
from typing import Dict, List

from src.classifiers.distance_calculator import get_distancia_euclidiana
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class KnnClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()
        self.K = 5

    def train(self, train_dataset: DatasetInterface) -> None:
        # salvar as amostras do dataset
        # Cada imagem é um vetor de 28 vezes 28 coordenadas
        self.vetores_de_base = []
        for i in range(train_dataset.size()):
            self.vetores_de_base.append(train_dataset.get(i))
        
        print(self.vetores_de_base)

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """
        classes_preditas = [self._predict_amostra(
            test_dataset, idx_vetor) for idx_vetor in range(test_dataset.size())]

        return classes_preditas

    def _predict_amostra(self, test_dataset, idx_vetor):
        vetor_de_teste, _ = test_dataset.get(
            idx_vetor)  # vetor p/ calcular distancia

        distancias = []

        # Calcula a distancia do vetor de teste para os vetores de base
        for vetor_de_base, result in self.vetores_de_base:
            distancia = (get_distancia_euclidiana(
                vetor_de_base, vetor_de_teste), result)
            distancias.append(distancia)

        distancias.sort(key=lambda dist: dist[0])

        classes_vetores_proximos = [dist[1] for dist in distancias[:self.K]]

        classe_vetor_de_teste = max(
            set(classes_vetores_proximos),
            key=classes_vetores_proximos.count
        )

        return classe_vetor_de_teste
