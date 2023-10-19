from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        raise NotImplementedError

    @abstractmethod
    def sleep(self):
        raise NotImplementedError


class Dog(Animal):
    __name = None

    def sound(self):
        print("ham ham")

    def sleep(self):
        print("la somn")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if self.__check_name(nume=name):
            self.__name = name

    @staticmethod
    def __check_name(nume):
        if nume == "":
            return False
        else:
            return True


x = Dog()
x.set_name("alex")
print(x.get_name())
