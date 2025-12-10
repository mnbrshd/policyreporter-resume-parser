from .base import FileParser
import docx

class WordParser(FileParser):
    def parse(self, file_path: str) -> str:
        doc = docx.Document(file_path)
        paragraphs = [p.text for p in doc.paragraphs if p.text]
        return "\n".join(paragraphs)