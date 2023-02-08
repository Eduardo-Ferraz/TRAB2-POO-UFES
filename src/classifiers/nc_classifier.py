
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

        if type(vetoresAPCO[0][0]) == type([]):
            self._calculo_centroide_vetor(classes, vetoresAPCO)
        else:
            self._calculo_centroide_dicionario(classes, vetoresAPCO)

    def _calculo_centroide_dicionario(self, classes, vetoresAPCO):
        for idx_classe in range((len(classes))):
            centroide = {}
                
            for idx_dicionario in range(len(vetoresAPCO[idx_classe])):
                for dicionario in vetoresAPCO[idx_classe][idx_dicionario]:
                    for palavra in dicionario:
                        if palavra in list(centroide.keys()):
                            centroide[palavra] += 1
                        else:
                            centroide[palavra] = 1

            for key in centroide:
                total_dicionarios = len(vetoresAPCO[idx_classe])

                    # substituindo soma por media
                centroide[key] = centroide[key] / total_dicionarios

            self.centroides.append((centroide, classes[idx_classe]))

    def _calculo_centroide_vetor(self, classes, vetoresAPCO):
        for idx_classe in range((len(classes))):
            self.centroides.append(([], classes[idx_classe]))
                
            for vetor in range(len(vetoresAPCO[0][0])):
                soma_coordenada = 0

                for idx_dicionario in range(len(vetoresAPCO[0])):
                    colecao = vetoresAPCO[idx_classe][idx_dicionario]
                    soma_coordenada += colecao[vetor]

                mediaPnesimaCoord = soma_coordenada / len(vetoresAPCO[0][0])

                self.centroides[idx_classe][0].append(mediaPnesimaCoord)


    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        classes_preditas = []

        for idx_vetor in range(test_dataset.size()):
            vetor_teste, _ = test_dataset.get(idx_vetor)

            distancias = []

            for centroide in self.centroides:
                distancias.append((
                    get_distancia_euclidiana(centroide[0], vetor_teste), 
                    centroide[1])
                )

            distancias.sort(key=lambda x: x[0])
            mais_proximo = distancias[0]

            classes_preditas.append(mais_proximo[1])

        return classes_preditas
