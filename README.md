# Multi-Agent Data Validation Copilot (Local LLM Powered)

## Overview

Multi-Agent Data Validation Copilot is an Agentic AI system that:

- Interprets table schema definitions
- Generates structured validation rules
- Executes deterministic data quality checks
- Explains validation failures in natural language
- Generates SQL validation queries for production use

The entire system runs locally using an open-source LLM via Ollama.  
No external APIs, no cloud dependency, and no internet connection required.

---

## Problem Statement

In enterprise data engineering workflows:

- Validation rules are manually written
- Schema interpretation is repetitive
- SQL data quality checks require effort
- Business-readable explanations are missing

This project demonstrates how Agentic AI can automate schema-driven validation while maintaining deterministic enforcement for reliability.

---

## Architecture

User  
→ Streamlit UI  
→ Orchestrator  
→ Planner Agent  
→ Rule Generator Agent  
→ Deterministic Validation Engine (Pandas)  
→ Explainer Agent  
→ SQL Generator Agent  

The system separates reasoning (LLM) from execution (deterministic validation engine).

---

## Agent Components

### Planner Agent
Analyzes schema and determines validation strategy.

### Rule Generator Agent
Converts schema metadata into structured validation rules.

Supported rule types:
- not_null
- between
- greater_than
- less_than
- regex (email validation)

### Deterministic Validator
Executes validation rules using Pandas.
Ensures reliable, non-probabilistic enforcement.

### Explainer Agent
Converts validation results into human-readable summaries.

### SQL Generator Agent
Generates SQL validation queries that can be integrated into:
- Databricks
- Delta Lake
- CI/CD data pipelines

---

## Technology Stack

- Python 3.10+
- Streamlit
- Pandas
- Ollama (Local LLM Runtime)
- Mistral 7B model
- Multi-Agent orchestration pattern

---

## Why Local LLM?

This system uses Ollama with the Mistral model running entirely on localhost.

Benefits:

- Zero API cost
- No external service dependency
- No data privacy concerns
- Fully offline operation
- Suitable for secure environments

Tested on:
- 16GB RAM
- Ryzen 7 CPU
- No GPU required

---

## Installation Guide

### 1. Install Python

Ensure Python 3.10 or higher is installed.

### 2. Install Ollama

Download from:
https://ollama.com

Verify installation:

```bash
ollama --version
```

### 3. Pull Mistral Model

```bash
ollama pull mistral
```

### 4. Clone Repository

```bash
git clone <repository-url>
cd data-validation-copilot
```

### 5. Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 6. Install Dependencies

```bash
pip install -r requirements.txt
```

### 7. Start Ollama Server

```bash
ollama serve
```

### 8. Run Application

```bash
streamlit run app.py
```

Open in browser:

http://localhost:8501

---

## Example Workflow

1. Upload dataset (CSV)
2. Upload schema (JSON)
3. Run Multi-Agent Validation
4. View:
   - Planner output
   - Generated rules
   - Validation report
   - AI explanation
5. Generate SQL validation queries

---

## Test Scenarios

Example datasets included:

- valid_data.csv – All valid records
- null_errors.csv – Missing values
- range_errors.csv – Out-of-range values
- mixed_errors.csv – Multiple validation failures

---

## Key Design Decisions

- LLM used only for reasoning and interpretation
- Deterministic engine enforces validation logic
- Clear modular separation between agents
- Extensible architecture for enterprise integration

LLMs assist with schema interpretation.  
Deterministic logic guarantees correctness.

---

## Enterprise Extension Possibilities

This framework can be extended to:

- Bronze to Silver validation pipelines
- Databricks Delta validation layer
- Metadata-driven validation systems
- CI/CD data quality enforcement
- Unity Catalog schema checks
- Integration with Great Expectations

---

## Limitations

- Local model reasoning limited compared to large cloud-hosted models
- Requires structured prompting
- Prototype architecture (monitoring and logging not included)

---

## Future Enhancements

- Retry mechanism for rule generation
- Confidence scoring
- Logging and monitoring
- REST API deployment
- Parallel agent execution
- Databricks integration
- Automated metadata ingestion

---

## What This Project Demonstrates

- Agentic AI architecture
- Local LLM deployment
- Hybrid AI + deterministic systems
- Secure and cost-efficient AI workflows
- Enterprise-style system design thinking

---

## Author

Built as a GenAI portfolio project to demonstrate multi-agent orchestration and production-style AI system design.
