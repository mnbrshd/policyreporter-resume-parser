from fastapi import FastAPI, UploadFile, File, HTTPException
import tempfile
import os
from pathlib import Path

from resume_parser.parsers.pdf_parser import PDFParser
from resume_parser.parsers.word_parser import WordParser
from resume_parser.extractors.name_extractor import NameExtractor
from resume_parser.extractors.email_extractor import EmailExtractor
from resume_parser.extractors.skills_extractor import SkillsExtractor
from resume_parser.extractors.llm_client.clients import OpenAILLMClient
from resume_parser.resume_extractor import ResumeExtractor
from resume_parser.framework import ResumeParserFramework
from resume_parser.models import ResumeData

from resume_parser.logging_setup import init_logging
from loguru import logger

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Initialize logging (console + file)
init_logging(log_file="resume_parser.log", level="INFO")

app = FastAPI(title="Resume Parsing API")
logger.info("Starting Resume Parser API")

parsers = {
    ".pdf": PDFParser(),
    ".docx": WordParser(),
}
llm_client = OpenAILLMClient(
    model="gpt-4.1-nano",
)

extractors = {
    "name": NameExtractor(),
    "email": EmailExtractor(),
    "skills": SkillsExtractor(llm_client=llm_client),
}
resume_extractor = ResumeExtractor(extractors)
framework = ResumeParserFramework(parsers=parsers, extractor=resume_extractor)


@app.post("/parse-resume/", response_model=ResumeData)
async def parse_resume(file: UploadFile = File(...)):
    suffix = Path(file.filename).suffix.lower()
    logger.info("Received file for parsing", filename=file.filename, suffix=suffix)
    if suffix not in parsers:
        logger.warning("Unsupported file type", suffix=suffix)
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {suffix}")

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name
    logger.debug("Saved uploaded file to temp path", temp_path=tmp_path)

    try:
        resume: ResumeData = await framework.parse_resume(tmp_path)

        logger.info(
            "Parsed resume successfully",
            name=resume.name,
            email=resume.email,
            skills=resume.skills,
        )
    except Exception as e:
        logger.exception("Failed to parse resume")
        raise HTTPException(status_code=500, detail=f"Error parsing resume: {e}")
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            logger.warning("Failed to remove temp file", path=tmp_path)

    return resume
