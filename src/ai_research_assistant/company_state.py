"""State definitions for the Virtual Company Simulator."""

from typing import TypedDict


class CompanyMetrics(TypedDict):
    """Company financial and operational metrics."""

    revenue: int
    expenses: int
    profit: int
    cash_flow: int
    employee_count: int
    customer_satisfaction: float
    market_share: float
    tech_debt: float
    brand_value: float


class ExecutiveOpinion(TypedDict):
    """Individual executive's opinion on a decision."""

    role: str
    opinion: str
    reasoning: str
    vote: str  # "approve", "reject", "abstain"
    priority_score: int  # 1-10


class Decision(TypedDict):
    """A business decision being considered."""

    title: str
    description: str
    category: str  # "financial", "technical", "marketing", "strategic"
    impact_areas: list[str]
    estimated_cost: int
    expected_roi: float
    timeline: str
    risk_level: str  # "low", "medium", "high"


class CompanyState(TypedDict):
    """Complete state of the virtual company."""

    company_name: str
    industry: str
    company_size: str  # "startup", "growth", "enterprise"
    current_quarter: str

    # Current situation
    decision_topic: str
    decision_details: Decision | None

    # Company metrics
    metrics: CompanyMetrics

    # Executive opinions
    ceo_opinion: ExecutiveOpinion | None
    cto_opinion: ExecutiveOpinion | None
    cmo_opinion: ExecutiveOpinion | None
    cfo_opinion: ExecutiveOpinion | None

    # Meeting flow
    current_speaker: str
    discussion_phase: str  # "presentation", "discussion", "voting", "decision"
    meeting_minutes: list[str]

    # Final outcome
    final_decision: str | None
    decision_rationale: str | None
    implementation_plan: str | None

    # Error handling
    error_message: str | None
