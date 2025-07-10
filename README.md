# Compliance ROI Engine 🚀

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub Last Commit](https://img.shields.io/github/last-commit/AlBochi/compliance-roi-engine)

> AI-powered toolkit for compliance financial analysis and audit automation

## ✨ Features

- **ROI Dashboard**: Calculate financial impact of compliance programs
- **Smart Policy Database**: Centralized controls (SOC2/HIPAA/GDPR/PCI DSS)
- **Audit Assistant**: Generate standards-compliant responses with citations
- **Coverage Analyzer**: Visualize framework implementation status

## 🚀 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/AlBochi/compliance-roi-engine.git
cd compliance-roi-engine

# 2. Set up environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Configure secrets
echo "OPENAI_API_KEY=your_key_here" > .env

# 4. Launch app
streamlit run app.py
