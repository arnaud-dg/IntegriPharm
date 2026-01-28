# IntegriPharm - Programme Data & IA

Application Streamlit de tableau de bord pour le programme Data & IA d'IntegriPharm (site biotech fictif).

## Objectifs 2026

- Inspection FDA + fondations IA
- Site biotech (fermentation 1 reacteur)

## Structure du projet

```
IntegriPham/
├── app.py                 # Application principale Streamlit
├── pages/                 # Pages Streamlit
│   ├── 1_Profil_de_l'entreprise.py
│   ├── 2_Enquete_employes.py
│   ├── 3_Demarche_CPV.py
│   ├── 4_Derniere_inspection_FDA.py
│   └── 5_Datasets.py
├── assets/                # Images et ressources
├── data/                  # Donnees
└── requirements.txt       # Dependances Python
```

## Installation

```bash
# Creer un environnement virtuel
python -m venv venv

# Activer l'environnement (Windows)
venv\Scripts\activate

# Installer les dependances
pip install -r requirements.txt
```

## Lancement

```bash
streamlit run app.py
```

## Contenu

1. **Profil de l'entreprise** : cadre, risques, objectifs
2. **Enquete employes** : signaux terrain (verbatims structures)
3. **Demarche CPV** : pipeline minimal viable CPV + data backbone
4. **Inspection FDA** : focus compliance + derniere warning letter
5. **Datasets** : bacs a sable pour consulter et aligner les sources
