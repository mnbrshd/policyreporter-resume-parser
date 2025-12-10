from .base import LLMClient
from typing import List, Optional

import os
from agents import Agent, Runner
import json_repair
import json
    

class OpenAILLMClient(LLMClient):
    """
    LLM client that uses OpenAI Agents SDK to extract skills from resume text.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-4.1-nano",
    ) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self._model = model
        

    async def extract_skills(self, resume_text: str) -> List[str]:
        agent = Agent(
            name="ResumeSkillExtractor",
            instructions=(
                "Given the full text of a resume, "
                "return a JSON list of skills (programming languages, frameworks, tools, "
                "ML skills, etc.). Respond with JSON only."
            ),
            model=self._model,
        )
        result = await Runner.run(agent, input=resume_text)

        try:
            skills = json_repair.loads(result.final_output)
            
        except json.JSONDecodeError:
            return []
        if isinstance(skills, list) and all(isinstance(s, str) for s in skills):
            return skills
        return []