from abc import ABC, abstractmethod


class Reporter(ABC):
    def __init__(self, log: list):
        self._log = log

    @abstractmethod
    def generate_report(self):
        pass
