
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface

SPACE = ' '
NO_CHAR = ''
NEW_LINE_CHAR = '\n'

class NewsDataset(DatasetInterface):
    # ler arquivo contendo os nomes dos arquivos de noticias e as classes
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.path = path
        self.noticias = []

        with open('data/datasets/stopwords.txt', 'r', encoding='utf-8') as stopwords_file:
            self._stop_words = stopwords_file.readlines()
            self._stop_words = [
                word.replace(NEW_LINE_CHAR, SPACE).replace(SPACE, NO_CHAR) 
                for word in self._stop_words
            ]

        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split()
                lastBar = self.path.rfind('/')

                notiPath = self.path[:lastBar+1] + line[0]
                notiClass = line[1]

                self.noticias.append([notiPath, notiClass])
                self.get(len(self.noticias) - 1)

    # retornar o numero de noticias no dataset (numero de linhas no arquivo)
    def size(self) -> int:
        return sum(1 for _ in self.noticias)

    # ler a i-esima noticia do disco e retornar o texto como uma string e
    # a classe
    def get(self, idx: int) -> Tuple[Any, str]:
        notiPath = self.noticias[idx][0]
        notiClass = self.noticias[idx][1]

        with open(notiPath) as f:
            notiContent = f.readlines()[0]

        palavras_relevantes_do_conteudo = self._limpar_conteudo(notiContent)

        return self._vetorizar_palavras(palavras_relevantes_do_conteudo), notiClass

    def _limpar_conteudo(self, full_content: str) -> list[str]:
        """Removes the stopwords, spaces, '\n' and returns a list of the remaining words"""
        all_words = full_content.replace(NEW_LINE_CHAR, SPACE).split(SPACE)
        all_words = [word for word in all_words if word not in self._stop_words]

        return all_words

    def _vetorizar_palavras(self, words: list[str]) -> dict:
        dict = {}

        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1

        return dict
