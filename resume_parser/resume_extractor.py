from typing import Dict
from .models import ResumeData
from .extractors.base import FieldExtractor

class ResumeExtractor:
    def __init__(self, extractors: Dict[str, FieldExtractor]):
        self._extractors = extractors

    async def extract(self, text: str) -> ResumeData:
        name = self._extractors["name"].extract(text) if "name" in self._extractors else ""
        email = self._extractors["email"].extract(text) if "email" in self._extractors else ""
        skills = await self._extractors["skills"].extract(text) if "skills" in self._extractors else ""

        return ResumeData(name=name, email=email, skills=skills)