import streamlit as st

st.set_page_config(page_title="Description entreprise — IntegriPharm", page_icon="🏭", layout="wide")

st.title("🏭 Description de l'entreprise **IntegriPharm**")

c1, c2 = st.columns(2)
with c1:
    st.subheader("🏢 Description synthétique")
    st.markdown(
        """
    **IntegriPharm**  
    - Créée en **2015**  
    - **Biotech** : fermentation (procédé en **1 réacteur**), puis **purification**  
    - **220 employés** sur site  
    - Inspection FDA **remote en 2022** : gaps d’intégrité des données  
    - Prochaine inspection : **mi-2026**  
    - Engagement actionnaires : améliorer performance & productivité via **data + IA**
    """
)
with c2:
    st.image("assets/Mockup.png")

st.divider()

st.subheader("🎯 Objectifs 2026")
c1, c2 = st.columns(2)
with c1:
    st.markdown(
        """
**1) Préparer et assurer l’inspection FDA**  
- Reprendre la main sur l’intégrité des données  
- Sécuriser l’usage des systèmes (droits, audit trails, traçabilité)  
- Standardiser les pratiques (naming, calculs, sources de vérité)
"""
    )
with c2:
    st.markdown(
        """
**2) Poser les fondations pour les projets IA**  
- Données fiables, gouvernées, accessibles  
- Interopérabilité des systèmes (LIMS / MES / logbooks / QMS / etc.)  
- Capacités de monitoring (CPV, tendances, signaux faibles)
"""
    )

st.divider()

st.subheader("⚠️ Risques clés (lecture ‘inspection-ready’)")
st.markdown(
    """
- **Shadow IT / Excels locaux** : divergence des chiffres et perte de traçabilité  
- **Accès & licences** : partage de comptes = gros drapeau rouge DI  
- **Hétérogénéité des calculs** : pas de “single source of truth”  
- **Retranscriptions lourdes** : perte de temps + erreurs + versioning  
- **Silos applicatifs** : systèmes achetés non connectés → data patchwork
"""
)

st.warning(
    "Point critique : si le site a déjà été ‘cartouché’ sur la data integrity en 2022, "
    "une inspection sur site en 2026 cherchera des preuves de remédiation systémique (pas juste des rustines)."
)

st.divider()

st.subheader("🧩 Deliverables typiques d’un programme 2026 (exemples)")
st.markdown(
    """
- Cartographie des systèmes & flux (as-is / to-be)
- Politique d’accès + gestion des identités (comptes nominaux, revues périodiques)
- Standard de calcul KPIs (TRS/OEE, rendement, déviations, etc.) + data dictionary
- Pipeline CPV minimal viable + tableaux de bord
- Playbook inspection (evidence pack, data requests, drill, Q&A)
"""
)
