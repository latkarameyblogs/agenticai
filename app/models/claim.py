from pydantic import BaseModel


class Claim(BaseModel):
    claim_id: str
    estimated_loss: float
    injury_reported: bool
    police_report_uploaded: bool
    fraud_score: float