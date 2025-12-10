from pathlib import Path
from typing import Dict
from .models import ResumeData
from .parsers.base import FileParser
from .resume_extractor import ResumeExtractor


class ResumeParserFramework:
    def __init__(self, parsers: Dict[str, FileParser], extractor: ResumeExtractor):
        self._parsers = {k.lower(): v for k, v in parsers.items()}
        self._extractor = extractor

    def parse_resume(self, file_path: str) -> ResumeData:
        suffix = Path(file_path).suffix.lower()
        print(file_path)
        parser = self._parsers.get(suffix)
        if not parser:
            raise ValueError(f"Unsupported file suffix: {suffix}")
        text = parser.parse(file_path)
        return self._extractor.extract(text)
