from simple_agent.prompts import CONVERSATION_INSTRUCTION
from simple_agent.config import cfg


from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.planners import BuiltInPlanner
from google.genai import types

from google import genai

root_agent = Agent(
    name=cfg.agent_settings.name,
    model=cfg.agent_settings.model,
    description=cfg.agent_settings.description,
    instruction=CONVERSATION_INSTRUCTION,
    generate_content_config=types.GenerateContentConfig(
        temperature=0.7,
        safety_settings=[
            types.SafetySetting(category=cat, threshold=thresh)
            for cat, thresh in cfg.agent_settings.safety_settings.items()
        ]
    ),
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
            thinking_budget=1024,
        )
    ),
    tools=[google_search]
)
