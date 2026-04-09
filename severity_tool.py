def get_severity(claim):
    estimated_loss = claim.get("estimated_loss", 0)
    injury = claim.get("injury_reported", False)

    if injury:
        return "HIGH"

    if estimated_loss > 15000:
        return "HIGH"
    elif estimated_loss > 5000:
        return "MEDIUM"
    else:
        return "LOW"