import streamlit as st
from utils import sidebar_logo

st.set_page_config(page_title="Démarche CPV — IntegriPharm", page_icon="📈", layout="wide")

sidebar_logo("assets/logo_ebi_a3p.png", logo_height=200, reserve_space=0, margin_top=10)

st.title("💊 Ligne de conditionnement")

tab1, tab2, tab3, tab4 = st.tabs(["🎥 Vidéo de la ligne","🔀 Diagramme fonctionnel","📋 SOP de conditionnement","🧾 Dossier de lot"])

with tab1: 
    st.subheader("🎥 Vidéo de la ligne")
    st.markdown(
        """
    Voici une illustration vidéo du type de ligne de conditionnement utilisée pour packager **l'Integrivex**.
    """
    )
    st.video("https://www.youtube.com/watch?v=ZWBIlqgVHsU")
    st.markdown(
        """
    *Vidéo publique utilisée à des fins éducatives (Jornen Machinery), www.jornen.com, https://www.youtube.com/watch?v=ZWBIlqgVHsU*
    """
    )

with tab2:
    st.subheader("🔀 Diagramme fonctionnel")
    st.markdown(
        """
    Voici un schéma qui représente de façon simplifiée les différentes étapes du procédé de conditionnement. Une dinstinction est faite entre : 
    - Le packaging primaire : emballage en contact direct avec le produit, qui le contient et le protège jusqu'à son utilisation
    - Le packaging secondaire : emballage  facilitant la présentation, l'information et la protection supplémentaire
    - Le packaging tertaire : emballage destiné au transport et au stockage en volume

    Le système de supervision ainsi que l'environnement documentaire sont aussi représentés ; 
    ils jouent un rôle capital dans les actions de pilotage, de paramétrage et de traçabilité du procédé de conditionnement.
    """
    )
    st.image("assets/Diagramme Condi.png", width="stretch")
    st.markdown(
        """
    Les flux d'information sont nombreux et sont représentés de façon extrêmement simplifiée. 
    L'analyse de la SOP de conditionnement et du dossier de lot permettront de comprendre finement les mouvements de données 
    """
    )

with tab3:
    st.subheader("📋 SOP de conditionnement")
    st.markdown("""**🚧 Work in Progress**""")

with tab4:
    st.subheader("🧾 Dossier de lot")
    st.markdown("""**🚧 Work in Progress**""")