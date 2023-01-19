import openai
from openai.openai_object import OpenAIObject

from config import chat_config


class ChatGPT:
    """
    Класс ChatGPT
    """
    API_KEY: str = chat_config.get("token")

    def __init__(self):
        self.API = openai
        self.API.api_key = self.API_KEY

    async def create_completion(
            self,
            prompt: str,
            model: str = "text-davinci-003",
            max_tokens: int = 7,
            temperature: int = 0
    ) -> OpenAIObject:
        return await self.API.Completion.acreate(
            prompt=prompt,
            engine=model,
            max_tokens=max_tokens,
            temperature=temperature
        )
