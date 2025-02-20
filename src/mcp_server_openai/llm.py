import logging
from openai import AsyncOpenAI

logger = logging.getLogger(__name__)

class LLMConnector:
    def __init__(self, openai_api_key: str):
        self.client = AsyncOpenAI(api_key=openai_api_key)

    async def ask_openai(self, query: str, model: str = "o3-mini") -> str:
        try:
            messages = [
                {
                    "role": "developer",
                    "content": "You are a helpful assistant that provides clear and accurate technical responses."
                },
                {
                    "role": "system",
                    "content": "Ensure responses are well-structured and technically precise."
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
            response = await self.client.chat.completions.create(
                messages=messages,
                model=model
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Failed to query OpenAI: {str(e)}")
            raise
