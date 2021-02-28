from abc import ABC, abstractmethod


class Reporter(ABC):
    def __init__(self, log: list[dict]):
        self._log = log

    @abstractmethod
    def generate_report(self) -> str:
        pass
