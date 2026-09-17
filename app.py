from flask import Flask, render_template, jsonify, send_from_directory
import json, os
from guardduty_fetcher import fetch_findings_from_aws, load_mock_findings

app = Flask(__name__, static_folder='static', template_folder='static')

USE_AWS = False  # Set True to enable AWS GuardDuty fetching (requires AWS credentials & GuardDuty enabled)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/findings')
def findings():
    if USE_AWS:
        try:
            findings = fetch_findings_from_aws()
        except Exception as e:
            findings = { 'error': str(e) }
    else:
        findings = load_mock_findings()
    return jsonify(findings)

if __name__ == '__main__':
    # Run in debug mode for local testing
    app.run(host='0.0.0.0', port=5000, debug=True)
