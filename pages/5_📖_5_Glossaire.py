import streamlit as st
import yaml
from utils import sidebar_logo

st.set_page_config(page_title="Glossaire — IntegriPharm", page_icon="📖", layout="wide")

sidebar_logo("assets/logo_ebi_a3p.png", logo_height=200, reserve_space=0, margin_top=10)

st.title("📖 Glossaire — Intégrité des données")

st.markdown(
    "Retrouvez ici les définitions des termes clés liés à l'**intégrité des données** "
    "dans l'industrie pharmaceutique."
)
# Image d'en-tête
a, b, c = st.columns([2,3,2])
with a:
    lapin=1
with b:
    st.image("assets/glossary.jpg", use_container_width=True)
with c: 
    lapin =1

# Chargement du fichier YAML
def load_glossaire():
    with open("assets/glossaire_data_integrity.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["glossaire"]

glossaire = load_glossaire()

st.markdown("---")

# Affichage des termes — regroupement par lettre initiale
lettres = sorted(set(item["terme"][0].upper() for item in glossaire))

for lettre in lettres:
        groupe = [item for item in glossaire if item["terme"][0].upper() == lettre]
        st.markdown(f"## {lettre}")
        cols = st.columns(2)
        for i, item in enumerate(groupe):
            with cols[i % 2]:
                with st.container(border=True):
                    st.markdown(f"### 🏷️ {item['terme']}")
                    st.markdown(item["definition"].strip())
                    if item.get("references"):
                        refs = " · ".join(item["references"])
                        st.caption(f"📚 {refs}")
        st.markdown("")
