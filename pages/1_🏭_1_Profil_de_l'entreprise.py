import streamlit as st
from utils import sidebar_logo

st.set_page_config(page_title="Description entreprise — IntegriPharm", page_icon="🏭", layout="wide")

sidebar_logo("assets/logo_ebi_a3p.png", logo_height=200, reserve_space=0, margin_top=10)

st.title("🏭 Profil de l'entreprise")
tab1, tab2, tab3 = st.tabs(
    ["🗂️ Description", "🎯 Objectifs 2026", "👥 Organigramme"]
)

with tab1:
    st.subheader("🗂️ Description synthétique de l'entreprise")
    c1, c2, c3 = st.columns([1,2,1])
    with c1:
        var=1
    with c2:
        st.image("assets/Mockup.png")
    with c3:
        var=1
        
    st.markdown(
        """
    - Entreprise pharmaceutique créée en 2015.
    - Dirigeant actuel : Jean-Luc Intègre.
    - L'entreprise assure la production de son produit phare l'**Integrivex**, depuis la fabrication jusqu'au packaging.
    - Le site de production unique de l'entreprise compte actuellement 250 employés. Pour anticiper les prévisions de croissance, l'entreprise envisage d'embaucher une cinquantaine d'opérateurs et techniciens de fabrication sur l'année 2026.
    - La dernière inspection FDA (Pre-Approval Inspection) s'est déroulée en 2025. Cette dernière a mis en évidence des écarts significatifs en matière d'intégrité des données.  
    - La prochaine inspection FDA est prévue en septembre 2026 et un des objectifs structurants du site est de réussir cette inspection retour. 
    """)

with tab2:
    st.subheader("🎯 Les objectifs 2026")
    st.markdown(
            """
    - **Renforcer le système qualité afin que l'inspection FDA à venir soit un succès**  
    - **Reprendre la main sur l'intégrité des données**
    - **Intégrer 50 nouveaux opérateurs dans les équipes de production**
    """
        )

with tab3:
    st.subheader("👥 Organigramme de l'équipe IntegriPharm")
    st.image("assets/Organigramme Integripharm.png")
