import streamlit as st
import pandas as pd

st.set_page_config(page_title="Enquête employés — IntegriPharm", page_icon="🗣️", layout="wide")

st.title("🗣️ Résultat de l'enquête employés")

SEPARATOR = "\n\n" + ("—" * 48) + "\n\n"

verbatims_struct = [
    {
        "Prenom": "Camille",
        "NomInitiale": "D.",
        "Service": "Assurance Qualité",
        "Intitule": "Quality Systems Specialist",
        "Verbatim": "Franchement, la retranscription… c’est super lourd. On perd un temps fou à recopier, vérifier, re-coller dans des templates, et au final personne n’est sûr d’avoir la bonne version."
    },
    {
        "Prenom": "Mehdi",
        "NomInitiale": "L.",
        "Service": "Production — Fermentation",
        "Intitule": "Superviseur de production",
        "Verbatim": "Le problème, c’est que les rôles et responsabilités sont pas hyper clairs. Du coup quand il y a un écart, tout le monde se renvoie la balle et on avance pas."
    },
    {
        "Prenom": "Sophie",
        "NomInitiale": "R.",
        "Service": "Performance Industrielle",
        "Intitule": "Ingénieure Méthodes / OEE",
        "Verbatim": "On a plusieurs façons de calculer les mêmes KPI… donc on se comprend pas. Un jour on me sort un TRS à 62%, le lendemain 70%, et tout le monde dit que c’est ‘la bonne formule’."
    },
    {
        "Prenom": "Thomas",
        "NomInitiale": "B.",
        "Service": "Contrôle de Gestion Industriel",
        "Intitule": "Analyste performance",
        "Verbatim": "Le challenge, c’est d’éviter que chacun crée son Excel de son côté. Parce qu’après on a 15 fichiers, 15 versions, et personne n’ose trancher sur la source officielle."
    },
    {
        "Prenom": "Nina",
        "NomInitiale": "K.",
        "Service": "IT / Systèmes",
        "Intitule": "Application Owner",
        "Verbatim": "On achète des systèmes, mais ils communiquent pas entre eux. Et parfois on n’a même pas assez de licences… donc oui, on se retrouve à partager des comptes, c’est pas idéal du tout."
    },
    {
        "Prenom": "Julien",
        "NomInitiale": "P.",
        "Service": "Production — Purification",
        "Intitule": "Technicien procédé",
        "Verbatim": "J’ai plein d’idées sur les données de prod, mais c’est une galère d’accéder à l’info. Je dois demander à trois personnes, attendre, et au final j’abandonne."
    },
    {
        "Prenom": "Laura",
        "NomInitiale": "S.",
        "Service": "Data / Digital",
        "Intitule": "Data Steward",
        "Verbatim": "Les collègues du service d’à côté respectent pas nos règles de nommage. Ça paraît bête, mais derrière on ne retrouve rien, et on perd la traçabilité."
    },
    {
        "Prenom": "Eric",
        "NomInitiale": "M.",
        "Service": "Assurance Qualité",
        "Intitule": "QA Compliance Manager",
        "Verbatim": "À la dernière inspection, on s’est fait cartoucher sur la data integrity. Honnêtement, on a eu de la chance que ce soit remote… sur site, ils auraient vu bien plus d’écarts."
    },
]

df = pd.DataFrame(verbatims_struct)

st.subheader("🧾 Verbatims employés")
full_text = SEPARATOR.join(
    [
        f"{row['Prenom']} {row['NomInitiale']} — {row['Service']} — {row['Intitule']}\n"
        f"“{row['Verbatim']}”"
        for _, row in df.iterrows()
    ]
)
st.text_area("Liste des verbatims", full_text, height=1200)