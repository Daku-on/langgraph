"""Advanced example demonstrating custom research workflows."""

from dotenv import load_dotenv

from src.ai_research_assistant import ResearchAssistant

# Load environment variables
load_dotenv()


def demonstrate_research_workflow():
    """Demonstrate the complete research workflow with detailed output."""
    assistant = ResearchAssistant()

    research_questions = [
        "What are the environmental impacts of electric vehicle adoption?",
        "How does machine learning improve cybersecurity?",
        "What are the latest developments in quantum computing?",
    ]

    for i, question in enumerate(research_questions, 1):
        print(f"\n{'=' * 80}")
        print(f"🔬 RESEARCH EXAMPLE {i}: {question}")
        print("=" * 80)

        try:
            result = assistant.research(question)

            if result.get("error_message"):
                print(f"❌ Error: {result['error_message']}")
                continue

            print("\n📅 RESEARCH PROCESS COMPLETE")
            print(f"Current Step: {result['current_step']}")

            print("\n📋 RESEARCH PLAN:")
            print("-" * 60)
            print(result["research_plan"])

            print(f"\n📚 INFORMATION COLLECTED ({len(result['collected_info'])} items):")
            print("-" * 60)
            for j, info in enumerate(result["collected_info"][:5], 1):  # Show first 5
                if info.strip():
                    print(f"{j}. {info}")
            if len(result["collected_info"]) > 5:
                print(f"... and {len(result['collected_info']) - 5} more items")

            print("\n🔬 ANALYSIS:")
            print("-" * 60)
            analysis = result["analysis"]
            if analysis and len(analysis) > 500:
                print(analysis[:500] + "...")
            else:
                print(analysis)

            print("\n📊 FINAL REPORT (Summary):")
            print("-" * 60)
            report = result["final_report"]
            if report and len(report) > 800:
                print(report[:800] + "...")
            else:
                print(report)

        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")

        if i < len(research_questions):
            print("\n⏳ Next research starting in a moment...")


def main():
    """Run advanced research examples."""
    print("🧪 Advanced AI Research Assistant Demo")
    print("This demo shows multiple research workflows")
    print("=" * 80)

    demonstrate_research_workflow()

    print("\n" + "=" * 80)
    print("✅ All research examples completed!")
    print("=" * 80)


if __name__ == "__main__":
    main()
