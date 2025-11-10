import os
from dotenv import load_dotenv
from google.genai.types import HarmCategory, HarmBlockThreshold


class Config:
    class AgentSettings:
        model = "gemini-2.5-flash"
        name = "google_search_agent"
        description = "Professional search assistant with Google Search capabilities"
        dense_vector_size = 3072
        sparse_vector_size = 64
        # Configuración de seguridad para proteger contra contenido dañino
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        }

    agent_settings = AgentSettings()
cfg = Config()

