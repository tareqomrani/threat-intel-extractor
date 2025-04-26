<p align="center">
  <img src="https://img.shields.io/badge/Project-Threat%20Intelligence%20Extractor%20(Lite)-brightgreen?style=for-the-badge&logo=streamlit&logoColor=white" alt="Threat Intelligence Extractor (Lite)"/>
</p>

<p align="center">
  Extract IOCs — IPs, Domains, Hashes — from Threat Reports using Streamlit + Python  
</p>

---
# Threat Intelligence Extractor (Lite)

A lightweight Streamlit app that extracts indicators of compromise (IOCs) using regular expressions.

## Features
- Extracts IP addresses, domains, and hashes (MD5, SHA1, SHA256)
- No external APIs or heavy ML models required
- 100% free deployment on Streamlit Cloud

## Setup Instructions

```bash
pip install -r requirements.txt
streamlit run threat_intel_extractor_ui.py
```

## License
MIT
