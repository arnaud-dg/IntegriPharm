import streamlit as st
from utils import sidebar_logo, pdf_download_button

st.set_page_config(
    page_title="IntegriPharm — Data & IA (fictif)",
    page_icon="🧬",
    layout="wide",
)

sidebar_logo("assets/logo_ebi_a3p.png", logo_height=200, reserve_space=0, margin_top=10)

st.title("Bienvenue chez **IntegriPharm**")

st.markdown("""
            Ce site sert de support au serious game « **IntegriPharm** » permettant de découvrir les concepts d'ALCOA+ et de data integrity dans un contexte industriel.
            """)

st.divider()

st.subheader("🎯 Contexte")
st.markdown(
    """
**IntegriPharm** est un site pharmaceutique stratégique produisant un médicament critique pour le marché américain.
Dans 90 jours, une inspection de la U.S. Food and Drug Administration est annoncée. Le site a déjà reçu une *Warning Letter* lors de sa précédente inspection.
Un signalement interne récent mentionne des pratiques douteuses sur la gestion des données.

Si l'inspection échoue, les conséquences seront dramatiques:
- Risque de nouvelle Warning Letter et de mise en demeure
- Suspension d'export vers les États-Unis
- Impact financier majeur
- Perte de crédibilité du site

**Vous êtes mandatés par la Direction pour éviter ce scénario catastrophe !**
"""
)

st.divider()

st.subheader("🧭 Votre rôle")
c1, c2 = st.columns([1,2])
with c1:
    st.image("assets/We want you.jpg")
with c2:
    st.markdown("""
    Vous êtes un groupe de nouveaux responsables Production et Assurance Qualité.
    
    Votre mission :
    - **Identifier les dérives possibles et réelles en matière de Data Integrity**
    - Évaluer le niveau de **risque**
    - Construire un plan d'action priorisé, réaliste et défendable face aux inspecteurs

    La Direction vous laisse carte blanche … mais le temps est compté.
    """)

st.divider()

st.subheader("🧭 Déroulé du *serious game*")
st.markdown("""
**🕵️ Phase 1 – Diagnostic (1h15 environ)**
            
- Lister les écarts liés aux principes ALCOA+
- Détecter les risques sur l'intégrité des données relative au procédé de conditionnement
- Classer ces écarts par niveau de risque
- Identifier et hiérarchiser les causes racines communes aux différents écarts (à la manière d'un "5 Pourquois")

**Livrable de cette étape** : Un diagnostic structuré avec cartographie des risques.         
""")

st.divider()

st.markdown("""
**🛠 Phase 2 – Plan d'action (1 heure environ)**

Maintenant que le diagnostic est posé, vous devez bâtir un plan d'action de remédiation.
                     
Vous disposez :
- D'un budget limité
- D'un nombre limité de ressources internes
- D'un délai de 90 jours
            
A vous de prioriser et d'arbitrer entre les différentes actions possibles afin de construire un plan cohérent, réaliste et défendable.

**Livrable de cette étape** : Un plan d'action arbitré.            
""")

st.divider()

st.markdown("""
**🎤 Restitution collective**

Afin de confronter les points de vue, chaque équipe disposera de 8 minutes pour livrer les grandes lignes de son diagnostic et justifier son plan d'action.      
""")

st.divider()

st.info("""
⚠️ Merci de bien respecter et de ne pas modifier la structure des templates excel qui vont seront fournis pour effectuer cette analyse.""")

st.info("""
Certaines informations seront peut-être partielles, d'autres ambiguës, à vous de décider si il s'agit d'un risque réel ou d'un faux signal.
Vu la quantité d'information à parcourir, vous êtes invités à vous répartir les tâches, puis à consolider vos remarques. Il y a 3 sources de données différentes : 
- Les résultats de l'enquête menée auprès des employés
- La *warning letter* FDA
- Les documents à disposition (Dossier de Lot, SOP) en provenance du conditionnement

En cas de question, n'hésitez pas à vous manifester auprès des animateurs et à avancer de votre côté en attendant.
""")

st.divider()
pdf_download_button()
