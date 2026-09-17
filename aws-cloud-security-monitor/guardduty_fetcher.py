# Example GuardDuty fetcher
# To use this module with real AWS GuardDuty data:
# 1) Install AWS CLI and configure credentials or set AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY env vars.
# 2) Ensure GuardDuty is enabled in the target region.
# 3) Import and call fetch_findings_from_aws() from your application.
import boto3, json

def fetch_findings_from_aws(region_name='us-east-1'):
    client = boto3.client('guardduty', region_name=region_name)
    detectors = client.list_detectors()
    if 'DetectorIds' not in detectors or len(detectors['DetectorIds']) == 0:
        raise Exception('No GuardDuty detector found in this account/region. Please enable GuardDuty.')
    detector_id = detectors['DetectorIds'][0]
    finding_ids_resp = client.list_findings(DetectorId=detector_id, MaxResults=50)
    finding_ids = finding_ids_resp.get('FindingIds', [])
    if not finding_ids:
        return { 'findings': [] }
    findings_resp = client.get_findings(DetectorId=detector_id, FindingIds=finding_ids)
    return findings_resp.get('Findings', [])

def load_mock_findings():
    with open('mock_findings.json') as f:
        return json.load(f)
