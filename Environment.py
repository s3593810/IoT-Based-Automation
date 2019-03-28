from abc import ABC, abstractmethod
class Environment(ABC):

    @abstractmethod
    def Read(self):
          pass

    @abstractmethod
    def Write(self):
          pass