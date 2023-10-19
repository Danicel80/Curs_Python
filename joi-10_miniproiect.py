from abc import ABC, abstractmethod


class MInterface(ABC):

    @abstractmethod
    def descriere(self):
        raise NotImplementedError

    @abstractmethod
    def inmatriculare(self):
        raise NotImplementedError

    @abstractmethod
    def vopseste(self, culoare):
        raise NotImplementedError

    @abstractmethod
    def accelereaza(self, viteza):
        raise NotImplementedError

    @abstractmethod
    def franeaza(self):
        raise NotImplementedError


class Masina(MInterface):
    marca = ""
    model = ""
    __viteza_maxima = 0
    __viteza_actuala = 0
    __culoare = "gri"
    __culori_disponibile = ["rosu", "alb", "negru", "visiniu"]
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.viteza_maxima = viteza_maxima
        self.model = model

    def vopseste(self, culoare):
        if culoare in self.__culori_disponibile:
            self.__culoare = culoare
        else:
            raise Exception("Culoarea nu este in lista")

    def accelereaza(self, viteza):
        if 0 < viteza and viteza <= self.viteza_maxima:
            self.__viteza_actuala = viteza
        else:
            raise Exception("Viteza nu este ok")

    def descrie(self):
        pass

    def franeaza(self):
        pass

    def inmatriculare(self):
        pass

    def descriere(self):
        pass

m = Masina("Dacia", 220)
t = Masina("Renault", 1440)
print(m.viteza_maxima)
m.accelereaza(43)
