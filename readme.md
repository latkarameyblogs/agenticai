# Claims Triage Agent

An industry-style Auto Insurance Claims Triage Agent built with CrewAI, Streamlit, and MCP.

This project is intentionally limited to the Claims Triage stage in the insurance claims lifecycle.

```text
Policy Validation -> Fraud Detection -> Claims Triage -> Claim Assignment
```

The application assumes that:

* Policy validation has already been completed
* Fraud score has already been calculated
* FNOL, OCR, image analysis, and claim settlement are handled elsewhere

The agent determines:

* Claim severity
* Claim priority
* Recommended queue
* Required documents
* Business explanation

---

## Features

* Streamlit UI for human users
* CrewAI-based Claims Triage Agent
* MCP tool exposure so other agents can reuse triage capability
* Structured claim input and triage output using Pydantic
* Simple rule-based services plus LLM explanation
* Ready for deployment on Hugging Face Spaces

---

## Architecture

```text
                    +-------------------+
                    | Streamlit UI      |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | TriageService     |
                    +---------+---------+
                              |
        +---------------------+----------------------+
        |                                            |
        v                                            v
+-------------------+                    +-------------------+
| Severity Service  |                    | CrewAI Agent      |
| Routing Service   |                    | Explanation Layer |
| Documents Service |                    +-------------------+
+-------------------+
                              |
                              v
                    +-------------------+
                    | MCP Tool          |
                    | claims_triage     |
                    +-------------------+
```

---

## Project Structure

```text
claims-triage-agent/
│
├── app/
│   ├── agents/
│   │   └── triage_agent.py
│   ├── models/
│   │   ├── claim.py
│   │   └── triage_result.py
│   ├── services/
│   │   ├── severity_service.py
│   │   ├── routing_service.py
│   │   ├── documents_service.py
│   │   └── triage_service.py
│   ├── mcp/
│   │   ├── tool_contract.py
│   │   ├── tool_handler.py
│   │   └── server.py
│   └── config.py
│
├── ui/
│   └── streamlit_app.py
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .env
```

---

## Input Contract

The Claims Triage Agent expects an already validated claim:

```json
{
  "claim_id": "CLM-100245",
  "estimated_loss": 18000,
  "injury_reported": true,
  "police_report_uploaded": false,
  "fraud_score": 0.2
}
```

---

## Output Contract

```json
{
  "severity": "HIGH",
  "priority": "P1",
  "recommended_queue": "BODILY_INJURY_TEAM",
  "required_documents": [
    "Medical Report",
    "Repair Estimate",
    "Police Report"
  ],
  "reason": "Injury reported and estimated loss exceeds threshold. A bodily injury specialist queue is recommended."
}
```

---

## MCP Tool Contract

Tool name:

```text
claims_triage
```

Description:

```text
Determine claim severity, priority, recommended queue, required documents, and explanation for an already validated auto insurance claim.
```

Example MCP request:

```json
{
  "claim_id": "CLM-100245",
  "estimated_loss": 18000,
  "injury_reported": true,
  "police_report_uploaded": false,
  "fraud_score": 0.2
}
```

Example MCP response:

```json
{
  "severity": "HIGH",
  "priority": "P1",
  "recommended_queue": "BODILY_INJURY_TEAM",
  "required_documents": [
    "Medical Report",
    "Repair Estimate",
    "Police Report"
  ],
  "reason": "Injury reported and estimated loss exceeds threshold"
}
```

---

## Local Setup

Clone the repository:

```bash
git clone <your-repository-url>
cd claims-triage-agent
```

Create and activate a virtual environment.

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your-openai-key
```

---

## Run the Streamlit UI

```bash
python -m streamlit run ui/streamlit_app.py
```

Then open:

```text
http://localhost:8501
```

---

## Run the MCP Server

```bash
python -m app.mcp.server
```

The MCP server will expose one tool:

```text
claims_triage
```

---

## Quick MCP Test

Create a file named `test_mcp_tool.py`:

```python
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
```

Run:

```bash
python test_mcp_tool.py
```

---

## Deploy to Hugging Face Space

This project is designed to deploy to a Docker-based Hugging Face Space.

After creating the Space:

```bash
git remote add hf https://huggingface.co/spaces/<your-username>/claims-triage-agent
git push hf main
```

Add the following secret in the Space settings:

```text
OPENAI_API_KEY
```

---

## Current Scope

Included:

* Claims triage only
* Severity
* Priority
* Queue recommendation
* Required documents
* MCP exposure

Not Included:

* FNOL
* OCR
* Image analysis
* Fraud detection
* Policy validation
* Settlement
* Payments
* Correspondence

---

## Future Enhancements

* Strict JSON schema validation
* SQLite persistence
* Logging and audit trail
* Better UI styling
* Multiple CrewAI specialist agents
* Public MCP endpoint
* Deployment of Streamlit and MCP server together in Docker

---




