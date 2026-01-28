import streamlit as st

st.set_page_config(
    page_title="IntegriPharm — Data & IA (fictif)",
    page_icon="🧬",
    layout="wide",
)

st.title("🧬 IntegriPharm — Programme Data & IA (fictif)")
st.caption("Objectifs 2026 : Inspection FDA + fondations IA. Site biotech (fermentation 1 réacteur).")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Année de création", "2015")
with col2:
    st.metric("Effectif site", "220")
with col3:
    st.metric("Prochaine inspection", "mi-2026")

st.divider()

st.subheader("🎯 Contexte & priorités")
st.markdown(
    """
- Produit biotech **par fermentation** (procédé “révolutionnaire” **en 1 réacteur**) puis **purification**
- Inspection FDA **remote en 2022** (période COVID) : **gaps Data Integrity** identifiés
- Engagement actionnaires : **performance & productivité via data/IA**
- Besoin interne : **support opérationnel** pour tenir les 2 objectifs 2026
    - Préparer et réussir l’inspection FDA
    - Poser des fondations robustes pour les projets IA
"""
)

st.info(
    "Navigation : utilise le menu de gauche (pages Streamlit). "
    "Les pages contiennent des données d’exemple (mock) prêtes à être remplacées par tes vrais datasets."
)

st.subheader("🧭 Plan de lecture conseillé")
st.markdown(
    """
1. **Description entreprise** : cadre, risques, objectifs
2. **Enquête employés** : signaux terrain (verbatims structurés)
3. **Démarche CPV** : pipeline minimal viable CPV + data backbone
4. **Inspection** : focus compliance + dernière warning letter (externe)
5. **Dataset** : bacs à sable pour consulter et aligner les sources
"""
)
