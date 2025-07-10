# Compliance ROI Engine 🔐

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)

> **Enterprise Compliance Automation**  
> Developed by **Al Bochi**, Lead Cloud Security Compliance at **Saillent**

---

## 🚀 Local Development Setup

### 1. Prerequisites
- Python 3.8+
- OpenAI API key ([Get here](https://platform.openai.com/api-keys))
- Git

### 2. Installation
```bash
# Clone repository
git clone https://github.com/AlBochi/compliance-roi-engine.git
cd compliance-roi-engine

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

### 3. Configuration
# Create environment file
echo "OPENAI_API_KEY=your_key_here" > .env
echo "LOG_LEVEL=INFO" >> .env
chmod 600 .env  # Restrict file permissions

# Initialize policy database
cat > policy_database.json << 'EOL'
{
  "policies": [
    {
      "framework": "SOC2",
      "control_id": "CC6.1",
      "text": "Multi-factor authentication required for all administrative access",
      "category": "Access Control"
    },
    {
      "framework": "GDPR",
      "control_id": "Art. 32",
      "text": "Encryption of personal data in transit and at rest",
      "category": "Data Protection"
    }
  ]
}
EOL

###4. Launch Application

streamlit run app.py

➡️ Access at: http://localhost:8501

⚙️ Environment Variables
- Variable	Required	Default	Description
- OPENAI_API_KEY	Yes	-	Your OpenAI API key
- LOG_LEVEL	No	INFO	Set to DEBUG for troubleshooting
- MAX_RESPONSE_TOKENS	No	1000	Limit response length

💡 Core Usage Examples
ROI Calculator
python
# Input
Compliance Program Cost: $

📜 License
MIT License
Copyright © 2023 Al Bochi - Saillent
