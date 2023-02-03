
from decimal import Decimal
from typing import Dict


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """

    lastBar = config['train_path'].rfind('/')
    datasetPath = config['train_path'][:lastBar+1]

    data = {
        'dataset': config['type'],
        'path': datasetPath,
        'classifier': config['classifier'],
        'training time per sample': f'{metrics_values["trainTime"]:.10f} s',
        'inference time per sample': f'{metrics_values["predictTime"]:.10f} s',
        'accuracy': f'{metrics_values["accuracy"]:.2f}',
    }

    f= open(path,"w+")

    [f.write(f'{key}: {value}\n') for key, value in data.items()]

    f.close()