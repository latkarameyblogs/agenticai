
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from mcp.server.fastmcp import FastMCP

from app.mcp.tool_contract import CLAIMS_TRIAGE_TOOL_CONTRACT
from app.mcp.tool_handler import execute_claims_triage

mcp = FastMCP("claims-triage-server")


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


# Base MCP HTTP app
mcp_app = mcp.streamable_http_app()

# Wrap it with Starlette so we can add CORS
app = Starlette()
app.mount("/", mcp_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:6274", "*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

