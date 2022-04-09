from abc import ABC, abstractmethod


class Money(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def acceptable(self):
        pass