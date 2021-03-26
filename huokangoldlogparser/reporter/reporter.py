from abc import ABC, abstractmethod
from typing import List


class Reporter(ABC):
    def __init__(self, log: List[dict]):
        self._log = log

    @abstractmethod
    def generate_report(self) -> str:
        pass
