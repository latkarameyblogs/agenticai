def get_required_documents(claim):
    docs = []

    if claim.get("injury_reported"):
        docs.append("Medical Report")

    if claim.get("estimated_loss", 0) > 5000:
        docs.append("Repair Estimate")

    if not claim.get("police_report_uploaded"):
        docs.append("Police Report")

    return docs