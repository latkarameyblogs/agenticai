class RoutingService:
    def determine_queue(self, severity: str, injury_reported: bool) -> str:
        if injury_reported:
            return "BODILY_INJURY_TEAM"

        if severity == "HIGH":
            return "SENIOR_ADJUSTER_QUEUE"

        if severity == "MEDIUM":
            return "STANDARD_ADJUSTER_QUEUE"

        return "FAST_TRACK_QUEUE"