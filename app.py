import streamlit as st

from agents.coordinator_agent import investigate_incident
from skills.agent_skills import AGENT_SKILLS

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI SOC Copilot",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.title("🛡️ AI SOC Copilot")

    st.markdown("### Multi-Agent Workflow")

    st.success("✅ Log Analysis Agent")
    st.success("✅ Threat Detection Agent")
    st.success("✅ MITRE Mapping Agent")
    st.success("✅ Risk Assessment Agent")
    st.success("✅ Report Generation Agent")

    st.divider()

    st.markdown("### 🧠 Agent Skills")

    for agent, skills in AGENT_SKILLS.items():

        with st.expander(agent):
            for skill in skills:
                st.write(f"✅ {skill}")

    st.divider()

    st.markdown("### ⚙️ Tech Stack")

    st.write("• Google Gemini")
    st.write("• Python")
    st.write("• Streamlit")
    st.write("• MCP Servers")
    st.write("• Multi-Agent AI")

    st.divider()

    st.markdown("### Supported Files")

    st.write("✔ TXT")
    st.write("✔ LOG")

# ---------------------------------------------------------
# Main Page
# ---------------------------------------------------------

st.title("🛡️ AI SOC Copilot")
st.subheader("Multi-Agent Security Incident Investigation Assistant")

st.info(
    "Upload a security log file to automatically analyze threats, "
    "map MITRE ATT&CK techniques, assess risk, and generate an "
    "AI-powered incident investigation report."
)

uploaded_file = st.file_uploader(
    "Upload Security Log File",
    type=["txt", "log"]
)

if uploaded_file:

    log_text = uploaded_file.read().decode("utf-8")

    with st.expander("📄 View Uploaded Logs"):
        st.code(log_text)

    if st.button("🚀 Analyze Incident"):

        with st.spinner("Running AI Investigation..."):

            try:
                result = investigate_incident(log_text)

            except Exception as e:

                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    st.error("⚠️ Gemini API quota exceeded.")
                    st.info(
                        "Please wait a few minutes and try again, or use another Gemini API key."
                    )
                else:
                    st.error(f"Unexpected error:\n\n{e}")

                st.stop()

        st.success("✅ Analysis Complete!")

        st.divider()

        # ---------------------------------------------------------
        # Summary Metrics
        # ---------------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Threat",
                result["threat"].threat_name
            )

        with col2:

            severity = result["risk"].severity

            if severity == "Critical":
                st.error("🔴 Critical")
            elif severity == "High":
                st.warning("🟠 High")
            elif severity == "Medium":
                st.info("🟡 Medium")
            else:
                st.success("🟢 Low")

        with col3:

            st.metric(
                "Risk Score",
                result["risk"].risk_score
            )

            st.progress(result["risk"].risk_score / 100)

        st.divider()

        # ---------------------------------------------------------
        # Attack Summary
        # ---------------------------------------------------------

        st.subheader("📄 Attack Summary")

        st.write(f"**Attack Type:** {result['log'].attack_type}")

        st.write(
            f"**Failed Login Attempts:** {result['log'].failed_login_count}"
        )

        st.write("**Suspicious IP Addresses:**")

        for ip in result["log"].suspicious_ips:
            st.code(ip)

        st.divider()

        # ---------------------------------------------------------
        # Tabs
        # ---------------------------------------------------------

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "🛡 Threat",
                "🎯 MITRE",
                "📄 Report",
                "✅ Recommendations",
            ]
        )

        # ---------------------------------------------------------
        # Threat
        # ---------------------------------------------------------

        with tab1:

            st.subheader("Threat Analysis")

            st.write(
                f"**Threat Name:** {result['threat'].threat_name}"
            )

            st.write(
                f"**Severity:** {result['threat'].severity}"
            )

            st.metric(
                "Confidence",
                f"{result['threat'].confidence}%"
            )

            st.subheader("Recommendation")

            st.write(result["threat"].recommendation)

        # ---------------------------------------------------------
        # MITRE
        # ---------------------------------------------------------

        with tab2:

            st.subheader("MITRE ATT&CK")

            st.write(
                f"**Technique ID:** {result['mitre'].technique_id}"
            )

            st.write(
                f"**Technique Name:** {result['mitre'].technique_name}"
            )

            st.write(result["mitre"].explanation)

        # ---------------------------------------------------------
        # Report
        # ---------------------------------------------------------

        with tab3:

            st.subheader("Executive Summary")

            st.write(result["report"].executive_summary)

            st.subheader("Findings")

            st.write(result["report"].findings)

        # ---------------------------------------------------------
        # Recommendations
        # ---------------------------------------------------------

        with tab4:

            st.subheader("Recommendations")

            st.write(result["report"].recommendations)

        # ---------------------------------------------------------
        # Download Report
        # ---------------------------------------------------------

        report_text = f"""
==================================================
           AI SOC COPILOT INCIDENT REPORT
==================================================

Incident Title:
{result["report"].incident_title}

--------------------------------------------------

Executive Summary
-----------------
{result["report"].executive_summary}

--------------------------------------------------

Findings
--------
{result["report"].findings}

--------------------------------------------------

MITRE ATT&CK Mapping
--------------------
{result["report"].mitre_mapping}

--------------------------------------------------

Risk Assessment
---------------
{result["report"].risk_assessment}

--------------------------------------------------

Recommendations
---------------
{result["report"].recommendations}

==================================================
Generated by AI SOC Copilot
Developed by Lata Nimbalkar
==================================================
"""

        st.download_button(
            label="📥 Download Incident Report",
            data=report_text,
            file_name="incident_report.txt",
            mime="text/plain",
        )

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "🛡️ AI SOC Copilot | Kaggle AI Agents Capstone Project (2026)\n"
    "Developed by Lata Nimbalkar | Powered by Google Gemini, MCP Servers, and Streamlit"
)