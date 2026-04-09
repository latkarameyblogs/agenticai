def get_queue(claim, severity):
    if claim.get("injury_reported"):
        return "BODILY_INJURY_TEAM"

    if severity == "HIGH":
        return "SENIOR_ADJUSTER_QUEUE"

    return "STANDARD_QUEUE"