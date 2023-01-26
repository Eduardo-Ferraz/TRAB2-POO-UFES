

from typing import Dict
import json

""" le o arquivo json e retorna como um dicionario """
def load_config(path: str) -> Dict:
    with open(path) as jsonFile:
        return json.load(jsonFile)