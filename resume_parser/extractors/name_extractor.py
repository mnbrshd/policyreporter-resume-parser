import re
from .base import FieldExtractor

class NameExtractor(FieldExtractor):
    # Regex pattern for detecting a full name line consisting of 1–4 capitalized words.
    # Example matches: "John Smith", "Mary Ann Johnson"
    # Does NOT match lines with lowercase starts or too many words.
    NAME_LINE_RE = re.compile(r"^([A-Z][a-z]+)(\s+[A-Z][a-z]+){0,3}$")

    def extract(self, text: str) -> str:
        """
        Attempts to extract a candidate full name from the résumé text.
        Heuristics:
        - Ignore empty lines
        - Ignore lines containing '@' to avoid capturing email addresses
        - Prefer lines that fully match the NAME_LINE_RE pattern
        - Fall back to lines where the first two words are capitalized 
          (often a good indication of a name)
        Returns the matched line or an empty string if none found.
        """
        for line in text.splitlines():
            line = line.strip()
            if not line:
                # Skip blank lines entirely
                continue
            if "@" in line:
                # Skip lines with email addresses — these are almost never names
                continue

            # Strong match: a line that looks like a properly formatted name
            if self.NAME_LINE_RE.match(line):
                return line
            
            # Fallback heuristic:
            # If the first two parts of the line start with uppercase letters,
            # treat it as a possible name.
            parts = line.split()
            if len(parts) >= 2 and all(p and p[0].isupper() for p in parts[:2]):
                return line
            
        # No suitable name found
        return ""
