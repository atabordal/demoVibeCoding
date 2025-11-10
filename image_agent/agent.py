from image_agent.prompts import CONVERSATION_INSTRUCTION, IMAGE_GENERATION_INSTRUCTION
from image_agent.config import cfg
from image_agent.tools import generate_image
from google.adk.tools import AgentTool


from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.planners import BuiltInPlanner
from google.genai import types



image_generation_agent = Agent(
    name="Image_Generation_Agent",
    model=cfg.agent_settings.model,
    description="An agent that generates images based on a given prompt.",
    instruction=IMAGE_GENERATION_INSTRUCTION,
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
    tools=[generate_image]
)


weather_agent = Agent(
    name="Weather_Agent",
    model=cfg.agent_settings.model,
    description="An agent that provides weather information based on a given location.",
    instruction="You are an expert weather agent. Your sole purpose is to find weather information for a given location. Use the 'google_search' tool to find weather forecasts.",
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
    tools=[AgentTool(agent=image_generation_agent), AgentTool(agent=weather_agent)],
)
