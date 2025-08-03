"""State definitions for the AI Research Assistant."""

from typing import TypedDict


class ResearchState(TypedDict):
    """State for research workflow."""

    question: str
    research_plan: str | None
    collected_info: list[str]
    analysis: str | None
    final_report: str | None
    current_step: str
    error_message: str | None
