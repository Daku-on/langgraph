"""Main ResearchAssistant class implementing the LangGraph workflow."""

import os
from typing import Any, cast

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from pydantic import SecretStr

from .state import ResearchState


class ResearchAssistant:
    """AI Research Assistant using LangGraph for multi-step research workflow."""

    def __init__(self, openai_api_key: str | None = None):
        """Initialize the research assistant.

        Args:
            openai_api_key: OpenAI API key. If not provided, will use OPENAI_API_KEY env var.
        """
        self.api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required")

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=SecretStr(self.api_key) if self.api_key else None,
            temperature=0.1,
        )

        self.workflow = self._build_workflow()

    def _build_workflow(self) -> Any:
        """Build the LangGraph workflow for research."""
        workflow = StateGraph(ResearchState)

        # Add nodes
        workflow.add_node("plan_research", self._plan_research)
        workflow.add_node("collect_info", self._collect_info)
        workflow.add_node("analyze_info", self._analyze_info)
        workflow.add_node("generate_report", self._generate_report)

        # Define edges
        workflow.set_entry_point("plan_research")
        workflow.add_edge("plan_research", "collect_info")
        workflow.add_edge("collect_info", "analyze_info")
        workflow.add_edge("analyze_info", "generate_report")
        workflow.add_edge("generate_report", END)

        return workflow.compile()

    def _plan_research(self, state: ResearchState) -> dict[str, Any]:
        """Plan the research approach based on the question."""
        try:
            messages = [
                SystemMessage(
                    content="""You are a research planning expert. Given a research question,
                create a clear, structured research plan. The plan should include:
                1. Key areas to investigate
                2. Types of information to look for
                3. Potential sources or approaches
                4. Expected outcomes

                Keep the plan concise but comprehensive."""
                ),
                HumanMessage(content=f"Research question: {state['question']}"),
            ]

            response = self.llm.invoke(messages)

            return {"research_plan": response.content or "", "current_step": "planning_complete"}
        except Exception as e:
            return {
                "error_message": f"Error in research planning: {str(e)}",
                "current_step": "error",
            }

    def _collect_info(self, state: ResearchState) -> dict[str, Any]:
        """Collect information based on the research plan."""
        try:
            messages = [
                SystemMessage(
                    content="""You are an information collection expert. Based on the research plan,
                simulate collecting relevant information. Since this is a demo, provide realistic but simulated
                information that would be found through research. Include:
                1. Key facts and data points
                2. Different perspectives on the topic
                3. Recent developments or trends
                4. Expert opinions or studies

                Format as a list of information points."""
                ),
                HumanMessage(
                    content=f"""
                Research Question: {state["question"]}
                Research Plan: {state["research_plan"]}

                Please collect relevant information based on this plan.
                """
                ),
            ]

            response = self.llm.invoke(messages)

            # Simulate multiple information sources
            content = str(response.content or "")
            info_points = content.split("\n")
            info_points = [point.strip() for point in info_points if point.strip()]

            return {"collected_info": info_points, "current_step": "collection_complete"}
        except Exception as e:
            return {
                "error_message": f"Error in information collection: {str(e)}",
                "current_step": "error",
            }

    def _analyze_info(self, state: ResearchState) -> dict[str, Any]:
        """Analyze the collected information."""
        try:
            info_text = "\n".join(state["collected_info"])

            messages = [
                SystemMessage(
                    content="""You are a research analyst. Analyze the collected information and provide:
                1. Key insights and patterns
                2. Strengths and limitations of the information
                3. Connections between different pieces of information
                4. Implications and conclusions
                5. Areas where more research might be needed

                Be objective and analytical in your assessment."""
                ),
                HumanMessage(
                    content=f"""
                Research Question: {state["question"]}
                Collected Information:
                {info_text}

                Please analyze this information thoroughly.
                """
                ),
            ]

            response = self.llm.invoke(messages)

            return {"analysis": response.content or "", "current_step": "analysis_complete"}
        except Exception as e:
            return {"error_message": f"Error in analysis: {str(e)}", "current_step": "error"}

    def _generate_report(self, state: ResearchState) -> dict[str, Any]:
        """Generate the final research report."""
        try:
            info_text = "\n".join(state["collected_info"])

            messages = [
                SystemMessage(
                    content="""You are a research report writer. Create a comprehensive final report that includes:
                1. Executive Summary
                2. Research Question and Methodology
                3. Key Findings
                4. Analysis and Insights
                5. Conclusions
                6. Recommendations for further research

                Make the report well-structured, professional, and actionable."""
                ),
                HumanMessage(
                    content=f"""
                Research Question: {state["question"]}
                Research Plan: {state["research_plan"]}
                Collected Information: {info_text}
                Analysis: {state["analysis"]}

                Please generate a comprehensive final report.
                """
                ),
            ]

            response = self.llm.invoke(messages)

            return {"final_report": response.content or "", "current_step": "complete"}
        except Exception as e:
            return {
                "error_message": f"Error in report generation: {str(e)}",
                "current_step": "error",
            }

    def research(self, question: str) -> ResearchState:
        """Conduct research on the given question.

        Args:
            question: The research question to investigate.

        Returns:
            Final state containing the research results.
        """
        initial_state = ResearchState(
            question=question,
            research_plan=None,
            collected_info=[],
            analysis=None,
            final_report=None,
            current_step="started",
            error_message=None,
        )

        result = self.workflow.invoke(initial_state)
        return cast(ResearchState, result)
