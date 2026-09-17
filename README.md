AWS Cloud Security Monitoring - Demo Project
===========================================
Overview
--------
This project demonstrates a small AWS Cloud Security Monitoring system that collects GuardDuty findings
(or mock findings), exposes them via a Flask backend and displays them in a simple real-time dashboard.
The project is intended for demo and learning purposes. Replace mock data with real AWS GuardDuty queries
by providing AWS credentials and enabling GuardDuty in your account.

What's included
----------------
- app.py                : Flask web app that serves a dashboard and an API endpoint (/findings)
- guardduty_fetcher.py  : Example GuardDuty fetcher using boto3 (commented instructions)
- static/index.html     : Simple dashboard that polls /findings and shows alerts
- mock_findings.json    : Example GuardDuty findings (mock data)
- requirements.txt      : Python dependencies
- run.sh                : Small script to run the Flask app locally
- LICENSE               : MIT license
- README.md             : This file

Quick start (local, with mock data)
----------------------------------
1. Create a Python 3.8+ virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows (PowerShell)

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app:
   python app.py

4. Open http://localhost:5000 in your browser. The dashboard will poll /findings and display mock alerts.

To use real AWS GuardDuty (optional)
-----------------------------------
- Configure AWS credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, region) using AWS CLI or env vars.
- Enable GuardDuty in the AWS Console for your account/region.
- Uncomment the boto3 code in guardduty_fetcher.py and call fetch_findings_from_aws() from app.py.
- Make sure boto3 is installed (included in requirements.txt).

Notes
-----
This is a demo starter project. Do not run automation that affects production resources without proper authorization.
