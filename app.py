import streamlit as st
import pandas as pd
import plotly.express as px
from classify import classify_transaction

st.set_page_config(page_title="AI Transaction Insights", layout="wide")
st.title("💳 AI Transaction Insights")
st.write("Upload a CSV file of your transactions to begin analysis and get AI-powered insights.")

uploaded_file = st.file_uploader("📂 Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])

    with st.spinner("🔍 Classifying transactions..."):
        df["AI Category"] = df["Description"].apply(classify_transaction)

    # Extract merchant from description (basic logic)
    df["Merchant"] = df["Description"].str.extract(r'(?:- )?(?P<Merchant>\b\w+\b)', expand=True)

    # Show full table
    st.subheader("🧾 Labeled Transactions")
    st.dataframe(df)

    # Spending by Category
    st.subheader("💰 Spending by AI Category")
    category_summary = df.groupby("AI Category")["Amount"].sum().reset_index()
    fig_cat = px.bar(category_summary, x="AI Category", y="Amount", title="Total Spending by Category")
    st.plotly_chart(fig_cat, use_container_width=True)

    # Spending Over Time
    st.subheader("📈 Spending Over Time")
    daily = df.groupby("Date")["Amount"].sum().reset_index()
    fig_time = px.line(daily, x="Date", y="Amount", title="Spending Over Time")
    st.plotly_chart(fig_time, use_container_width=True)

    # Top Merchants
    st.subheader("🏪 Top Merchants by Spend")
    top_merchants = df.groupby("Merchant")["Amount"].sum().sort_values(ascending=False).reset_index()
    st.dataframe(top_merchants)

    # Anomalies (3x category median)
    st.subheader("⚠️ Potential Anomalies")
    anomalies = []
    for cat in df["AI Category"].unique():
        subset = df[df["AI Category"] == cat]
        median = subset["Amount"].median()
        threshold = 3 * median
        flagged = subset[subset["Amount"] > threshold]
        anomalies.append(flagged)
    anomalies_df = pd.concat(anomalies) if anomalies else pd.DataFrame()
    st.dataframe(anomalies_df)

    # Natural Language Summary
    st.subheader("🧠 Smart Summary")
    summary = []
    for cat in df["AI Category"].unique():
        total = df[df["AI Category"] == cat]["Amount"].sum()
        summary.append(f"You spent **${total:.2f}** on **{cat}**.")
    st.markdown(" ".join(summary))

    # Export Button
    st.subheader("⬇️ Export Labeled Data")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download as CSV", csv, "labeled_transactions.csv", "text/csv")