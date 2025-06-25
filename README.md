# 🧠 AI Transaction Insights


A lightweight fintech analytics tool that ingests CSV bank statements, uses AI to classify transactions, and visualizes financial trends.

🚀 **Live App**: https://ai-transaction-insights.streamlit.app

---

## ✨ Features

- 📂 Upload and analyze CSV bank statements
- 🤖 AI-powered transaction classification using GPT
- 📊 Visual dashboards: category spend, trends over time
- ⚠️ Anomaly detection: flag unusual transactions
- 🧾 Export AI-labeled results as CSV
- 🔐 Secrets management via Streamlit Cloud

---
## Instructions
📌 Column Details:
- Date: A valid date string (e.g., 2024-06-01). Format: YYYY-MM-DD.
- Description: Transaction label or merchant name.
- Amount: Use negative numbers for expenses and positive for income.
- Currency: ISO 4217 currency code (e.g., EUR, USD).
- Category (optional): You can pre-fill this, or the app will try to classify it automatically.

💡 Tips:
	•	Decimal separator: Use . (dot), not comma.
	•	Header row must be included.
	•	File must be in .csv format, UTF-8 encoded.
 

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** (web app interface)
- **Pandas** (data handling)
- **Plotly** (interactive visualizations)
- **OpenAI API** (semantic classification via GPT)
- **Deployed** on Streamlit Cloud

---

## 🧱 Project Structure
