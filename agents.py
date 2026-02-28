import json
import requests
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def call_llm(prompt, temperature=0):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "temperature": temperature
        }
    )
    return response.json()["response"]


def extract_json(text):
    try:
        json_match = re.search(r"\[.*\]", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except:
        pass
    return []


# 🧠 1. Planner Agent
def planner_agent(schema):
    prompt = f"""
You are a planning agent.

Given this schema:
{json.dumps(schema, indent=2)}

Decide the steps required for validation.

Return bullet steps only.
"""
    return call_llm(prompt)


# 🧠 2. Rule Generator Agent
def rule_generator_agent(schema):
    prompt = f"""
You are a senior data quality engineer.

STRICT:
Return ONLY JSON array.
No explanation.

Schema:
{json.dumps(schema, indent=2)}

Format:
[
  {{"column": "col", "rule": "not_null"}},
  {{"column": "age", "rule": "between", "min": 18, "max": 60}},
  {{"column": "email", "rule": "regex", "pattern": "email"}},
  {{"column": "salary", "rule": "greater_than", "min": 1000}}
]
"""
    output = call_llm(prompt)
    return extract_json(output)


# 🧠 3. Explainer Agent
def explainer_agent(schema, report):
    prompt = f"""
You are a senior data engineer.

Explain validation failures clearly and suggest fixes.

Schema:
{json.dumps(schema, indent=2)}

Report:
{json.dumps(report, indent=2)}
"""
    return call_llm(prompt, temperature=0.3)


# 🧠 4. SQL Agent
def sql_agent(schema):
    prompt = f"""
Generate SQL validation queries for this schema.

Schema:
{json.dumps(schema, indent=2)}

Return SQL only.
"""
    return call_llm(prompt)