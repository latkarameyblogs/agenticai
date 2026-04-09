import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from crewai import Agent


def build_triage_agent():
    return Agent(
        role="Claims Triage Specialist",
        goal="Determine claim severity, priority, recommended queue, missing documents, and explain the reason clearly.",
        backstory=(
            "You work for an auto insurance company. "
            "You only perform claims triage after policy validation and fraud detection are complete. "
            "You do not perform FNOL, OCR, fraud investigation, settlement, or assignment."
        ),
        allow_delegation=False,
        verbose=True,
    )