import streamlit as st

st.set_page_config(page_title="Description entreprise — IntegriPharm", page_icon="🏭", layout="wide")

st.title("🏭 Description de l'entreprise **IntegriPharm**")

c1, c2 = st.columns([2,1])
with c1:
    st.subheader("Description synthétique de l'entreprise")
    st.markdown(
        """
    - Entreprise pharmaceutique créée en 2015
    - Dirigeant actuel : Jean-Luc Intègre, CEO d'Integripharm
    - L'entreprise compte actuelle 220 employés  
    - Le produit phare est un produit biotechnologique produit par fermentation / purification 
    - La dernière inspection FDA s'est déroulée en remote en 2022. Cette dernière a mis en évidence des écarts significatifs en matière d'intégrité des données  
    - La prochaine inspection FDA est prévue en septembre 2026
    - Des engagements ont été pris auprès des actionnaires pour 2026 en ce qui concerne la performance industrielle. Le site souhaite lancer des projets
     d'amélioration de la Productivité à l'aide d'outils "data" et "IA".
    """
)
with c2:
    st.image("assets/Mockup.png")

st.divider()

st.subheader("Les objectifs 2026")
c1, c2 = st.columns(2)
with c1:
    st.markdown(
        """
**1) Améliorer le système qualité afin que l'inspection FDA soit un succès**  
- Reprendre la main sur l'intégrité des données
- Sécuriser l'usage des systèmes
- Standardiser les pratiques
"""
    )
with c2:
    st.markdown(
        """
**2) Lancer les premières initiatives IA**  
- Identifier les sujets d'intérêts
- Evaluer si les données sont suffisantes et adaptées pour déployer les initiatives IA
"""
    )

st.divider()

st.subheader("Votre rôle")
c1, c2 = st.columns([3,1])
with c1:
    st.markdown(
        """
**Vous êtes une équipe de consultants en charge d'aider IntegriPharm a atteindre ses objectifs 2026 !**

**Sur la partie Qualité**
- Vous devrez à travers les informations qui vous ont été transmises réaliser un diagnostic mettant en lumière les points faibles de l'organisaton.
- Vous devrez aider l'entreprise à mettre en place les actions de remédiation qui s'imposent dans une perspectif court-terme et long-terme.

**Sur la partie Performance**
- Vous devrez aider les équipes à identifier les bons sujets et les bons axes d'amélioration.
- Vous devrez garantir que les données sont adaptées à ces projets, et dans le cas contraire proposer des actions de remédiation.
"""
    )
with c2:
    st.image("assets/We want you.jpg")
