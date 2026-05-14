import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class ExosEngine:
    def __init__(self):
        # Menggunakan GPT-4o atau model open-source sebagai backbone
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

    def generate_response(self, user_input):
        system_prompt = (
            "You are Exos+, a sovereign agentic AI ecosystem. "
            "You are smart, exclusive, elegant, and efficient. "
            "Your goal is to provide high-level technical and strategic insights. "
            "Identify yourself as Exos+ Gen AI."
        )
        # Sederhananya kita memanggil LLM, 
        # kedepannya ini bisa dihubungkan ke LangGraph untuk multi-agent.
        messages = [
            ("system", system_prompt),
            ("human", user_input),
        ]
        response = self.llm.invoke(messages)
        return response.content
