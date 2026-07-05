from agents.log_agent import analyze_logs
from agents.threat_agent import detect_threat
from agents.mitre_agent import map_mitre
from agents.risk_agent import assess_risk
from agents.report_agent import generate_report


def investigate_incident(log_text):
    """
    Runs the complete AI investigation pipeline.
    """

    # Step 1
    log_analysis = analyze_logs(log_text)

    # Step 2
    threat_analysis = detect_threat(log_analysis)

    # Step 3
    mitre_mapping = map_mitre(threat_analysis)

    # Step 4
    risk_assessment = assess_risk(
        threat_analysis,
        mitre_mapping
    )

    # Step 5
    incident_report = generate_report(
        log_analysis,
        threat_analysis,
        mitre_mapping,
        risk_assessment
    )

    return {
        "log": log_analysis,
        "threat": threat_analysis,
        "mitre": mitre_mapping,
        "risk": risk_assessment,
        "report": incident_report
    }