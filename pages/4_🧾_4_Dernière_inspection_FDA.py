import streamlit as st

st.set_page_config(page_title="Inspection — IntegriPharm", page_icon="🧾", layout="wide")

st.title("🧾 Inspection (FDA) — Focus Data Integrity & références")
st.caption("Page pédagogique : ressources externes + lecture structurée.")

st.subheader("📌 Dernière Warning Letter (FDA) — repère externe récent")
st.markdown(
    """
Sur le registre FDA des Warning Letters, les entrées les plus récentes sont **postées au 23/12/2025**.
Une des lettres CGMP ‘Drugs’ récemment publiée (datée **16/12/2025**) concerne **Guangdong Renhe Guozhuang Biotechnology Co., Ltd.** :contentReference[oaicite:1]{index=1}
"""
)

with st.expander("Voir le lien + points saillants (résumé)"):
    st.markdown(
        """
**Lien (FDA)** : page warning letter du 16/12/2025 (postée 23/12/2025) :contentReference[oaicite:2]{index=2}

**Thèmes saillants (extraits résumés)**
- Release testing insuffisant / données non fournies
- Identity testing composants (21 CFR 211.84)
- Procédures process control (21 CFR 211.100) + validation
- Recommandation de consultant CGMP / audit “six-system”
"""
    )

st.divider()

st.subheader("🧠 Clarifier : Warning Letter vs Form 483 (important)")
st.markdown(
    """
- **Form FDA 483** = observations à la fin d’une inspection (ce que l’inspecteur a vu)
- **Warning Letter** = escalade formelle (quand la réponse/corrections sont jugées insuffisantes ou que les écarts sont significatifs)
"""
)

st.subheader("📎 Où suivre les observations 483 (agrégées) ?")
st.markdown(
    """
FDA publie une page “Inspection Observations” avec des **spreadsheets par année fiscale** (agrégats d’observations associées aux 483 générés par outils électroniques). :contentReference[oaicite:3]{index=3}

Pour des documents inspection/compliance, FDA renvoie aussi vers des espaces FOIA / reading rooms (selon périmètre). :contentReference[oaicite:4]{index=4}
"""
)

st.info(
    "Dans ton cas (IntegriPharm) : l’objectif n’est pas de ‘citer une lettre’, "
    "mais de transformer ces thèmes en checklist preuves + remédiations mesurables."
)

st.divider()

st.subheader("✅ Checklist ‘data integrity’ (ultra opérationnelle)")
st.markdown(
    """
- Comptes **nominatifs** (fin du partage) + revues périodiques des accès
- Audit trails : activation, revue, exceptions, retention
- “Single source of truth” : dictionnaire de données + formules KPI validées
- Interop (ou à défaut : procédures d’export/import contrôlées + versioning)
- Naming & gestion documentaire : règles + contrôles + ownership
- CAPA : preuves, efficacité, délais, re-test
"""
)
