from app.models.claim import Claim
from app.services.severity_service import SeverityService


def test_high_severity_claim():
    claim = Claim(
        claim_id="CLM-1001",
        estimated_loss=20000,
        injury_reported=True,
        police_report_uploaded=False,
        fraud_score=0.2,
    )

    severity = SeverityService().calculate(
        claim.estimated_loss,
        claim.injury_reported,
    )

    assert severity == "HIGH"