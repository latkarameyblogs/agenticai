import streamlit as st
from triage_agent import triage_claim

st.title("Claims Triage Agent")

estimated_loss = st.number_input("Estimated Loss", min_value=0)
injury_reported = st.checkbox("Injury Reported")
police_report_uploaded = st.checkbox("Police Report Uploaded")

if st.button("Run Triage"):
    claim = {
        "estimated_loss": estimated_loss,
        "injury_reported": injury_reported,
        "police_report_uploaded": police_report_uploaded,
    }

    result = triage_claim(claim)

    st.subheader("Triage Result")
    st.json(result)