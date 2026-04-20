CLAIMS_TRIAGE_TOOL_CONTRACT = {
    "name": "claims_triage",
    "description": (
        "Determine claim severity, priority, recommended queue, "
        "required documents, and explanation for an already validated "
        "auto insurance claim."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "claim_id": {
                "type": "string",
                "description": "Unique insurance claim identifier"
            },
            "estimated_loss": {
                "type": "number",
                "description": "Estimated claim loss amount"
            },
            "injury_reported": {
                "type": "boolean",
                "description": "Whether bodily injury is reported"
            },
            "police_report_uploaded": {
                "type": "boolean",
                "description": "Whether a police report is available"
            },
            "fraud_score": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
                "description": "Fraud score calculated by upstream fraud service"
            }
        },
        "required": [
            "claim_id",
            "estimated_loss",
            "injury_reported",
            "police_report_uploaded",
            "fraud_score"
        ]
    },
    "output_schema": {
        "type": "object",
        "properties": {
            "severity": {
                "type": "string"
            },
            "priority": {
                "type": "string"
            },
            "recommended_queue": {
                "type": "string"
            },
            "required_documents": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "reason": {
                "type": "string"
            }
        }
    }
}