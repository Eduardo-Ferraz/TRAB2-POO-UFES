
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface
import cv2


class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        # ler arquivo com os nomes das imagens e classes e armazenar em uma lista
        super().__init__(path)
        self.path = path
        self.images = []
    
        with open(self.path) as f:
            for line in f:
                line = line.split()
                lastBar = self.path.rfind('/')
                
                imgPath = self.path[:lastBar+1] + line[0]
                imgClass = line[1]

                self.images.append([imgPath, imgClass])

    def size(self) -> int:
        # retornar tamanho do dataset (numero de linhas do arquivo)
        return sum(1 for _ in self.images)
        
    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima imagem do disco usando a biblioteca cv2 e retornar
        # a imagem e a respectiva classe
        imgPath = self.images[idx][0]
        imgClass = self.images[idx][1]

        # Using cv2.imread() method
        # Using 0 to read image in grayscale mode
        img = cv2.imread(imgPath, 0)
        flatImage = [pixel for line in img for pixel in line]

        # Displaying the image
        # cv2.imshow('image', img)
        # cv2.waitKey()

        return flatImage, imgClass
