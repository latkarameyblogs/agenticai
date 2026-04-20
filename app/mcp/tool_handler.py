from app.models.claim import Claim
from app.services.triage_service import TriageService


def execute_claims_triage(arguments: dict):
    claim = Claim(**arguments)

    service = TriageService()

    result = service.run(claim)

    return result