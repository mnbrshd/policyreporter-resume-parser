from abc import ABC, abstractmethod
from typing import Any

class FieldExtractor(ABC):
    @abstractmethod
    def extract(self, text: str) -> Any:
        pass