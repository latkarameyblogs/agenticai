from app.mcp.tool_handler import execute_claims_triage

result = execute_claims_triage(
    {
        "claim_id": "CLM-100245",
        "estimated_loss": 18000,
        "injury_reported": True,
        "police_report_uploaded": False,
        "fraud_score": 0.2,
    }
)

print(result)