import streamlit as st
import pandas as pd
from utils import sidebar_logo

st.set_page_config(page_title="Enquête employés — IntegriPharm", page_icon="🗣️", layout="wide")

sidebar_logo("assets/logo_ebi_a3p.png", logo_height=200, reserve_space=0, margin_top=10)

st.title("🗣️ Résultat de l'enquête employés")

SEPARATOR = "\n\n" + ("—" * 48) + "\n\n"

verbatims_struct = [
    {
        "Prenom": "Jean-Luc Intègre",
        "NomInitiale": "",
        "Service": "IntegriPharm",
        "Intitule": "CEO",
        "Verbatim": "L'inspection de la FDA est un moment clé pour notre entreprise : elle conditionne notre crédibilité sur le marché américain"
        "… Une fois cette inspection passée avec succès, nous pourrons nous recentrer sur nos priorités business et opérationnelles ; l'objectif est avant tout de réussir ce rendez-vous précis."
    },
    {
        "Prenom": "Camille",
        "NomInitiale": "D.",
        "Service": "Assurance Qualité",
        "Intitule": "Directrice Qualité",
        "Verbatim": "La situation est sensible car nous avons encore énormément de travail avant l'inspection. L'inspection readiness est définitvement un enjeu qu'il faudra que je travaille. "
        "... Le management tolère certains écarts au nom des contraintes opérationnelles, ce qui fragilise notre culture qualité. Il faut que le Top management se mouille davantage et m'aide sur ces sujets"
    },
    {
        "Prenom": "Eric",
        "NomInitiale": "Z.",
        "Service": "Assurance Qualité",
        "Intitule": "Responsable Qualité Opérationnelle",
        "Verbatim": "Je ne suis pas sûr ici que les gens comprennent bien que la qualité et la Data Integrity c'est l'affaire de tous. Très souvent, les gens se reposent sur nous et imaginent que dès qu'il y a un sujet déviation ou Data Integrity c'est forcément l'affaire de la qualité."
        "Il y a un autre problème ; quand je compare avec mon ancienne entreprise, je trouve que, ici, la Data Integrity n'est pas assez représentée dans les analyses de risques, la démarche de Change Control et les dashboards de reporting"
    },
    {
        "Prenom": "Nina",
        "NomInitiale": "K.",
        "Service": "Assurance Qualité",
        "Intitule": "Qualification/Validation Expert",
        "Verbatim": "J'ai un vrai problème de bande passante ! Tous les projets sont urgents et on doit tout gérer de front. … Le choix des fournisseurs se fait à la va-vite et on en paye parfois les pots cassés. "
        "Après, quand il y a un écart, tout le monde se renvoie la balle et on avance pas. ... Je constate qu'on a aussi beaucoup mal à passer du mode projet au mode routine. Dans le cadre des systèmes de supervision condi, "
        "j'ai fait un certain nombre de recommandations par rapport à la gestions des accès, à la revue des *audits trails* et aux sauvegardes, mais les services concernés ne les ont pas prises en compte et ne s'en sont pas saisis. On se dit, on verra plus tard."
        "Mais bon, on a un audit trail sur la ligne de condi, c'est déjà ça !"
    },
    {
        "Prenom": "Julien",
        "NomInitiale": "B.",
        "Service": "DSI",
        "Intitule": "Directeur",
        "Verbatim": "Moi et mon équipe nous travaillons avec un parc d'équipements très hétérogène. Je suis frappé par la faible culture numérique."
        "Je n'arrête pas de dire aux gens qui font les appels d'offre qu'il ne faut pas voir leur projet de façon isolée, il faut que les équipements "
        "puissent bien communiquer ensemble pour atteindre une vraie digitalisation."
    },
    {
        "Prenom": "Miranda",
        "NomInitiale": "G.",
        "Service": "Finance",
        "Intitule": "Directrice",
        "Verbatim": "En qualité de directrice du controlling, je suis prête à valider toute forme d'investissement, mais je tiens à ce que l'on me prouve le retour sur investissement."
        "Ce qui apporte de la valeur à l'entreprise sur le compte de résultat, c'est bien le produit et non la donnée. Cela fait cher de dépenser 100k€ pour des activités bureaucratiques."
    },
    {
        "Prenom": "Medhi",
        "NomInitiale": "L.",
        "Service": "Production",
        "Intitule": "Directeur de production",
        "Verbatim": "Mes équipes doivent produire des grosses quantités et avec un turn-over important, cela implique que tout le monde doit être super polyvalent."
        "Je sais que ce n'est pas toujours facile pour les gens de switcher d'une ligne à l'autre en si peu de temps."
    },
    {
        "Prenom": "Sophie",
        "NomInitiale": "R.",
        "Service": "Production",
        "Intitule": "Responsable Conditionnement",
        "Verbatim": "Je recontre régulièrement des opérateurs dans mon bureau pour les resensibiliser suite à des écarts en provenance des équipes de relecture dossier. "
        "Hier, j'ai recadré un opérateur qui n'avait pas compris qu'il ne faut pas écraser de données de proeduction en pharma."
        "... Après, ce n'est pas pour défendre les équipes, mais je ne suis pas sûr que les gens se rendent compte du nombre d'informations que les opérateurs saisissent ou retranscrivent à longueur de journée."
    },
    {
        "Prenom": "Gérald",
        "NomInitiale": "D.",
        "Service": "Production",
        "Intitule": "Responsable Performance Industrielle",
        "Verbatim": "Le problème ici, c'est que les données sont silotées et c'est un enfer pour les retrouver. J'ai plein d'idées pour améliorer la productivité et la qualité produit "
        "mais, entre la production, la qualité et la supply, chacun utilise son propre fichier excel avec ses propres calculs. Et impossible de s'y retrouver entre les versions et les noms de fichiers chaotiques !"
    },
    {
        "Prenom": "Jérome",
        "NomInitiale": "J.",
        "Service": "Production",
        "Intitule": "Opérateur",
        "Verbatim": "C'est beaucoup plus pratique d'avoir un compte partagé, cela évite d'oublier son mot de passe, ce qui m'est déjà arrivé souvent de nuit. "
        "Sur les caméras vision par exemple, les comptes sont nominatifs et cela fait une foule de comptes différents dans le système."
        "... Roger est parti en retraite il y 5 ans et son compte est toujours là ! Tout le monde connaît son mot de passe *'Juventus95'*"
    },
    {
        "Prenom": "Laura",
        "NomInitiale": "S.",
        "Service": "Production",
        "Intitule": "Opératrice Intérimaire",
        "Verbatim": "Cela fait 3 semaines et je suis encore en formation. J'ai eu l'occasion de réaliser quelques réconciliations en fin de lot mais c'est complexe ; "
        "chaque chef de ligne a un peu sa propre méthode de comptage. Les gens sont accueillants, mais la formation est bof. "
    },
]

df = pd.DataFrame(verbatims_struct)

st.markdown("""
En fin d'année 2025, une enquête terrain a été réalisée par un consultant indépendant. Ce dernier a pu échanger avec divers membres de l'organisation et a consolidé les principaux échanges. 
Voici quelques éléments de Verbatim issus de ces interviews.
    """)

full_text = SEPARATOR.join(
    [
        f"{row['Prenom']} {row['NomInitiale']} — {row['Service']} — {row['Intitule']}\n"
        f"“{row['Verbatim']}”"
        for _, row in df.iterrows()
    ]
)
st.text_area("", full_text, height=1200)