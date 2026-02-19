import streamlit as st
from utils import sidebar_logo

st.set_page_config(page_title="Inspection — IntegriPharm", page_icon="🧾", layout="wide")

sidebar_logo("assets/logo_ebi_a3p.png", logo_height=200, reserve_space=0, margin_top=10)

st.title("🧾 Résultat de la dernière inspection FDA")

st.markdown(
    """
    Voici le contenu de la warning letter publique adressée au CEO d'Integripharm en 2022 : 
""")

warning_letter = """
Dear **Mr. Jean-Luc Intègre**,

The U.S. Food and Drug Administration (FDA) inspected your drug manufacturing facility, Integripharm, and identified significant violations of Current Good Manufacturing Practice (CGMP) regulations (21 CFR parts 210 and 211).

Because your methods and controls do not conform to CGMP, your drug products are adulterated within the meaning of section 501(a)(2)(B) of the FD&C Act.
### Observed Deficiencies

##### 1. Uncontrolled Weighing Documentation - 21 CFR § 211.188(b)(11) and 21 CFR § 211.194(a)

**Uncontrolled and non-conform weighing ticket was found inside a trash bin without explanation.**  
A non-compliant weighing ticket was discovered in the equipment, and personnel were unable to provide traceability, investigation records, or justification for its presence.

##### 2. System Time Manipulation - 21 CFR § 211.68(b) and 21 CFR § 11.10(a)

**The production control software allowed manual modification of system time.**  
Our investigator was able to change the system clock without restriction, compromising the reliability and chronological integrity of electronic records and audit trails.
By the way, this modification does not appear in the system's audit trail. This finding reflects a lack of validation of the concerned computerized system.

##### 3. Pre-Signed Production Documentation - 21 CFR § 211.100(b)

**Production start-up documentation was pre-signed prior to execution of operations.**  
An operator had signed the start-up control form before the related manufacturing steps were performed, calling into question the contemporaneous and attributable nature of the records.

##### 4. Shared Generic User Accounts - 21 CFR § 11.100(a) and 21 CFR § 11.10(g)

**Shared generic user accounts were used within the supervisory module.**  
The use of team-based accounts (“*Equipe A/B/C*”) by multiple operators prevented individual attribution of actions and undermined data integrity and accountability.

These deficiencies demonstrate inadequate controls over documentation practices, computerized systems, and quality oversight. No deviation was initiated to manage the discrepancies observed during the inspection.

You are responsible for investigating these violations, determining their root causes, and implementing sustainable corrective actions to ensure ongoing compliance with CGMP.

You must respond in writing within 15 working days of receipt of this letter, specifying corrective actions taken and planned, including timelines for completion.

**Sincerely,**  
/S/  
Steven Spielberg ;)  
Program Division Director  
U.S. Food and Drug Administration
"""

with st.container():
    st.markdown(
        f"""
        <div style="
            border:1px solid #ccc;
            padding:15px;
            border-radius:10px;
            max-height:650px;
            overflow-y:auto;
            background-color:#f9f9f9;">
{warning_letter}
</div>""",
        unsafe_allow_html=True
    )

st.markdown(
    """
    
""")
st.markdown(
    """
    En réponse à cette *Warning Letter*, un plan d'action a été communiqué à la FDA. 
    Ce dernier se concentrait spécifiquement sur la resensibilisation des opérateurs concernés par les différents écarts observés en inspection. 
""")