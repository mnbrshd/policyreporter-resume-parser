from abc import ABC, abstractmethod
from typing import List

class LLMClient(ABC):
    @abstractmethod
    def extract_skills(self, resume_text: str) -> List[str]:
        pass