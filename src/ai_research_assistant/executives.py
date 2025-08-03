"""AI Executive roles for the Virtual Company Simulator."""

from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from .company_state import CompanyState, ExecutiveOpinion


class AIExecutive:
    """Base class for AI executives."""

    def __init__(self, openai_api_key: str | None = None):
        """Initialize the AI executive."""
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=SecretStr(openai_api_key) if openai_api_key else None,
            temperature=0.7,
        )

    def get_opinion(self, state: CompanyState) -> ExecutiveOpinion:
        """Get the executive's opinion on the current decision."""
        raise NotImplementedError


class CEOExecutive(AIExecutive):
    """Chief Executive Officer - focuses on overall strategy and leadership."""

    def get_opinion(self, state: CompanyState) -> ExecutiveOpinion:
        """Get CEO's strategic opinion."""
        decision = state["decision_details"]
        metrics = state["metrics"]

        prompt = f"""You are the CEO of {state["company_name"]}, a {state["company_size"]} company in the {state["industry"]} industry.
        
        Current Company Metrics:
        - Revenue: ${metrics["revenue"]:,}
        - Profit: ${metrics["profit"]:,}
        - Employee Count: {metrics["employee_count"]}
        - Market Share: {metrics["market_share"]:.1%}
        - Customer Satisfaction: {metrics["customer_satisfaction"]:.1f}/10
        
        Decision Being Considered:
        - Title: {decision["title"] if decision else "N/A"}
        - Description: {decision["description"] if decision else "N/A"}
        - Estimated Cost: ${decision["estimated_cost"]:,} if decision else 0
        - Expected ROI: {decision["expected_roi"]:.1%} if decision else 0
        - Risk Level: {decision["risk_level"] if decision else "N/A"}
        
        As CEO, provide your opinion focusing on:
        1. Strategic alignment with company vision
        2. Long-term impact on company growth
        3. Leadership and stakeholder considerations
        4. Overall business strategy
        
        Respond with:
        - Your opinion (2-3 sentences)
        - Your reasoning (3-4 sentences)
        - Your vote: "approve", "reject", or "abstain"
        - Priority score (1-10, where 10 is highest priority)
        
        Be decisive but consider all stakeholders including employees, customers, and shareholders."""

        messages = [
            SystemMessage(
                content="You are an experienced CEO making strategic business decisions."
            ),
            HumanMessage(content=prompt),
        ]

        response = self.llm.invoke(messages)
        content = str(response.content or "")

        # Parse the response (simplified parsing)
        lines = content.split("\n")
        opinion = ""
        reasoning = ""
        vote = "abstain"
        priority_score = 5

        for line in lines:
            if "opinion:" in line.lower():
                opinion = line.split(":", 1)[1].strip()
            elif "reasoning:" in line.lower():
                reasoning = line.split(":", 1)[1].strip()
            elif "vote:" in line.lower():
                vote_text = line.split(":", 1)[1].strip().lower()
                if "approve" in vote_text:
                    vote = "approve"
                elif "reject" in vote_text:
                    vote = "reject"
            elif "priority" in line.lower() and any(char.isdigit() for char in line):
                import re

                numbers = re.findall(r"\d+", line)
                if numbers:
                    priority_score = min(10, max(1, int(numbers[0])))

        # Fallback parsing if structured format not found
        if not opinion:
            opinion = content[:200] + "..." if len(content) > 200 else content
        if not reasoning:
            reasoning = "Strategic considerations based on company position and market dynamics."

        return ExecutiveOpinion(
            role="CEO",
            opinion=opinion,
            reasoning=reasoning,
            vote=vote,
            priority_score=priority_score,
        )


class CTOExecutive(AIExecutive):
    """Chief Technology Officer - focuses on technology and innovation."""

    def get_opinion(self, state: CompanyState) -> ExecutiveOpinion:
        """Get CTO's technology-focused opinion."""
        decision = state["decision_details"]
        metrics = state["metrics"]

        prompt = f"""You are the CTO of {state["company_name"]}, a {state["company_size"]} company in the {state["industry"]} industry.
        
        Current Technical Metrics:
        - Tech Debt Level: {metrics["tech_debt"]:.1f}/10
        - Employee Count: {metrics["employee_count"]} (consider tech team size)
        
        Decision Being Considered:
        - Title: {decision["title"] if decision else "N/A"}
        - Description: {decision["description"] if decision else "N/A"}
        - Category: {decision["category"] if decision else "N/A"}
        - Timeline: {decision["timeline"] if decision else "N/A"}
        
        As CTO, focus on:
        1. Technical feasibility and implementation challenges
        2. Impact on existing systems and infrastructure
        3. Innovation opportunities and competitive advantage
        4. Technical team capacity and skill requirements
        5. Long-term technical debt implications
        
        Provide your technical perspective with vote and priority score."""

        messages = [
            SystemMessage(content="You are an experienced CTO evaluating technical decisions."),
            HumanMessage(content=prompt),
        ]

        response = self.llm.invoke(messages)
        content = str(response.content or "")

        # Similar parsing logic as CEO
        opinion = content[:200] + "..." if len(content) > 200 else content
        reasoning = "Technical evaluation based on feasibility, infrastructure impact, and innovation potential."
        vote = "abstain"
        priority_score = 6

        # Simple vote extraction
        if "approve" in content.lower():
            vote = "approve"
        elif "reject" in content.lower():
            vote = "reject"

        return ExecutiveOpinion(
            role="CTO",
            opinion=opinion,
            reasoning=reasoning,
            vote=vote,
            priority_score=priority_score,
        )


