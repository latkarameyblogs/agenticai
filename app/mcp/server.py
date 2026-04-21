from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mcp.server.fastmcp import FastMCP

from app.mcp.tool_contract import CLAIMS_TRIAGE_TOOL_CONTRACT
from app.mcp.tool_handler import execute_claims_triage

mcp = FastMCP(
    "claims-triage-server",
    host="claims-triage-mcp.onrender.com"
)


@mcp.tool(
    name=CLAIMS_TRIAGE_TOOL_CONTRACT["name"],
    description=CLAIMS_TRIAGE_TOOL_CONTRACT["description"],
)
def claims_triage(
    claim_id: str,
    estimated_loss: float,
    injury_reported: bool,
    police_report_uploaded: bool,
    fraud_score: float,
):
    return execute_claims_triage(
        {
            "claim_id": claim_id,
            "estimated_loss": estimated_loss,
            "injury_reported": injury_reported,
            "police_report_uploaded": police_report_uploaded,
            "fraud_score": fraud_score,
        }
    )


app = FastAPI(title="Claims Triage MCP Server")


@app.get("/")
def health():
    return JSONResponse(
        {
            "status": "ok",
            "service": "claims-triage-mcp",
            "tool": "claims_triage",
        }
    )


app.mount("/mcp", mcp.streamable_http_app())