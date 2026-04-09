class SeverityService:
    
    def calculate(self, estimated_loss: float, injury_reported: bool) -> str:
        if injury_reported:
            return "HIGH"

        if estimated_loss > 15000:
            return "HIGH"
        if estimated_loss > 5000:
            return "MEDIUM"

        return "LOW"