class CMOExecutive(AIExecutive):
    """Chief Marketing Officer - focuses on marketing and customer experience."""

    def get_opinion(self, state: CompanyState) -> ExecutiveOpinion:
        """Get CMO's marketing-focused opinion."""
        decision = state["decision_details"]
        metrics = state["metrics"]

        prompt = f"""You are the CMO of {state["company_name"]}, a {state["company_size"]} company in the {state["industry"]} industry.
        
        Current Marketing Metrics:
        - Market Share: {metrics["market_share"]:.1%}
        - Customer Satisfaction: {metrics["customer_satisfaction"]:.1f}/10
        - Brand Value: {metrics["brand_value"]:.1f}/10
        
        Decision Being Considered:
        - Title: {decision["title"] if decision else "N/A"}
        - Description: {decision["description"] if decision else "N/A"}
        
        As CMO, evaluate based on:
        1. Impact on customer experience and satisfaction
        2. Brand positioning and market perception
        3. Competitive advantage in the market
        4. Customer acquisition and retention potential
        5. Marketing and sales implications
        
        Provide your marketing perspective with vote and priority score."""

        messages = [
            SystemMessage(
                content="You are an experienced CMO evaluating marketing and customer impact."
            ),
            HumanMessage(content=prompt),
        ]

        response = self.llm.invoke(messages)
        content = str(response.content or "")

        opinion = content[:200] + "..." if len(content) > 200 else content
        reasoning = (
            "Marketing evaluation focused on customer impact, brand value, and market positioning."
        )
        vote = "abstain"
        priority_score = 5

        if "approve" in content.lower():
            vote = "approve"
        elif "reject" in content.lower():
            vote = "reject"

        return ExecutiveOpinion(
            role="CMO",
            opinion=opinion,
            reasoning=reasoning,
            vote=vote,
            priority_score=priority_score,
        )


class CFOExecutive(AIExecutive):
    """Chief Financial Officer - focuses on financial impact and risk."""

    def get_opinion(self, state: CompanyState) -> ExecutiveOpinion:
        """Get CFO's financial opinion."""
        decision = state["decision_details"]
        metrics = state["metrics"]

        prompt = f"""You are the CFO of {state["company_name"]}, a {state["company_size"]} company in the {state["industry"]} industry.
        
        Current Financial Metrics:
        - Revenue: ${metrics["revenue"]:,}
        - Expenses: ${metrics["expenses"]:,}
        - Profit: ${metrics["profit"]:,}
        - Cash Flow: ${metrics["cash_flow"]:,}
        
        Decision Being Considered:
        - Title: {decision["title"] if decision else "N/A"}
        - Estimated Cost: ${decision["estimated_cost"]:,} if decision else 0
        - Expected ROI: {decision["expected_roi"]:.1%} if decision else 0
        - Risk Level: {decision["risk_level"] if decision else "N/A"}
        
        As CFO, analyze:
        1. Financial impact and ROI projections
        2. Budget implications and cash flow effects
        3. Financial risk assessment
        4. Cost-benefit analysis
        5. Impact on financial KPIs and investor relations
        
        Provide your financial perspective with vote and priority score."""

        messages = [
            SystemMessage(content="You are an experienced CFO evaluating financial decisions."),
            HumanMessage(content=prompt),
        ]

        response = self.llm.invoke(messages)
        content = str(response.content or "")

        opinion = content[:200] + "..." if len(content) > 200 else content
        reasoning = "Financial analysis considering ROI, cash flow impact, and risk assessment."
        vote = "abstain"
        priority_score = 7  # CFO often has high priority on financial decisions

        if "approve" in content.lower():
            vote = "approve"
        elif "reject" in content.lower():
            vote = "reject"

        return ExecutiveOpinion(
            role="CFO",
            opinion=opinion,
            reasoning=reasoning,
            vote=vote,
            priority_score=priority_score,
        )
