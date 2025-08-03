"""Tests for the Virtual Company Simulator."""

from unittest.mock import patch

import pytest

from src.ai_research_assistant import (
    VirtualCompanySimulator,
    CompanyMetrics,
    Decision,
    CEOExecutive,
    CTOExecutive,
    CMOExecutive,
    CFOExecutive,
)


class TestVirtualCompanySimulator:
    """Test cases for VirtualCompanySimulator."""

    def test_init_with_api_key(self):
        """Test initialization with API key."""
        simulator = VirtualCompanySimulator(openai_api_key="test-key")
        assert simulator.api_key == "test-key"
        assert isinstance(simulator.ceo, CEOExecutive)
        assert isinstance(simulator.cto, CTOExecutive)
        assert isinstance(simulator.cmo, CMOExecutive)
        assert isinstance(simulator.cfo, CFOExecutive)

    def test_init_without_api_key_raises_error(self):
        """Test that initialization without API key raises ValueError."""
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="OpenAI API key is required"):
                VirtualCompanySimulator()

    @patch.dict("os.environ", {"OPENAI_API_KEY": "env-test-key"})
    def test_init_with_env_var(self):
        """Test initialization with environment variable."""
        simulator = VirtualCompanySimulator()
        assert simulator.api_key == "env-test-key"

    @patch("src.ai_research_assistant.company_simulator.ChatOpenAI")
    def test_workflow_creation(self, mock_chat_openai):
        """Test that workflow is properly created."""
        simulator = VirtualCompanySimulator(openai_api_key="test-key")
        assert simulator.workflow is not None

    def test_company_metrics_structure(self):
        """Test CompanyMetrics structure."""
        metrics = CompanyMetrics(
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
        assert metrics["revenue"] == 1000000
        assert metrics["profit"] == 200000
        assert metrics["employee_count"] == 50

    def test_decision_structure(self):
        """Test Decision structure."""
        decision = Decision(
            title="Test Decision",
            description="A test decision for the board",
            category="technical",
            impact_areas=["technology", "costs"],
            estimated_cost=100000,
            expected_roi=0.20,
            timeline="3 months",
            risk_level="medium",
        )
        assert decision["title"] == "Test Decision"
        assert decision["estimated_cost"] == 100000
        assert decision["expected_roi"] == 0.20
        assert "technology" in decision["impact_areas"]


class TestExecutives:
    """Test cases for AI executives."""

    @patch("src.ai_research_assistant.executives.ChatOpenAI")
    def test_executives_initialization(self, mock_chat_openai):
        """Test that all executives can be initialized."""
        ceo = CEOExecutive(openai_api_key="test-key")
        cto = CTOExecutive(openai_api_key="test-key")
        cmo = CMOExecutive(openai_api_key="test-key")
        cfo = CFOExecutive(openai_api_key="test-key")

        assert ceo.llm is not None
        assert cto.llm is not None
        assert cmo.llm is not None
        assert cfo.llm is not None
