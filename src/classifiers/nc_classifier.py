
from typing import Dict, List

from src.classifiers.distance_calculator import get_distancia_euclidiana
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()

    def train(self, train_dataset: DatasetInterface) -> None:
        """ calcular os centroides por classe """
        classes = []
        vetoresAPCO = []  # vetoresAgrupadosPorClasseOrdenada
        self.centroides = []
        somaPnesimaCoord = 0
        datasetSize = train_dataset.size()

        """ Pega todaclasses sem repetição e ordena em classes"""
        for i in range(datasetSize):
            _, classeAtual = train_dataset.get(i)

            if classeAtual not in classes:
                classes.append(classeAtual)
                vetoresAPCO.append([])

        classes.sort()

        """ Para cada vetor do dataset, da append nele em vetoresAPCO de acordo com a classe"""
        for i in range(datasetSize):
            vetor, classeAtual = train_dataset.get(i)

            for j in range(len(classes)):
                if classeAtual == classes[j]:
                    vetoresAPCO[j].append(vetor)
                    break

        """Para cada Classe c, para cada Coordenada x, para cada vetor v...."""
        for c in range((len(classes))):
            self.centroides.append(([], classes[c]))
            for x in range(len(vetoresAPCO[0][0])):
                for v in range(len(vetoresAPCO[0])):
                    somaPnesimaCoord += vetoresAPCO[c][v][x]
                mediaPnesimaCoord = somaPnesimaCoord / len(vetoresAPCO[0][0])
                self.centroides[c][0].append(mediaPnesimaCoord)
                somaPnesimaCoord = 0

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        classes_preditas = []

        for idx_vetor in range(test_dataset.size()):
            vetor_teste, _ = test_dataset.get(idx_vetor)

            distancias = []

            for centroide in self.centroides:
                distancias.append((get_distancia_euclidiana(
                    vetor_teste, centroide[0]), centroide[1]))

            distancias.sort(key=lambda x: x[0])
            mais_proximo = distancias[0]

            classes_preditas.append(mais_proximo[1])

        return classes_preditas
