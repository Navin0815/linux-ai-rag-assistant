"""
LLM Module
Connects to Ollama.
"""

from langchain_community.llms import Ollama


class LLM:

    def __init__(self):

        self.llm = Ollama(
            model="llama3:latest"
        )

    def get_model(self):

        return self.llm