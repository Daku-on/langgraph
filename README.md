# AI Research Assistant & Virtual Company Simulator with LangGraph

## 概要

LangGraphを使用した2つの革新的なAIアプリケーション：

### 🔬 AI研究アシスタント
ステートフルなマルチステップの研究ワークフローを実装。研究質問を受け取り、計画立案から情報収集、分析、レポート生成まで、一連の研究プロセスを自動化します。

### 🏢 バーチャル企業シミュレーター  
AI役員（CEO、CTO、CMO、CFO）による取締役会議をシミュレート。各役員がそれぞれの専門分野から意見を述べ、協議を通じて経営判断を下します。

## 主な機能

### 🔬 研究アシスタント機能
- **研究計画立案**: 質問に基づいた体系的な研究計画の自動生成
- **情報収集**: 研究計画に沿った関連情報の収集（シミュレーション）
- **分析・考察**: 収集した情報の詳細な分析と洞察の抽出
- **レポート生成**: 包括的な研究レポートの自動作成

### 🏢 企業シミュレーター機能
- **AI役員会議**: CEO、CTO、CMO、CFOによる取締役会議のシミュレーション
- **多角的検討**: 各役員の専門分野（戦略、技術、マーケティング、財務）からの意見
- **民主的決定**: 投票システムによる意思決定プロセス
- **実装計画**: 承認された提案の具体的な実行計画の自動生成
- **ステートフル処理**: LangGraphによる会議フローの状態管理

## インストール

```bash
# リポジトリをクローン
git clone https://github.com/Daku-on/langgraph.git
cd langgraph

# 依存関係をインストール
uv sync

# 環境変数を設定
cp .env.example .env
# .envファイルを編集してOpenAI API keyを設定
```

## 使用方法

### 🔬 研究アシスタントの使用例

```python
from src.ai_research_assistant import ResearchAssistant

# 研究アシスタントを初期化
assistant = ResearchAssistant()

# 研究を実行
result = assistant.research("人工知能のヘルスケア分野での最新動向は？")

# 結果を表示
print("研究計画:", result["research_plan"])
print("分析結果:", result["analysis"])
print("最終レポート:", result["final_report"])
```

### 🏢 企業シミュレーターの使用例

```python
from src.ai_research_assistant import VirtualCompanySimulator, Decision, CompanyMetrics

# 企業シミュレーターを初期化
simulator = VirtualCompanySimulator()

# 会社の財務指標を定義
metrics = CompanyMetrics(
    revenue=2500000,
    expenses=2200000,
    profit=300000,
    cash_flow=200000,
    employee_count=25,
    customer_satisfaction=8.2,
    market_share=0.08,
    tech_debt=6.5,
    brand_value=7.1
)

# 検討する提案を定義
decision = Decision(
    title="AI顧客サポートシステムの導入",
    description="AI チャットボットシステムを導入し、顧客サポート業務の70%を自動化",
    category="technical",
    impact_areas=["customer_experience", "operations", "costs"],
    estimated_cost=150000,
    expected_roi=0.25,
    timeline="6ヶ月間での実装",
    risk_level="medium"
)

# 取締役会議をシミュレート
result = simulator.simulate_board_meeting(
    company_name="TechFlow Solutions",
    industry="SaaS Technology",
    company_size="startup",
    decision_topic="AI顧客サポート導入",
    decision_details=decision,
    company_metrics=metrics
)

# 会議結果を表示
print("最終決定:", result["final_decision"])
print("実装計画:", result["implementation_plan"])
```

### 実行例

```bash
# 研究アシスタントの基本例
uv run python examples/basic_research.py

# 研究アシスタントの応用例
uv run python examples/advanced_research.py

# 企業シミュレーターの例
uv run python examples/company_board_meeting.py
```

## 開発

### テスト実行

```bash
uv run pytest tests/ -v
```

### コード品質チェック

```bash
# フォーマットチェック
uv run ruff check .

# 型チェック  
uv run mypy src/

# 全チェックを一括実行
uv run pytest tests/ -v && uv run ruff check . && uv run ruff format --check . && uv run mypy src/
```

## プロジェクト構造

```
├── src/ai_research_assistant/          # メインパッケージ
│   ├── __init__.py                     # パッケージ初期化
│   ├── state.py                        # 研究アシスタント用ステート定義
│   ├── research_assistant.py           # 研究アシスタント実装
│   ├── company_state.py                # 企業シミュレーター用ステート定義
│   ├── company_simulator.py            # 企業シミュレーター実装
│   └── executives.py                   # AI役員クラス（CEO/CTO/CMO/CFO）
├── tests/                              # テストファイル
│   ├── test_research_assistant.py      # 研究アシスタントのテスト
│   └── test_company_simulator.py       # 企業シミュレーターのテスト
├── examples/                           # 使用例
│   ├── basic_research.py               # 基本的な研究例
│   ├── advanced_research.py            # 応用研究例
│   └── company_board_meeting.py        # 企業取締役会議例
├── .env.example                        # 環境変数テンプレート
└── pyproject.toml                     # プロジェクト設定
```

