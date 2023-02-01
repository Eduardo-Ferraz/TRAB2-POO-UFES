
from typing import Union, Dict, List
from src.datasets.dataset_interface import DatasetInterface
from src.classifiers.classifier_interface import ClassifierInterface
import time
from src.metrics import accuracy


class Experiment:
    def __init__(self,
                 train_dataset: DatasetInterface,
                 test_dataset: DatasetInterface):
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        self.true_classes = self._get_true_classes_from_dataset(
            self.test_dataset)

    def run(self, classifier: ClassifierInterface) -> Dict[str, float]:
        """ executa o experimento """
        startTrain = time.time()
        classifier.train(self.train_dataset)

        trainTime = time.time() - startTrain
        startPredict = time.time()
        # trainTime = float(date.time.now() - start) / self.train_dataset.size()

        pred_classes = classifier.predict(self.test_dataset)
        predictTime = time.time() - startPredict
        # predictTime = float(date.time.now() - trainTime) / self.test_dataset.size()

        metrics = {
            'accuracy': accuracy(self.true_classes, pred_classes),
            'trainTime': trainTime / self.train_dataset.size(),
            'predictTime': predictTime / self.test_dataset.size(),
        }

        return metrics

    def _get_true_classes_from_dataset(self, dataset: DatasetInterface) -> List[str]:
        true_classes = []
        for idx in range(dataset.size()):
            _, sample_class = dataset.get(idx) # _, descarta o primeiro valor e salva só a classe
            true_classes.append(sample_class)
        return true_classes
