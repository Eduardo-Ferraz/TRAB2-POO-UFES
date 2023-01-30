
from src.datasets.dataset_factory import create_dataset
from src.classifiers.classifier_factory import create_classifier
from src.experiment import Experiment
from src.io.config import load_config
from src.io.report import write_report

from sys import argv


def main():
    CONFIG_PATH = './data/configs/'

    config = load_config(CONFIG_PATH + argv[1])

    train_dataset = create_dataset(config["train_path"], config["type"])
    test_dataset = create_dataset(config["test_path"], config["type"])
    classifier = create_classifier(config["classifier"])

    experiment = Experiment(train_dataset, test_dataset)
    metrics = experiment.run(classifier)

    # escreve o arquivo de saida
    write_report(CONFIG_PATH + argv[2], config, metrics)

    print(metrics['accuracy'])
    print("Success.")

if __name__ == "__main__":
    main()