## 必要な環境変数

- `OPENAI_API_KEY`: OpenAI APIキー（必須）

## ライセンス

このプロジェクトはオープンソースです。

---

# AI Research Assistant & Virtual Company Simulator with LangGraph

## Overview

Two innovative AI applications built with LangGraph:

### 🔬 AI Research Assistant
Implements stateful, multi-step research workflows. Automates the entire research process from question intake to planning, information collection, analysis, and report generation.

### 🏢 Virtual Company Simulator
Simulates board meetings with AI executives (CEO, CTO, CMO, CFO). Each executive provides opinions from their domain expertise and collaborates to make business decisions.

## Key Features

### 🔬 Research Assistant Features
- **Research Planning**: Automatic generation of systematic research plans based on questions
- **Information Collection**: Gathering relevant information according to research plans (simulated)
- **Analysis & Insights**: Detailed analysis of collected information and insight extraction
- **Report Generation**: Automatic creation of comprehensive research reports

### 🏢 Company Simulator Features
- **AI Executive Board**: Simulated board meetings with CEO, CTO, CMO, and CFO
- **Multi-perspective Analysis**: Each executive provides opinions from their domain expertise (strategy, technology, marketing, finance)
- **Democratic Decision Making**: Voting system for collaborative decision processes
- **Implementation Planning**: Automatic generation of actionable implementation plans for approved proposals
- **Stateful Processing**: State management for meeting flow using LangGraph

## Installation

```bash
# Clone the repository
git clone https://github.com/Daku-on/langgraph.git
cd langgraph

# Install dependencies
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env file to set your OpenAI API key
```

## Usage

### 🔬 Research Assistant Usage Example

```python
from src.ai_research_assistant import ResearchAssistant

# Initialize the research assistant
assistant = ResearchAssistant()

# Conduct research
result = assistant.research("What are the latest trends in AI for healthcare?")

# Display results
print("Research Plan:", result["research_plan"])
print("Analysis:", result["analysis"])
print("Final Report:", result["final_report"])
```

### 🏢 Company Simulator Usage Example

```python
from src.ai_research_assistant import VirtualCompanySimulator, Decision, CompanyMetrics

# Initialize the company simulator
simulator = VirtualCompanySimulator()

# Define company metrics
metrics = CompanyMetrics(
    revenue=2500000,
    expenses=2200000,
    profit=300000,
    cash_flow=200000,
    employee_count=25,
    customer_satisfaction=8.2,
    market_share=0.08,
    tech_debt=6.5,
    brand_value=7.1
)

# Define the decision to be considered
decision = Decision(
    title="Implement AI-Powered Customer Support System",
    description="Deploy AI chatbot system to handle 70% of customer support inquiries",
    category="technical",
    impact_areas=["customer_experience", "operations", "costs"],
    estimated_cost=150000,
    expected_roi=0.25,
    timeline="6 months implementation",
    risk_level="medium"
)

# Simulate board meeting
result = simulator.simulate_board_meeting(
    company_name="TechFlow Solutions",
    industry="SaaS Technology",
    company_size="startup",
    decision_topic="AI Customer Support Implementation",
    decision_details=decision,
    company_metrics=metrics
)

# Display meeting results
print("Final Decision:", result["final_decision"])
print("Implementation Plan:", result["implementation_plan"])
```

### Running Examples

```bash
# Research Assistant Examples
uv run python examples/basic_research.py
uv run python examples/advanced_research.py

# Company Simulator Example
uv run python examples/company_board_meeting.py
```

## Development

### Running Tests

```bash
uv run pytest tests/ -v
```

### Code Quality Checks

```bash
# Format checking
uv run ruff check .

# Type checking
uv run mypy src/

# Run all checks together
uv run pytest tests/ -v && uv run ruff check . && uv run ruff format --check . && uv run mypy src/
```

## Project Structure

```
├── src/ai_research_assistant/          # Main package
│   ├── __init__.py                     # Package initialization
│   ├── state.py                        # Research assistant state definitions
│   ├── research_assistant.py           # Research assistant implementation
│   ├── company_state.py                # Company simulator state definitions
│   ├── company_simulator.py            # Company simulator implementation
│   └── executives.py                   # AI executive classes (CEO/CTO/CMO/CFO)
├── tests/                              # Test files
│   ├── test_research_assistant.py      # Research assistant tests
│   └── test_company_simulator.py       # Company simulator tests
├── examples/                           # Usage examples
│   ├── basic_research.py               # Basic research example
│   ├── advanced_research.py            # Advanced research example
│   └── company_board_meeting.py        # Board meeting example
├── .env.example                        # Environment variable template
└── pyproject.toml                     # Project configuration
```

## Required Environment Variables

- `OPENAI_API_KEY`: OpenAI API key (required)

## License

This project is open source.
