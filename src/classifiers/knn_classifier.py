
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class KnnClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()

    def train(self, train_dataset: DatasetInterface) -> None:
        # salvar as amostras do dataset
        # Cada imagem é um vetor de 28 vezes 28 coordenadas
        self.vetores = []
        for i in range(train_dataset.size()): 
            self.vetores.append(train_dataset.get(i))


    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """
        return []
