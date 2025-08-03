"""Tests for the ResearchAssistant class."""

from unittest.mock import patch

import pytest

from src.ai_research_assistant import ResearchAssistant, ResearchState


class TestResearchAssistant:
    """Test cases for ResearchAssistant."""

    def test_init_with_api_key(self):
        """Test initialization with API key."""
        assistant = ResearchAssistant(openai_api_key="test-key")
        assert assistant.api_key == "test-key"

    def test_init_without_api_key_raises_error(self):
        """Test that initialization without API key raises ValueError."""
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="OpenAI API key is required"):
                ResearchAssistant()

    @patch.dict("os.environ", {"OPENAI_API_KEY": "env-test-key"})
    def test_init_with_env_var(self):
        """Test initialization with environment variable."""
        assistant = ResearchAssistant()
        assert assistant.api_key == "env-test-key"

    @patch("src.ai_research_assistant.research_assistant.ChatOpenAI")
    def test_workflow_creation(self, mock_chat_openai):
        """Test that workflow is properly created."""
        assistant = ResearchAssistant(openai_api_key="test-key")
        assert assistant.workflow is not None

    def test_research_state_structure(self):
        """Test that ResearchState has required fields."""
        state = ResearchState(
            question="test question",
            research_plan=None,
            collected_info=[],
            analysis=None,
            final_report=None,
            current_step="started",
            error_message=None,
        )
        assert state["question"] == "test question"
        assert state["collected_info"] == []
        assert state["current_step"] == "started"
