import re
from .base import FieldExtractor

class EmailExtractor(FieldExtractor):
    EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

    def extract(self, text: str) -> str:
        m = self.EMAIL_RE.search(text)
        return m.group(0) if m else ""
