"""Example: Virtual Company Board Meeting Simulation."""

from dotenv import load_dotenv

from src.ai_research_assistant import VirtualCompanySimulator, Decision, CompanyMetrics

# Load environment variables
load_dotenv()


def simulate_tech_startup_meeting():
    """Simulate a board meeting for a tech startup."""
    print("🏢 VIRTUAL COMPANY SIMULATOR")
    print("=" * 80)

    # Initialize the simulator
    simulator = VirtualCompanySimulator()

    # Define company metrics
    metrics = CompanyMetrics(
        revenue=2500000,  # $2.5M
        expenses=2200000,  # $2.2M
        profit=300000,  # $300K profit
        cash_flow=200000,  # $200K cash flow
        employee_count=25,
        customer_satisfaction=8.2,
        market_share=0.08,  # 8% market share
        tech_debt=6.5,  # High tech debt
        brand_value=7.1,
    )

    # Define the decision to be discussed
    decision = Decision(
        title="Implement AI-Powered Customer Support System",
        description="Deploy an AI chatbot system to handle 70% of customer support inquiries, reducing response time and operational costs while improving customer satisfaction.",
        category="technical",
        impact_areas=["customer_experience", "operations", "costs", "technology"],
        estimated_cost=150000,  # $150K
        expected_roi=0.25,  # 25% ROI expected
        timeline="6 months implementation",
        risk_level="medium",
    )

    print(f"🎯 Meeting Topic: {decision['title']}")
    print(f"💰 Investment: ${decision['estimated_cost']:,}")
    print(f"📈 Expected ROI: {decision['expected_roi']:.1%}")
    print("=" * 80)

    # Run the board meeting simulation
    result = simulator.simulate_board_meeting(
        company_name="TechFlow Solutions",
        industry="SaaS Technology",
        company_size="startup",
        decision_topic="AI Customer Support Implementation",
        decision_details=decision,
        company_metrics=metrics,
    )

    # Display results
    if result.get("error_message"):
        print(f"❌ Error: {result['error_message']}")
        return

    print("\n📝 MEETING MINUTES:")
    print("=" * 80)
    for minute in result["meeting_minutes"]:
        print(minute)
        print("-" * 60)

    print(f"\n🎯 FINAL DECISION: {result['final_decision']}")
    print("=" * 80)

    if result.get("implementation_plan"):
        print("\n📋 IMPLEMENTATION PLAN:")
        print(result["implementation_plan"])


def simulate_enterprise_meeting():
    """Simulate a board meeting for an enterprise company."""
    print("\n\n🏢 ENTERPRISE COMPANY MEETING")
    print("=" * 80)

    simulator = VirtualCompanySimulator()

    # Enterprise company metrics
    metrics = CompanyMetrics(
        revenue=50000000,  # $50M
        expenses=42000000,  # $42M
        profit=8000000,  # $8M profit
        cash_flow=6000000,  # $6M cash flow
        employee_count=200,
        customer_satisfaction=7.8,
        market_share=0.35,  # 35% market share
        tech_debt=3.2,  # Lower tech debt
        brand_value=8.5,
    )

    # Strategic decision
    decision = Decision(
        title="Acquire Competitor StartupX for Market Expansion",
        description="Strategic acquisition of StartupX to expand into the European market, gain access to their innovative technology, and increase market share by an estimated 8%.",
        category="strategic",
        impact_areas=["market_expansion", "technology", "competition", "growth"],
        estimated_cost=12000000,  # $12M acquisition
        expected_roi=0.18,  # 18% ROI
        timeline="12 months to complete",
        risk_level="high",
    )

    print(f"🎯 Meeting Topic: {decision['title']}")
    print(f"💰 Investment: ${decision['estimated_cost']:,}")
    print(f"📈 Expected ROI: {decision['expected_roi']:.1%}")
    print("=" * 80)

    result = simulator.simulate_board_meeting(
        company_name="GlobalTech Enterprises",
        industry="Enterprise Software",
        company_size="enterprise",
        decision_topic="Strategic Acquisition",
        decision_details=decision,
        company_metrics=metrics,
    )

    if result.get("error_message"):
        print(f"❌ Error: {result['error_message']}")
        return

    print("\n📝 MEETING MINUTES:")
    print("=" * 80)
    for minute in result["meeting_minutes"]:
        print(minute)
        print("-" * 60)

    print(f"\n🎯 FINAL DECISION: {result['final_decision']}")
    print("=" * 80)


def main():
    """Run board meeting simulations."""
    try:
        simulate_tech_startup_meeting()
        simulate_enterprise_meeting()

        print("\n" + "=" * 80)
        print("✅ Board meeting simulations completed!")
        print("Each executive provided their perspective based on their role.")
        print("Decisions were made through collaborative AI discussion.")
        print("=" * 80)

    except Exception as e:
        print(f"❌ Error running simulations: {str(e)}")
        print("Make sure your OpenAI API key is set in the .env file")


if __name__ == "__main__":
    main()
