import streamlit as st
import pandas as pd
import json
from orchestrator import run_pipeline, generate_sql

st.title("🧠 Multi-Agent Data Validation Copilot")

uploaded_csv = st.file_uploader("Upload CSV", type=["csv"])
uploaded_schema = st.file_uploader("Upload Schema JSON", type=["json"])

if uploaded_csv and uploaded_schema:
    df = pd.read_csv(uploaded_csv)
    schema = json.load(uploaded_schema)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    if st.button("Run Multi-Agent Validation"):
        with st.spinner("Agents collaborating..."):
            result = run_pipeline(schema, df)

        st.subheader("📋 Planner Output")
        st.write(result["plan"])

        st.subheader("📝 Generated Rules")
        st.json(result["rules"])

        st.subheader("📊 Validation Report")
        st.json(result["report"])

        st.subheader("🧾 AI Explanation")
        st.write(result["explanation"])

    if st.button("Generate SQL Checks"):
        sql = generate_sql(schema)
        st.code(sql)