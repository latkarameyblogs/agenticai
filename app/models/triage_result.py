from pydantic import BaseModel
from typing import List


class TriageResult(BaseModel):
    severity: str
    priority: str
    recommended_queue: str
    required_documents: List[str]
    reason: str