''' Information regarding one module of a program '''

from abc import ABCMeta
from abc import abstractmethod


class Module(metaclass=ABCMeta):
    ''' Represents information describing one module of a program '''

    @abstractmethod
    def moduleName(self):
        raise NotImplementedError

    @abstractmethod
    def moduleUses(self):
        raise NotImplementedError

    @abstractmethod
    def modificationTime(self):
        raise NotImplementedError

    @abstractmethod
    def compilationTime(self):
        raise NotImplementedError

    @abstractmethod
    def compilationMode(self):
        raise NotImplementedError
