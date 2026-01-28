import streamlit as st

st.set_page_config(page_title="Démarche CPV — IntegriPharm", page_icon="📈", layout="wide")

st.title("📈 Démarche CPV (Continued Process Verification)")
st.caption("Proposition de démarche CPV ‘MVP’ orientée inspection et industrialisation data/IA.")

st.subheader("1) Objectif CPV (pragmatique)")
st.markdown(
    """
- Démontrer que le procédé est **en état de contrôle** (surveillance continue)
- Détecter **dérives** et **signaux faibles** avant impact qualité
- Produire des **preuves** auditables (traçabilité, versioning, règles de calcul)
"""
)

st.divider()

st.subheader("2) MVP CPV (90 jours) — ce qui compte vraiment")
st.markdown(
    """
**Lot 1 — Socle “inspection-ready”**
- Inventaire des variables critiques (CPP/CQA) par étape (fermentation → purification)
- Standard de calcul (data dictionary + définition KPI + règles d’exclusion)
- Contrôles d’accès (comptes nominatifs) + traçabilité (audit trails)
- Pipeline de collecte minimal + horodatage + provenance

**Lot 2 — Monitoring & alerting**
- Tendances : contrôles statistiques simples (règles type Nelson/WECO si pertinent)
- Détection d’anomalies sur séries (basique, interprétable)
- Tableaux de bord : batch-to-batch, shift-to-shift, équipements, matières

**Lot 3 — Gouvernance**
- RACI clair (qui possède la donnée, qui valide la formule, qui publie)
- Change control sur formules & dashboards
- Routine mensuelle CPV (revue multi-métiers)
"""
)

st.divider()

st.subheader("3) Artefacts attendus (preuves)")
st.markdown(
    """
- Dossier CPV : périmètre, variables, fréquences, seuils
- Registre des modifications (formules, sources, dashboards)
- Journal d’accès / audit trails (systèmes critiques)
- Dossier “inspection pack” : captures, exports, procédures, exemples de revues
"""
)

st.warning(
    "Erreur classique : lancer du ML ‘sexy’ avant d’avoir verrouillé (1) l’accès nominatif, "
    "(2) les règles de calcul, (3) la source de vérité. En inspection, c’est l’inverse : preuves d’abord."
)

st.divider()

st.subheader("4) Piste IA (après socle)")
st.markdown(
    """
Quand le socle est stable :
- Modèles de dérive / prédiction (ex : rendement, durée de cycle, écart qualité)
- NLP sur déviations / logbooks (récurrence, clustering)
- Aide à l’investigation (recommandations + explications + traçabilité)
"""
)
