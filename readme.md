# Claims Triage Agent

An industry-style Auto Insurance Claims Triage Agent built with CrewAI, Streamlit, and MCP.

This project is intentionally limited to the Claims Triage stage in the insurance claims lifecycle.

```text
Policy Validation -> Fraud Detection -> Claims Triage -> Claim Assignment
```

The application assumes that:

* Policy validation has already been completed
* Fraud score has already been calculated
* FNOL, OCR, image analysis, and claim settlement are handled elsewhere

The agent determines:

* Claim severity
* Claim priority
* Recommended queue
* Required documents
* Business explanation

---

## Features

* Streamlit UI for human users
* CrewAI-based Claims Triage Agent
* MCP tool exposure so other agents can reuse triage capability
* Structured claim input and triage output using Pydantic
* Simple rule-based services plus LLM explanation
* Ready for deployment on Hugging Face Spaces

---

## Architecture

```text
                    +-------------------+
                    | Streamlit UI      |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    | TriageService     |
                    +---------+---------+
                              |
        +---------------------+----------------------+
        |                                            |
        v                                            v
+-------------------+                    +-------------------+
| Severity Service  |                    | CrewAI Agent      |
| Routing Service   |                    | Explanation Layer |
| Documents Service |                    +-------------------+
+-------------------+
                              |
                              v
                    +-------------------+
                    | MCP Tool          |
                    | claims_triage     |
                    +-------------------+
```

---

