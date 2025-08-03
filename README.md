# AI Research Assistant with LangGraph

## 概要

LangGraphを使用してステートフルなマルチステップの研究ワークフローを実装したAI研究アシスタントです。このアプリケーションは、研究質問を受け取り、計画立案から情報収集、分析、レポート生成まで、一連の研究プロセスを自動化します。

## 主な機能

- **研究計画立案**: 質問に基づいた体系的な研究計画の自動生成
- **情報収集**: 研究計画に沿った関連情報の収集（シミュレーション）
- **分析・考察**: 収集した情報の詳細な分析と洞察の抽出
- **レポート生成**: 包括的な研究レポートの自動作成
- **ステートフル処理**: LangGraphによる各ステップの状態管理

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

### 基本的な使用例

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

### 実行例

```bash
# 基本的な例を実行
uv run python examples/basic_research.py
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
├── src/ai_research_assistant/    # メインパッケージ
│   ├── __init__.py
│   ├── state.py                  # ステート定義
│   └── research_assistant.py     # メインロジック
├── tests/                        # テストファイル
├── examples/                     # 使用例
├── .env.example                  # 環境変数テンプレート
└── pyproject.toml               # プロジェクト設定
```

## 必要な環境変数

- `OPENAI_API_KEY`: OpenAI APIキー（必須）

## ライセンス

このプロジェクトはオープンソースです。

---

# AI Research Assistant with LangGraph

## Overview

An AI Research Assistant that implements stateful, multi-step research workflows using LangGraph. This application automates the entire research process from question intake to planning, information collection, analysis, and report generation.

## Key Features

- **Research Planning**: Automatic generation of systematic research plans based on questions
- **Information Collection**: Gathering relevant information according to research plans (simulated)
- **Analysis & Insights**: Detailed analysis of collected information and insight extraction
- **Report Generation**: Automatic creation of comprehensive research reports
- **Stateful Processing**: State management for each step using LangGraph

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

### Basic Usage Example

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

### Running Examples

```bash
# Run the basic example
uv run python examples/basic_research.py
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
├── src/ai_research_assistant/    # Main package
│   ├── __init__.py
│   ├── state.py                  # State definitions
│   └── research_assistant.py     # Main logic
├── tests/                        # Test files
├── examples/                     # Usage examples
├── .env.example                  # Environment variable template
└── pyproject.toml               # Project configuration
```

## Required Environment Variables

- `OPENAI_API_KEY`: OpenAI API key (required)

## License

This project is open source.
