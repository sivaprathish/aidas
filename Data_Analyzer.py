import streamlit as st
from layout import render_shared_layout, render_footer
import tempfile
import os
import pandas as pd
from data_analysis import analyze_dataset
from ai import generate_ai_insights

# Shared layout (adds navbar + CSS)
render_shared_layout("ClariData Analyzer")

st.markdown("<div style='margin-top:100px'></div>", unsafe_allow_html=True)
st.title("📊 Data Analyzer")

uploaded_file = st.file_uploader("📂 Upload your dataset", type=["csv", "xlsx", "xls", "json"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.success(f"✅ File `{uploaded_file.name}` uploaded successfully!")

    st.info("Analyzing dataset... please wait ⏳")
    metadata = analyze_dataset(tmp_path)

    st.subheader("🧩 Columns & Data Types")
    st.dataframe(pd.DataFrame(list(metadata["data_types"].items()), columns=["Column", "Type"]))

    st.subheader("🚫 Missing Values")
    st.bar_chart(pd.DataFrame(list(metadata["missing_values"].items()), columns=["Column", "Missing"]).set_index("Column"))

    st.subheader("📊 Summary Statistics")
    st.dataframe(pd.DataFrame(metadata["summary_statistics"]).T.astype(str))

    st.subheader("📉 Correlations")
    st.dataframe(pd.DataFrame(metadata["correlations"]).astype(str))

    st.subheader("🤖 AI Insights")
    with st.spinner("Generating insights..."):
        ai_output = generate_ai_insights(metadata)

    if "error" in ai_output:
        st.error("⚠️ AI response parsing failed.")
        st.text(ai_output.get("raw_text", ""))
    else:
        st.success("✅ AI Insights generated!")
        st.json(ai_output)
else:
    st.info("👆 Upload a file to start analysis.")

# Footer
render_footer()
