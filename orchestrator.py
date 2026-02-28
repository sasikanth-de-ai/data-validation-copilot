from agents import planner_agent, rule_generator_agent, explainer_agent, sql_agent
from validator import validate_data


def run_pipeline(schema, df):
    plan = planner_agent(schema)
    rules = rule_generator_agent(schema)
    report = validate_data(df, rules)
    explanation = explainer_agent(schema, report)

    return {
        "plan": plan,
        "rules": rules,
        "report": report,
        "explanation": explanation
    }


def generate_sql(schema):
    return sql_agent(schema)