"""Virtual Company Simulator with AI Executive Board Meetings."""

import os
from typing import Any, cast

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from pydantic import SecretStr

from .company_state import CompanyState, CompanyMetrics, Decision
from .executives import CEOExecutive, CTOExecutive, CMOExecutive, CFOExecutive


class VirtualCompanySimulator:
    """Virtual company simulator with AI executive board meetings."""

    def __init__(self, openai_api_key: str | None = None):
        """Initialize the company simulator."""
        self.api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required")

        # Initialize executives
        self.ceo = CEOExecutive(self.api_key)
        self.cto = CTOExecutive(self.api_key)
        self.cmo = CMOExecutive(self.api_key)
        self.cfo = CFOExecutive(self.api_key)

        # Initialize facilitator LLM for meeting management
        self.facilitator = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=SecretStr(self.api_key) if self.api_key else None,
            temperature=0.3,
        )

        self.workflow = self._build_workflow()

    def _build_workflow(self) -> Any:
        """Build the LangGraph workflow for board meetings."""
        workflow = StateGraph(CompanyState)

        # Add meeting workflow nodes
        workflow.add_node("present_decision", self._present_decision)
        workflow.add_node("collect_ceo_opinion", self._collect_ceo_opinion)
        workflow.add_node("collect_cto_opinion", self._collect_cto_opinion)
        workflow.add_node("collect_cmo_opinion", self._collect_cmo_opinion)
        workflow.add_node("collect_cfo_opinion", self._collect_cfo_opinion)
        workflow.add_node("facilitate_discussion", self._facilitate_discussion)
        workflow.add_node("vote_and_decide", self._vote_and_decide)
        workflow.add_node("create_implementation_plan", self._create_implementation_plan)

        # Define the meeting flow
        workflow.set_entry_point("present_decision")
        workflow.add_edge("present_decision", "collect_ceo_opinion")
        workflow.add_edge("collect_ceo_opinion", "collect_cto_opinion")
        workflow.add_edge("collect_cto_opinion", "collect_cmo_opinion")
        workflow.add_edge("collect_cmo_opinion", "collect_cfo_opinion")
        workflow.add_edge("collect_cfo_opinion", "facilitate_discussion")
        workflow.add_edge("facilitate_discussion", "vote_and_decide")
        workflow.add_edge("vote_and_decide", "create_implementation_plan")
        workflow.add_edge("create_implementation_plan", END)

        return workflow.compile()

    def _present_decision(self, state: CompanyState) -> dict[str, Any]:
        """Present the decision to be discussed."""
        try:
            decision = state["decision_details"]
            if not decision:
                return {"error_message": "No decision provided for discussion"}

            presentation = f"""
            📋 BOARD MEETING - {state["company_name"]}
            Quarter: {state["current_quarter"]}
            
            📊 DECISION PRESENTATION:
            Title: {decision["title"]}
            Category: {decision["category"]}
            Description: {decision["description"]}
            
            💰 Financial Impact:
            - Estimated Cost: ${decision["estimated_cost"]:,}
            - Expected ROI: {decision["expected_roi"]:.1%}
            - Risk Level: {decision["risk_level"]}
            - Timeline: {decision["timeline"]}
            
            🎯 Impact Areas: {", ".join(decision["impact_areas"])}
            """

            return {
                "discussion_phase": "executive_opinions",
                "current_speaker": "Board Facilitator",
                "meeting_minutes": [presentation],
            }
        except Exception as e:
            return {"error_message": f"Error presenting decision: {str(e)}"}

    def _collect_ceo_opinion(self, state: CompanyState) -> dict[str, Any]:
        """Collect CEO's opinion."""
        try:
            opinion = self.ceo.get_opinion(state)

            minute = f"""
            🔑 CEO OPINION:
            Opinion: {opinion["opinion"]}
            Reasoning: {opinion["reasoning"]}
            Vote: {opinion["vote"].upper()}
            Priority Score: {opinion["priority_score"]}/10
            """

            minutes = state.get("meeting_minutes", [])
            minutes.append(minute)

            return {"ceo_opinion": opinion, "current_speaker": "CEO", "meeting_minutes": minutes}
        except Exception as e:
            return {"error_message": f"Error collecting CEO opinion: {str(e)}"}

    def _collect_cto_opinion(self, state: CompanyState) -> dict[str, Any]:
        """Collect CTO's opinion."""
        try:
            opinion = self.cto.get_opinion(state)

            minute = f"""
            💻 CTO OPINION:
            Opinion: {opinion["opinion"]}
            Reasoning: {opinion["reasoning"]}
            Vote: {opinion["vote"].upper()}
            Priority Score: {opinion["priority_score"]}/10
            """

            minutes = state.get("meeting_minutes", [])
            minutes.append(minute)

            return {"cto_opinion": opinion, "current_speaker": "CTO", "meeting_minutes": minutes}
        except Exception as e:
            return {"error_message": f"Error collecting CTO opinion: {str(e)}"}

    def _collect_cmo_opinion(self, state: CompanyState) -> dict[str, Any]:
        """Collect CMO's opinion."""
        try:
            opinion = self.cmo.get_opinion(state)

            minute = f"""
            📈 CMO OPINION:
            Opinion: {opinion["opinion"]}
            Reasoning: {opinion["reasoning"]}
            Vote: {opinion["vote"].upper()}
            Priority Score: {opinion["priority_score"]}/10
            """

            minutes = state.get("meeting_minutes", [])
            minutes.append(minute)

            return {"cmo_opinion": opinion, "current_speaker": "CMO", "meeting_minutes": minutes}
        except Exception as e:
            return {"error_message": f"Error collecting CMO opinion: {str(e)}"}

    def _collect_cfo_opinion(self, state: CompanyState) -> dict[str, Any]:
        """Collect CFO's opinion."""
        try:
            opinion = self.cfo.get_opinion(state)

            minute = f"""
            💰 CFO OPINION:
            Opinion: {opinion["opinion"]}
            Reasoning: {opinion["reasoning"]}
            Vote: {opinion["vote"].upper()}
            Priority Score: {opinion["priority_score"]}/10
            """

            minutes = state.get("meeting_minutes", [])
            minutes.append(minute)

            return {"cfo_opinion": opinion, "current_speaker": "CFO", "meeting_minutes": minutes}
        except Exception as e:
            return {"error_message": f"Error collecting CFO opinion: {str(e)}"}

    def _facilitate_discussion(self, state: CompanyState) -> dict[str, Any]:
        """Facilitate discussion between executives."""
        try:
            ceo_op = state.get("ceo_opinion")
            cto_op = state.get("cto_opinion")
            cmo_op = state.get("cmo_opinion")
            cfo_op = state.get("cfo_opinion")

            # Summarize the different perspectives
            discussion_summary = f"""
            EXECUTIVE SUMMARY:
            
            CEO ({ceo_op["vote"] if ceo_op else "N/A"}): Strategic perspective focusing on overall business impact
            CTO ({cto_op["vote"] if cto_op else "N/A"}): Technical feasibility and innovation considerations  
            CMO ({cmo_op["vote"] if cmo_op else "N/A"}): Marketing and customer impact analysis
            CFO ({cfo_op["vote"] if cfo_op else "N/A"}): Financial risk and ROI evaluation
            
            Key areas of alignment and disagreement will be considered in the final decision.
            """

            minutes = state.get("meeting_minutes", [])
            minutes.append(discussion_summary)

            return {
                "discussion_phase": "voting",
                "current_speaker": "Board",
                "meeting_minutes": minutes,
            }
        except Exception as e:
            return {"error_message": f"Error facilitating discussion: {str(e)}"}

    def _vote_and_decide(self, state: CompanyState) -> dict[str, Any]:
        """Tabulate votes and make final decision."""
        try:
            votes = []
            priority_scores = []

            for role in ["ceo_opinion", "cto_opinion", "cmo_opinion", "cfo_opinion"]:
                opinion = state.get(role)
                if opinion:
                    votes.append(opinion["vote"])
                    priority_scores.append(opinion["priority_score"])

            approve_count = votes.count("approve")
            reject_count = votes.count("reject")
            abstain_count = votes.count("abstain")

            # Decision logic: majority wins, but consider priority scores for ties
            if approve_count > reject_count:
                decision = "APPROVED"
            elif reject_count > approve_count:
                decision = "REJECTED"
            else:
                # Tie - use average priority score
                avg_priority = sum(priority_scores) / len(priority_scores) if priority_scores else 5
                decision = "APPROVED" if avg_priority >= 6 else "REJECTED"

            vote_summary = f"""
            🗳️ VOTING RESULTS:
            Approve: {approve_count}
            Reject: {reject_count}
            Abstain: {abstain_count}
            
            FINAL DECISION: {decision}
            """

            minutes = state.get("meeting_minutes", [])
            minutes.append(vote_summary)

            return {
                "final_decision": decision,
                "discussion_phase": "decision_made",
                "meeting_minutes": minutes,
            }
        except Exception as e:
            return {"error_message": f"Error in voting: {str(e)}"}

    def _create_implementation_plan(self, state: CompanyState) -> dict[str, Any]:
        """Create implementation plan based on decision."""
        try:
            decision = state.get("final_decision")
            decision_details = state.get("decision_details")

            if decision == "APPROVED" and decision_details:
                # Create implementation plan using facilitator LLM
                prompt = f"""
                The board has APPROVED the following decision:
                Title: {decision_details["title"]}
                Description: {decision_details["description"]}
                Timeline: {decision_details["timeline"]}
                Cost: ${decision_details["estimated_cost"]:,}
                
                Create a practical implementation plan with:
                1. Key milestones and timeline
                2. Resource allocation
                3. Success metrics
                4. Risk mitigation strategies
                5. Responsible parties
                
                Keep it concise but actionable.
                """

                messages = [
                    SystemMessage(
                        content="You are a business strategy consultant creating implementation plans."
                    ),
                    HumanMessage(content=prompt),
                ]

                response = self.facilitator.invoke(messages)
                implementation_plan = str(response.content or "")

                plan_summary = f"""
                📋 IMPLEMENTATION PLAN:
                {implementation_plan}
                """

            else:
                plan_summary = f"""
                📋 DECISION OUTCOME:
                The proposal was {decision}. No implementation plan required.
                
                Next steps: Review feedback and consider alternative approaches.
                """
                implementation_plan = f"Decision {decision} - No implementation required"

            minutes = state.get("meeting_minutes", [])
            minutes.append(plan_summary)

            return {
                "implementation_plan": implementation_plan,
                "discussion_phase": "completed",
                "current_speaker": "Meeting Concluded",
                "meeting_minutes": minutes,
            }
        except Exception as e:
            return {"error_message": f"Error creating implementation plan: {str(e)}"}

    def simulate_board_meeting(
        self,
        company_name: str,
        industry: str,
        company_size: str,
        decision_topic: str,
        decision_details: Decision,
        company_metrics: CompanyMetrics | None = None,
    ) -> CompanyState:
        """Simulate a complete board meeting."""

        # Default metrics if not provided
        if not company_metrics:
            company_metrics = CompanyMetrics(
                revenue=1000000,
                expenses=800000,
                profit=200000,
                cash_flow=150000,
                employee_count=50,
                customer_satisfaction=7.5,
                market_share=0.15,
                tech_debt=4.0,
                brand_value=6.5,
            )

        initial_state = CompanyState(
            company_name=company_name,
            industry=industry,
            company_size=company_size,
            current_quarter="Q1 2024",
            decision_topic=decision_topic,
            decision_details=decision_details,
            metrics=company_metrics,
            ceo_opinion=None,
            cto_opinion=None,
            cmo_opinion=None,
            cfo_opinion=None,
            current_speaker="",
            discussion_phase="presentation",
            meeting_minutes=[],
            final_decision=None,
            decision_rationale=None,
            implementation_plan=None,
            error_message=None,
        )

        result = self.workflow.invoke(initial_state)
        return cast(CompanyState, result)
