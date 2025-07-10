# Compliance ROI Engine 🔍💰

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Maintenance](https://img.shields.io/badge/maintained%3F-yes-green)

> **Enterprise Compliance Automation**  
> Developed by **Al Bochi**, Lead Cloud Security Compliance at **Saillent**

<div align="center">
  <img src="assets/app-screenshot.png" alt="Compliance ROI Engine Dashboard" width="800">
</div>

## ✨ Features

- **ROI Calculator**  
  Quantify financial impact of compliance programs with risk-adjusted metrics

- **Smart Policy Engine**  
  AI-powered audit response generation with regulatory citations (SOC2, HIPAA, GDPR, PCI DSS)

- **Coverage Analyzer**  
  Visual dashboard showing framework implementation status

- **Executive Reporting**  
  Auto-generated compliance posture reports in PDF/CSV

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key

### Installation
```bash
# Clone repository
git clone https://github.com/AlBochi/compliance-roi-engine.git
cd compliance-roi-engine

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
echo "OPENAI_API_KEY=your_key_here" > .env
Launch Application
bash
streamlit run app.py
Access at: http://localhost:8501

⚙️ Configuration
Policy Database
Edit policy_database.json to add controls:

json
{
  "policies": [
    {
      "framework": "SOC2",
      "control_id": "CC6.1",
      "text": "Multi-factor authentication required for all administrative access"
    },
    {
      "framework": "GDPR",
      "control_id": "Art. 32",
      "text": "Encryption of personal data in transit and at rest"
    }
  ]
}
Environment Variables
Variable	Required	Description
OPENAI_API_KEY	Yes	Get your OpenAI key
ANALYTICS_ENABLED	No	Set to "false" to disable usage tracking
💡 Usage Examples
ROI Calculation
text
Compliance Program Cost: $120,000  
Potential Fines Avoided: $450,000  
Incidents Prevented: 5  
Cost per Incident: $90,000
➡️ ROI: 287.5%

Audit Response Generation
Question:
"What are our requirements for encryption under HIPAA and GDPR?"

Generated Response:

"Per HIPAA 164.312(e)(2) and GDPR Article 32:

All ePHI must be encrypted at rest (AES-256)

Personal data requires TLS 1.2+ for transmission

Encryption keys must be rotated quarterly

Key management procedures must be documented"

📂 Project Structure
text
.
├── app.py                 # Streamlit application
├── utils.py               # AI response generation
├── policy_database.json   # Compliance controls
├── requirements.txt       # Python dependencies
├── .gitignore            # Excluded files
├── LICENSE               # MIT License
└── README.md             # This documentation
🛠️ Troubleshooting
Error	Solution
401 Invalid API Key	Verify key at OpenAI Dashboard
429 Rate Limit	Upgrade plan or wait for quota reset
JSON Decode Error	Validate syntax: python -c "import json; json.load(open('policy_database.json'))"
🌟 Roadmap
Core ROI Calculator

Audit Response Automation

Local LLM Support (Ollama)

Multi-user Authentication

JIRA Integration

🤝 Contributing
Fork the repository

Create feature branch (git checkout -b feature/improvement)

Commit changes (git commit -m 'Add new feature')

Push to branch (git push origin feature/improvement)

Open a Pull Request

📜 License
MIT License
Copyright © 2023 Al Bochi - Saillent
