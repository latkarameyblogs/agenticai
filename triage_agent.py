from severity_tool import get_severity
from routing_tool import get_queue
from documents_tool import get_required_documents


def triage_claim(claim):
    severity = get_severity(claim)
    queue = get_queue(claim, severity)
    documents = get_required_documents(claim)

    if severity == "HIGH":
        priority = "P1"
    elif severity == "MEDIUM":
        priority = "P2"
    else:
        priority = "P3"

    return {
        "severity": severity,
        "priority": priority,
        "recommended_queue": queue,
        "required_documents": documents,
    }