class DocumentsService:
    def get_missing_documents(
        self,
        estimated_loss: float,
        injury_reported: bool,
        police_report_uploaded: bool,
    ):
        documents = []

        if injury_reported:
            documents.append("Medical Report")

        if estimated_loss > 5000:
            documents.append("Repair Estimate")

        if not police_report_uploaded:
            documents.append("Police Report")

        return documents