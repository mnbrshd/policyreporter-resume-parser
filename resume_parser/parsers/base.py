from abc import ABC, abstractmethod

class FileParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> str:
        """
        Given path to a file, returns extracted text
        """
        pass

    