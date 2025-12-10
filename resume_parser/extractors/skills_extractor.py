from typing import List
from .base import FieldExtractor
from .llm_client.clients import OpenAILLMClient

class SkillsExtractor(FieldExtractor):
    def __init__(self, llm_client: OpenAILLMClient):
        self._client = llm_client

    async def extract(self, text: str) -> List[str]:
        skills = await self._client.extract_skills(text)
        
        return skills