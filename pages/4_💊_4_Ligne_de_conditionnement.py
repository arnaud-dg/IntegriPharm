from pathlib import Path

import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from utils import sidebar_logo


def embed_pdf(pdf_path: str, height: int = 1200) -> None:
    path = Path(pdf_path)
    if not path.exists():
        st.error(f"Fichier introuvable : {pdf_path}")
        return
    _, col, _ = st.columns([0.14, 0.72, 0.14])
    with col:
        with st.container(border=True):
            pdf_viewer(str(path), height=height, width="100%", zoom_level=1.5)

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
    embed_pdf("data/SOP.pdf")

with tab4:
    st.subheader("🧾 Dossier de lot")
    embed_pdf("data/DDL.pdf")

    st.divider()

    st.markdown("#### Glossaire des acronymes")
    acronymes = {
        "Acronyme": ["BLPR", "C / NC", "CIP", "DOD", "GTIN", "GS1", "MO", "NA", "OCV", "OF"],
        "Signification": [
            "Blister Primaire",
            "Conforme / Non-Conforme",
            "Code Identifiant de Présentation",
            "Drop On Demand",
            "Global Trade Item Number",
            "Global Standards One",
            "Mode Opératoire",
            "Non Applicable",
            "Optical Character Verification",
            "Ordre de fabrication",
        ],
        "Contexte": [
            "Code article du composant prévu dans l'OF.",
            "Terme utilisé pour valider / invalider un contrôle.",
            "Code français, utilisé pour identifier de manière unique une présentation précise d'un médicament (dosage, forme, conditionnement, etc.).",
            "Technologie d'impression jet d'encre où l'imprimante éjecte une goutte d'encre uniquement lorsqu'elle doit imprimer, à l'inverse du jet d'encre continu.",
            "Identifiant international, normalisé par GS1, utilisé pour identifier de manière unique tout produit commercialisé dans le monde.",
            "Organisation internationale qui développe et maintient les normes mondiales d'identification, dont le GTIN, le GLN, le SSCC, les codes-barres EAN/UPC, et les GS1 DataMatrix utilisés en santé, logistique, distribution et industrie.",
            "Séquençage des tâches à réaliser, défini dans le mode opératoire du système MES.",
            "Terme utilisé pour acter la non applicabilité de la tâche.",
            "Vérification visuelle humaine des caractères imprimés sur un emballage.",
            "Référence unique d'une fabrication contenant la liste des composants, les quantités et la liste des opérations.",
        ],
    }
    import pandas as pd
    df_acronymes = pd.DataFrame(acronymes)
    st.dataframe(df_acronymes, use_container_width=True, hide_index=True)