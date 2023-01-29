
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()

    def train(self, train_dataset: DatasetInterface) -> None:
        """ calcular os centroides por classe """
        classes = []
        vetoresAPCO = [] # vetoresAgrupadosPorClasseOrdenada
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
                
        """Algoritmo de teste pra exibir os centroides 'e' de forma visual(apenas para imagens)"""
        for e in range(len(self.centroides)):
            k = 0
            for i in range(28):
                for j in range(28):
                    teste = self.centroides[e][0][k]
                    print(f'{teste:.0f}', end=" ")
                    k+=1
                print('\n')
            print(self.centroides[e][1])
            print('\n')
        
        # print(classes)
        # print(vetoresAPCO[0][0])
        # foda,_  = train_dataset.get(30)
        # print(foda == vetoresAPCO[0][0])

        # print(self.centroides)
        # print(len(vetoresAPCO[0][0]))


    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        # for i in range(test_dataset.size()):

        return []
