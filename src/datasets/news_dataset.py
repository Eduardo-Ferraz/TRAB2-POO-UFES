
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface


class NewsDataset(DatasetInterface):
    # ler arquivo contendo os nomes dos arquivos de noticias e as classes
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.path = path
        self.noticias = []
    
        with open(self.path) as f:
            for line in f:
                line = line.split()
                lastBar = self.path.rfind('/')
                
                notiPath = self.path[:lastBar+1] + line[0]
                notiClass = line[1]

                self.noticias.append([notiPath, notiClass])

    # retornar o numero de noticias no dataset (numero de linhas no arquivo)
    def size(self) -> int:
        return sum(1 for _ in self.noticias)

    # ler a i-esima noticia do disco e retornar o texto como uma string e
    # a classe
    def get(self, idx: int) -> Tuple[Any, str]:
        notiPath = self.noticias[idx][0]
        notiClass = self.noticias[idx][1]

        with open(notiPath) as f:
            notiContent = f.readlines()

        return notiContent, notiClass
