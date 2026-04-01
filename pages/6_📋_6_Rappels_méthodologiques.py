import streamlit as st
from utils import sidebar_logo

st.set_page_config(page_title="Rappels méthodologiques — IntegriPharm", page_icon="📋", layout="wide")

sidebar_logo("assets/logo_ebi_a3p.png", logo_height=200, reserve_space=0, margin_top=10)

st.title("📋 Quelques rappels méthodologiques")
st.markdown(
    "Voici une rapide synthèse des points clés méthodologiques relatifs à l'**intégrité des données**."
)
st.markdown("---")

slides = [
    {
        "image": "assets/Slide_24.jpg",
        "label": "Slide 24",
        "content": """
**Le contexte de l'industrie pharmaceutique actuelle** :

- Des environnement shybrides (documents papier + données électroniques)
- Un niveau de maturité technologique variable, d'un site à l'autre, d'un atelier à l'autre
- Des utilisateurs confrontés à différentes failles (complexité, multiplicité des systèmes, …) pouvant entraîner une **perte d'intégrité de données**
""",
    },
    {
        "image": "assets/Slide_26.jpg",
        "label": "Slide 26",
        "content": """
**Des obligations réglementaires** : 

- Évaluer *(en continu)* son système de gestion des données dans le but de garantir que l'**intégrité des données est maintenue**
- Identifier, et mettre sous contrôle, les **risques sur les données** (vulnérabilités)
- Implémenter des pratiques de **'Good Data Governance'**
""",
    },
    {
        "image": "assets/Slide_28.jpg",
        "label": "Slide 28",
        "content": """
**Garantir que toutes les données critiques** *(ayant un impact sur une décision pharmaceutique)* **respectent ALCOA**, c'est à dire qu'elles sont :

> *Attribuables — Lisibles — Contemporaines — Originales — Exactes*
> *Complètes - Cohérentes - Durables - Disponibles*
""",
    },
    {
        "image": "assets/Slide_32.jpg",
        "label": "Slide 32",
        "content": """
**La maîtrise s'appuie sur 3 couches** :

- Une **infrastructure maîtrisée** (droit d'accès, backup, …), y compris pour les applications SaaS ou autres
- Des **systèmes informatisés (GxP) validés**
- Une approche **Data Integrity** doit être définie et appliquée
""",
    },
    {
        "image": "assets/Slide_33.jpg",
        "label": "Slide 33",
        "content": """
Les systèmes et les données ne sont ni statiques, ni isolés. **L'approche Data Integrity** doit permettre de prévenir une perte d'intégrité sur tout le **cycle de vie de chaque donnée critique**.

Ce cycle de vie peut être représenté par un flux de données, à travers potentiellement plusieurs systèmes et/ou de l'hybride **Papier / Électronique**.
""",
    },
    {
        "image": "assets/Slide_35.jpg",
        "label": "Slide 35",
        "content": """
**L'approche Data Integrity** doit aboutir à la mise en place d'une **Data Gouvernance** fixant les dispositions :

- Techniques
- Organisationnelles
- Culturelles et Comportementales

Pour :
- **Prévenir les risques** *Data Integrity*
- **Détecter les failles potentielles**, et réagir aux situations pouvant entraîner une décision pharma incorrecte
""",
    },
    {
        "image": "assets/Slide_36.jpg",
        "label": "Slide 36",
        "content": """
**L'ensemble de la démarche** répond à un besoin de **Data Management**, ou *Bonnes Pratiques de Management des Données* :

- Identifier les **Données critiques**
- Poser le **cycle de vie** de ces données critiques
- Mener une **maîtrise des risques** selon ICH Q9, à savoir : 
  - Identifier et évaluer les situations de risques / perte d'ALCOA *(probabilité, gravité)*
  - Définir, mettre en place et surveiller l'efficacité des actions 
""",
    },
]

st.markdown("""
<style>
div[data-testid="stHorizontalBlock"] {
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

for slide in slides:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(slide["image"], use_container_width=True)
    with col2:
        with st.container(border=True):
            st.markdown(slide["content"])
    st.markdown("---")
