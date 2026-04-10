import os
import sys
sys.path.append(os.path.abspath("."))

import streamlit as st


from app.models.claim import Claim
from app.models.triage_result import TriageResult
from app.services.triage_service import TriageService


st.set_page_config(
    page_title="Claims Triage Agent",
    page_icon="🚗",
    layout="centered",
)

st.title("🚗 Claims Triage Agent")
st.caption("Industry-style Claims Triage MVP")

with st.form("triage_form"):
    claim_id = st.text_input("Claim ID", value="CLM-100245")

    estimated_loss = st.number_input(
        "Estimated Loss ($)",
        min_value=0.0,
        value=18000.0,
    )

    injury_reported = st.checkbox("Injury Reported", value=True)

    police_report_uploaded = st.checkbox(
        "Police Report Uploaded",
        value=False,
    )

    fraud_score = st.slider(
        "Fraud Score",
        min_value=0.0,
        max_value=1.0,
        value=0.20,
        step=0.01,
    )

    submitted = st.form_submit_button("Run Triage")

if submitted:
    claim = Claim(
        claim_id=claim_id,
        estimated_loss=estimated_loss,
        injury_reported=injury_reported,
        police_report_uploaded=police_report_uploaded,
        fraud_score=fraud_score,
    )

    service = TriageService()
    result = service.run(claim)

    st.subheader("Triage Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Severity", result.get("severity", "UNKNOWN"))
        st.metric("Priority", result.get("priority", "UNKNOWN"))

    with col2:
        st.metric(
            "Recommended Queue",
            result.get("recommended_queue", "UNKNOWN"),
        )

    st.subheader("Required Documents")

    docs = result.get("required_documents", [])

    if docs:
        for doc in docs:
            st.write(f"• {doc}")
    else:
        st.write("No missing documents")

    st.subheader("Reason")
    st.info(result.get("reason", "No explanation available"))

    with st.expander("Raw JSON"):
        st.json(result)