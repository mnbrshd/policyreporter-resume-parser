from .base import FileParser
import pdfplumber
from loguru import logger


class PDFParser(FileParser):
    def parse(self, file_path: str) -> str:
        text_parts = []
        try:
            with pdfplumber.open(file_path) as pdf:
                for i, page in enumerate(pdf.pages, start=1):
                    try:
                        txt = page.extract_text()
                        if txt:
                            text_parts.append(txt)
                            logger.debug(
                                "Extracted text from PDF page",
                                file_path=file_path,
                                page_number=i,
                                length=len(txt),
                            )
                        else:
                            logger.debug(
                                "No text found on page",
                                file_path=file_path,
                                page_number=i,
                            )
                    except Exception as e:
                        # Unexpected error for this page, log and continue
                        logger.warning(
                            "Error extracting text from PDF page — skipping page",
                            file_path=file_path,
                            page_number=i,
                            error=str(e),
                        )
            result = "\n".join(text_parts)
            if not result.strip():
                logger.warning(
                    "Parsed PDF, but no text was extracted — result is empty",
                    file_path=file_path,
                )
            return result
        except Exception as e:
            # Catch-all for other pdfplumber/pdfminer errors
            logger.exception(
                "Unexpected exception while parsing PDF",
                file_path=file_path,
            )
            return ""