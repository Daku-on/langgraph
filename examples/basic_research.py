"""Basic example of using the AI Research Assistant."""

from dotenv import load_dotenv

from src.ai_research_assistant import ResearchAssistant

# Load environment variables
load_dotenv()


def main():
    """Run a basic research example."""
    # Initialize the research assistant
    assistant = ResearchAssistant()

    # Define a research question
    question = "What are the latest trends in artificial intelligence for healthcare?"

    print(f"🔍 Starting research on: {question}")
    print("=" * 60)

    # Conduct research
    result = assistant.research(question)

    # Display results
    if result.get("error_message"):
        print(f"❌ Error: {result['error_message']}")
        return

    print("\n📋 RESEARCH PLAN:")
    print("-" * 40)
    print(result["research_plan"])

    print("\n📚 COLLECTED INFORMATION:")
    print("-" * 40)
    for i, info in enumerate(result["collected_info"], 1):
        if info.strip():
            print(f"{i}. {info}")

    print("\n🔬 ANALYSIS:")
    print("-" * 40)
    print(result["analysis"])

    print("\n📊 FINAL REPORT:")
    print("-" * 40)
    print(result["final_report"])


if __name__ == "__main__":
    main()
