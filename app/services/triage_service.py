import json
from crewai import Crew, Task

from app.agents.triage_agent import build_triage_agent
from app.models.claim import Claim
from app.services.documents_service import DocumentsService
from app.services.routing_service import RoutingService
from app.services.severity_service import SeverityService

class TriageService:
    def run(self, claim: Claim):
        severity_service = SeverityService()
        routing_service = RoutingService()
        documents_service = DocumentsService()

        severity = severity_service.calculate(
            claim.estimated_loss,
            claim.injury_reported,
        )

        queue = routing_service.determine_queue(
            severity,
            claim.injury_reported,
        )

        documents = documents_service.get_missing_documents(
            claim.estimated_loss,
            claim.injury_reported,
            claim.police_report_uploaded,
        )

        if severity == "HIGH":
            priority = "P1"
        elif severity == "MEDIUM":
            priority = "P2"
        else:
            priority = "P3"

        agent = build_triage_agent()

        task = Task(
            description=f"""
            A validated claim has already been checked for policy validation and fraud.

            Claim ID: {claim.claim_id}
            Estimated Loss: {claim.estimated_loss}
            Injury Reported: {claim.injury_reported}
            Fraud Score: {claim.fraud_score}

            Determined Severity: {severity}
            Determined Priority: {priority}
            Recommended Queue: {queue}
            Missing Documents: {documents}

            Explain in business language why this claim received this severity,
            priority, queue, and required documents.

            Return only JSON in this exact format:

            {{
              "severity": "HIGH",
              "priority": "P1",
              "recommended_queue": "BODILY_INJURY_TEAM",
              "required_documents": ["Medical Report", "Police Report"],
              "reason": "Short explanation"
            }}
            """,
            expected_output="Valid JSON only",
            agent=agent,
        )

        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=True,
        )

        result = crew.kickoff()

        if hasattr(result, "raw"):
            result_text = result.raw
        else:
            result_text = str(result)

        try:
            return json.loads(result_text)
        except Exception:
            return {
                "severity": severity,
                "priority": priority,
                "recommended_queue": queue,
                "required_documents": documents,
                "reason": result_text,
            }