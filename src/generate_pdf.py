"""
Générateur PDF — IntegriPharm
Compile l'ensemble du contenu du site (pages + onglets) en un PDF unique.
Stocke le résultat dans assets/IntegriPharm_rapport.pdf
Usage : python src/generate_pdf.py
"""

import sys
import os
import yaml
from pathlib import Path
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    PageBreak, Table, TableStyle, Image as RLImage, KeepTogether,
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# ── Chemins ──────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
OUTPUT = ASSETS / "IntegriPharm_rapport.pdf"

# ── Palette couleurs ──────────────────────────────────────────────────────────
BLEU       = colors.HexColor("#1B3A6B")
BLEU_CLAIR = colors.HexColor("#3D7EAA")
GRIS_FOND  = colors.HexColor("#F4F6F9")
GRIS_BORD  = colors.HexColor("#CCCCCC")
ROUGE      = colors.HexColor("#C0392B")
BLANC      = colors.white

# ── Styles ────────────────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    styles = {
        "cover_title": ParagraphStyle(
            "cover_title", fontSize=32, textColor=BLANC,
            alignment=TA_CENTER, spaceAfter=12, fontName="Helvetica-Bold",
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub", fontSize=14, textColor=BLANC,
            alignment=TA_CENTER, spaceAfter=6, fontName="Helvetica",
        ),
        "page_title": ParagraphStyle(
            "page_title", fontSize=18, textColor=BLANC,
            spaceAfter=8, spaceBefore=4, fontName="Helvetica-Bold",
            backColor=BLEU, leftIndent=-1*cm, rightIndent=-1*cm,
            borderPad=(6, 10, 6, 10),
        ),
        "tab_title": ParagraphStyle(
            "tab_title", fontSize=13, textColor=BLEU,
            spaceAfter=6, spaceBefore=14, fontName="Helvetica-Bold",
            borderPad=(4, 0, 4, 0),
        ),
        "body": ParagraphStyle(
            "body", fontSize=10, textColor=colors.black,
            spaceAfter=5, spaceBefore=2, fontName="Helvetica",
            alignment=TA_JUSTIFY, leading=14,
        ),
        "body_bold": ParagraphStyle(
            "body_bold", fontSize=10, textColor=colors.black,
            spaceAfter=4, fontName="Helvetica-Bold",
        ),
        "bullet": ParagraphStyle(
            "bullet", fontSize=10, textColor=colors.black,
            spaceAfter=3, leftIndent=14, fontName="Helvetica",
            bulletIndent=4, leading=13,
        ),
        "verbatim_name": ParagraphStyle(
            "verbatim_name", fontSize=10, textColor=BLEU,
            spaceAfter=2, fontName="Helvetica-Bold",
        ),
        "verbatim_text": ParagraphStyle(
            "verbatim_text", fontSize=9.5, textColor=colors.HexColor("#333333"),
            spaceAfter=4, fontName="Helvetica-Oblique",
            alignment=TA_JUSTIFY, leading=13, leftIndent=8,
        ),
        "warning_header": ParagraphStyle(
            "warning_header", fontSize=10, textColor=ROUGE,
            spaceAfter=4, fontName="Helvetica-Bold",
        ),
        "glossary_term": ParagraphStyle(
            "glossary_term", fontSize=11, textColor=BLEU,
            spaceAfter=2, spaceBefore=8, fontName="Helvetica-Bold",
        ),
        "glossary_def": ParagraphStyle(
            "glossary_def", fontSize=9.5, textColor=colors.black,
            spaceAfter=4, fontName="Helvetica",
            alignment=TA_JUSTIFY, leading=13, leftIndent=10,
        ),
        "footer": ParagraphStyle(
            "footer", fontSize=8, textColor=colors.grey,
            alignment=TA_CENTER, fontName="Helvetica",
        ),
        "toc_entry": ParagraphStyle(
            "toc_entry", fontSize=11, textColor=BLEU,
            spaceAfter=5, fontName="Helvetica",
        ),
    }
    return styles


# ── En-tête de section ────────────────────────────────────────────────────────
def section_header(title, styles):
    return [
        Spacer(1, 0.3 * cm),
        Table(
            [[Paragraph(title, styles["page_title"])]],
            colWidths=[19 * cm],
            style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), BLEU),
                ("TOPPADDING",    (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LEFTPADDING",   (0, 0), (-1, -1), 12),
                ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
                ("ROUNDEDCORNERS", [4]),
            ]),
        ),
        Spacer(1, 0.3 * cm),
    ]


def tab_header(title, styles):
    return [
        Spacer(1, 0.2 * cm),
        HRFlowable(width="100%", thickness=1.5, color=BLEU_CLAIR, spaceAfter=4),
        Paragraph(title, styles["tab_title"]),
    ]


# ── Page de couverture ────────────────────────────────────────────────────────
def build_cover(styles):
    story = []

    # Rectangle bleu simulé par un tableau pleine page
    date_str = datetime.today().strftime("%d/%m/%Y")
    cover_data = [[
        Paragraph("IntegriPharm", styles["cover_title"]),
    ]]
    cover_table = Table(cover_data, colWidths=[19 * cm])
    cover_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), BLEU),
        ("TOPPADDING",    (0, 0), (-1, -1), 60),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 60),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(Spacer(1, 3 * cm))
    story.append(cover_table)
    story.append(Spacer(1, 0.6 * cm))

    subtitle_data = [[Paragraph(
        "Data & Intégrité des données — Support du Serious Game",
        styles["cover_sub"],
    )]]
    subtitle_table = Table(subtitle_data, colWidths=[19 * cm])
    subtitle_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), BLEU_CLAIR),
        ("TOPPADDING",    (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("LEFTPADDING",   (0, 0), (-1, -1), 20),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 20),
    ]))
    story.append(subtitle_table)
    story.append(Spacer(1, 2 * cm))
    story.append(Paragraph(f"Document généré le {date_str}", styles["footer"]))
    story.append(Spacer(1, 1 * cm))
    story.append(Paragraph(
        "© 2026 Data-Boost / Oravis / Humanim – Tous droits réservés",
        styles["footer"],
    ))

    story.append(PageBreak())
    return story


# ── Sommaire ──────────────────────────────────────────────────────────────────
def build_toc(styles):
    story = []
    story += section_header("📋 Sommaire", styles)
    sections = [
        ("1", "Accueil — Contexte du serious game"),
        ("2", "Profil de l'entreprise"),
        ("3", "Enquête employés — Verbatims"),
        ("4", "Résultat de la dernière inspection FDA"),
        ("5", "Ligne de conditionnement"),
        ("6", "Glossaire — Intégrité des données"),
    ]
    for num, label in sections:
        story.append(Paragraph(f"  {num}.  {label}", styles["toc_entry"]))
    story.append(PageBreak())
    return story


# ── Page 0 : Accueil ──────────────────────────────────────────────────────────
def build_home(styles):
    story = []
    story += section_header("🧬 Accueil — Contexte du serious game", styles)

    story.append(Paragraph("Contexte", styles["tab_title"]))
    story.append(Paragraph(
        "IntegriPharm est un site pharmaceutique stratégique produisant un médicament critique "
        "pour le marché américain. Dans 90 jours, une inspection de la U.S. Food and Drug "
        "Administration est annoncée. Le site a déjà reçu une Warning Letter lors de sa précédente inspection. "
        "Un signalement interne récent mentionne des pratiques douteuses sur la gestion des données.",
        styles["body"],
    ))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph("Si l'inspection échoue, les conséquences seront dramatiques :", styles["body_bold"]))
    for item in [
        "Risque de nouvelle Warning Letter et de mise en demeure",
        "Suspension d'export vers les États-Unis",
        "Impact financier majeur",
        "Perte de crédibilité du site",
    ]:
        story.append(Paragraph(f"• {item}", styles["bullet"]))

    story += tab_header("Votre rôle", styles)
    story.append(Paragraph(
        "Vous êtes un groupe de nouveaux responsables Production et Assurance Qualité. "
        "Votre mission : identifier les dérives possibles et réelles en matière de Data Integrity, "
        "évaluer le niveau de risque, et construire un plan d'action priorisé, réaliste et défendable "
        "face aux inspecteurs.",
        styles["body"],
    ))

    story += tab_header("Déroulé du serious game", styles)
    story.append(Paragraph("Phase 1 – Diagnostic (1 heure)", styles["body_bold"]))
    for item in [
        "Lister les écarts constatés liés aux principes ALCOA+",
        "Détecter les risques critiques sur le procédé de conditionnement",
        "Classer ces écarts par niveau de criticité",
        "Identifier les causes racines (organisationnelles, techniques, culturelles)",
    ]:
        story.append(Paragraph(f"• {item}", styles["bullet"]))

    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph("Phase 2 – Plan d'action (1 heure)", styles["body_bold"]))
    for item in [
        "Budget limité",
        "Nombre limité de ressources internes",
        "Délai de 90 jours",
    ]:
        story.append(Paragraph(f"• {item}", styles["bullet"]))
    story.append(Paragraph(
        "Vous devez prioriser et arbitrer entre les différentes actions possibles.",
        styles["body"],
    ))

    story.append(PageBreak())
    return story


# ── Page 1 : Profil de l'entreprise ──────────────────────────────────────────
def build_profil(styles):
    story = []
    story += section_header("🏭 Profil de l'entreprise", styles)

    # Onglet 1 — Description
    story += tab_header("🗂️ Description synthétique de l'entreprise", styles)
    for item in [
        "Entreprise pharmaceutique créée en 2015.",
        "Dirigeant actuel : Jean-Luc Intègre.",
        "L'entreprise assure la production de son produit phare l'Integrivex, depuis la fabrication jusqu'au packaging.",
        "Le site de production unique de l'entreprise compte actuellement 250 employés. "
        "Pour anticiper les prévisions fortes de croissance, l'entreprise envisage d'embaucher "
        "une cinquantaine d'opérateurs et techniciens de fabrication sur l'année 2026.",
        "La dernière inspection FDA (Pre-Approval Inspection) s'est déroulée en 2022. "
        "Cette dernière a mis en évidence des écarts significatifs en matière d'intégrité des données.",
        "La prochaine inspection FDA est prévue en septembre 2026 et un des objectifs structurants "
        "du site est de réussir cette inspection retour.",
    ]:
        story.append(Paragraph(f"• {item}", styles["bullet"]))

    # Onglet 2 — Objectifs 2026
    story += tab_header("🎯 Objectifs 2026", styles)
    story.append(Paragraph(
        "Améliorer le système qualité afin que l'inspection FDA soit un succès.",
        styles["body_bold"],
    ))
    for item in [
        "Reprendre la main sur l'intégrité des données",
        "Sécuriser l'usage des systèmes",
        "Standardiser les pratiques",
    ]:
        story.append(Paragraph(f"• {item}", styles["bullet"]))

    # Onglet 3 — Organigramme (image)
    story += tab_header("👥 Organigramme de l'équipe IntegriPharm", styles)
    org_path = ASSETS / "Organigramme Integripharm.png"
    if org_path.exists():
        story.append(RLImage(str(org_path), width=16 * cm, height=10 * cm, kind="proportional"))
    else:
        story.append(Paragraph("(Image organigramme non disponible)", styles["body"]))

    story.append(PageBreak())
    return story


# ── Page 2 : Enquête employés ─────────────────────────────────────────────────
def build_enquete(styles):
    story = []
    story += section_header("🗣️ Enquête employés — Verbatims", styles)

    story.append(Paragraph(
        "En fin d'année 2025, une enquête terrain a été réalisée par un consultant indépendant. "
        "Ce dernier a pu échanger avec divers membres de l'organisation et a consolidé les principaux échanges.",
        styles["body"],
    ))
    story.append(Spacer(1, 0.3 * cm))

    verbatims = [
        ("Jean-Luc Intègre", "", "IntegriPharm", "CEO",
         "L'inspection de la FDA est un moment clé pour notre entreprise : elle conditionne notre crédibilité sur le marché américain"
         "… Une fois cette inspection passée avec succès, nous pourrons nous recentrer sur nos priorités business et opérationnelles ; "
         "l'objectif est avant tout de réussir ce rendez-vous précis."),
        ("Camille", "D.", "Assurance Qualité", "Directrice Qualité",
         "La situation est sensible car nous avons encore énormément de travail avant l'inspection. "
         "L'inspection readiness est définitivement un enjeu qu'il faudra que je travaille. "
         "Le management tolère certains écarts au nom des contraintes opérationnelles, ce qui fragilise notre culture qualité. "
         "Il faut que le Top management se mouille davantage et m'aide sur ces sujets."),
        ("Eric", "Z.", "Assurance Qualité", "Responsable Qualité Opérationnelle",
         "Je ne suis pas sûr ici que les gens comprennent bien que la qualité et la Data Integrity c'est l'affaire de tous. "
         "Très souvent, les gens se reposent sur nous et imaginent que dès qu'il y a un sujet déviation ou Data Integrity c'est forcément l'affaire de la qualité. "
         "Il y a un autre problème ; quand je compare avec mon ancienne entreprise, je trouve que, ici, la Data Integrity n'est pas assez représentée "
         "dans les analyses de risques, la démarche de Change Control et les dashboards de reporting."),
        ("Nina", "K.", "Assurance Qualité", "Qualification/Validation Expert",
         "J'ai un vrai problème de bande passante ! Tous les projets sont urgents et on doit tout gérer de front. "
         "Le choix des fournisseurs se fait à la va-vite et on en paye parfois les pots cassés. "
         "Après, quand il y a un écart, tout le monde se renvoie la balle et on avance pas. "
         "Je constate qu'on a aussi beaucoup mal à passer du mode projet au mode routine. "
         "J'ai fait un certain nombre de recommandations par rapport à la gestion des accès, à la revue des audits trails "
         "et aux sauvegardes, mais les services concernés ne les ont pas prises en compte. "
         "Mais bon, on a un audit trail sur la ligne de condi, c'est déjà ça !"),
        ("Julien", "B.", "DSI", "Directeur",
         "Moi et mon équipe nous travaillons avec un parc d'équipements très hétérogène. Je suis frappé par la faible culture numérique. "
         "Je n'arrête pas de dire aux gens qui font les appels d'offre qu'il ne faut pas voir leur projet de façon isolée, "
         "il faut que les équipements puissent bien communiquer ensemble pour atteindre une vraie digitalisation."),
        ("Miranda", "G.", "Finance", "Directrice",
         "En qualité de directrice du controlling, je suis prête à valider toute forme d'investissement, "
         "mais je tiens à ce que l'on me prouve le retour sur investissement. "
         "Ce qui apporte de la valeur à l'entreprise sur le compte de résultat, c'est bien le produit et non la donnée. "
         "Cela fait cher de dépenser 100k€ pour des activités bureaucratiques."),
        ("Medhi", "L.", "Production", "Directeur de production",
         "Mes équipes doivent produire des grosses quantités et avec un turn-over important, "
         "cela implique que tout le monde doit être super polyvalent. "
         "Je sais que ce n'est pas toujours facile pour les gens de switcher d'une ligne à l'autre en si peu de temps."),
        ("Sophie", "R.", "Production", "Responsable Conditionnement",
         "Je rencontre régulièrement des opérateurs dans mon bureau pour les resensibiliser suite à des écarts en provenance des équipes de relecture dossier. "
         "Hier, j'ai recadré un opérateur qui n'avait pas compris qu'il ne faut pas écraser de données de production en pharma. "
         "Je ne suis pas sûr que les gens se rendent compte du nombre d'informations que les opérateurs saisissent ou retranscrivent à longueur de journée."),
        ("Gérald", "D.", "Production", "Responsable Performance Industrielle",
         "Le problème ici, c'est que les données sont silotées et c'est un enfer pour les retrouver. "
         "J'ai plein d'idées pour améliorer la productivité et la qualité produit mais, entre la production, la qualité et la supply, "
         "chacun utilise son propre fichier excel avec ses propres calculs. "
         "Et impossible de s'y retrouver entre les versions et les noms de fichiers chaotiques !"),
        ("Jérome", "J.", "Production", "Opérateur",
         "C'est beaucoup plus pratique d'avoir un compte partagé, cela évite d'oublier son mot de passe, ce qui m'est déjà arrivé souvent de nuit. "
         "Sur les caméras vision par exemple, les comptes sont nominatifs et cela fait une foule de comptes différents dans le système. "
         "Roger est parti en retraite il y a 5 ans et son compte est toujours là ! Tout le monde connaît son mot de passe 'Juventus95'"),
        ("Laura", "S.", "Production", "Opératrice Intérimaire",
         "Cela fait 3 semaines et je suis encore en formation. J'ai eu l'occasion de réaliser quelques réconciliations en fin de lot mais c'est complexe ; "
         "chaque chef de ligne a un peu sa propre méthode de comptage. Les gens sont accueillants, mais la formation est bof."),
    ]

    for prenom, initiale, service, intitule, verbatim in verbatims:
        nom_complet = f"{prenom} {initiale}".strip()
        block = KeepTogether([
            Paragraph(f"{nom_complet} — {service} — {intitule}", styles["verbatim_name"]),
            Paragraph(f"« {verbatim} »", styles["verbatim_text"]),
            HRFlowable(width="100%", thickness=0.5, color=GRIS_BORD, spaceAfter=4),
        ])
        story.append(block)

    story.append(PageBreak())
    return story


# ── Page 3 : Warning Letter FDA ───────────────────────────────────────────────
def build_warning_letter(styles):
    story = []
    story += section_header("🧾 Résultat de la dernière inspection FDA", styles)

    story.append(Paragraph(
        "Voici le contenu de la warning letter publique adressée au CEO d'Integripharm en 2022.",
        styles["body"],
    ))
    story.append(Spacer(1, 0.3 * cm))

    story.append(Paragraph("Cher Mr. Jean-Luc Intègre,", styles["body"]))
    story.append(Paragraph(
        "The U.S. Food and Drug Administration (FDA) inspected your drug manufacturing facility, "
        "Integripharm, and identified significant violations of Current Good Manufacturing Practice (CGMP) "
        "regulations (21 CFR parts 210 and 211). Because your methods and controls do not conform to CGMP, "
        "your drug products are adulterated within the meaning of section 501(a)(2)(B) of the FD&amp;C Act.",
        styles["body"],
    ))
    story.append(Spacer(1, 0.2 * cm))

    deficiencies = [
        (
            "1. Uncontrolled Weighing Documentation — 21 CFR § 211.188(b)(11) and 21 CFR § 211.194(a)",
            "Uncontrolled and non-conform weighing ticket was found inside a trash bin without explanation. "
            "A non-compliant weighing ticket was discovered in the equipment, and personnel were unable to "
            "provide traceability, investigation records, or justification for its presence.",
        ),
        (
            "2. System Time Manipulation — 21 CFR § 211.68(b) and 21 CFR § 11.10(a)",
            "The production control software allowed manual modification of system time. "
            "Our investigator was able to change the system clock without restriction, compromising the "
            "reliability and chronological integrity of electronic records and audit trails. "
            "This modification does not appear in the system's audit trail, reflecting a lack of validation "
            "of the concerned computerized system.",
        ),
        (
            "3. Pre-Signed Production Documentation — 21 CFR § 211.100(b)",
            "Production start-up documentation was pre-signed prior to execution of operations. "
            "An operator had signed the start-up control form before the related manufacturing steps were "
            "performed, calling into question the contemporaneous and attributable nature of the records.",
        ),
        (
            "4. Shared Generic User Accounts — 21 CFR § 11.100(a) and 21 CFR § 11.10(g)",
            "Shared generic user accounts were used within the supervisory module. "
            "The use of team-based accounts (Equipe A/B/C) by multiple operators prevented individual "
            "attribution of actions and undermined data integrity and accountability.",
        ),
    ]

    for title, text in deficiencies:
        story.append(KeepTogether([
            Paragraph(title, styles["warning_header"]),
            Paragraph(text, styles["body"]),
            Spacer(1, 0.1 * cm),
        ]))

    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        "En réponse à cette Warning Letter, un plan d'action a été communiqué à la FDA. "
        "Ce dernier se concentrait spécifiquement sur la resensibilisation des opérateurs concernés "
        "par les différents écarts observés en inspection.",
        styles["body"],
    ))

    story.append(PageBreak())
    return story


# ── Page 4 : Ligne de conditionnement ────────────────────────────────────────
def build_conditionnement(styles):
    story = []
    story += section_header("💊 Ligne de conditionnement", styles)

    # Onglet 1 — Vidéo (non reproductible en PDF)
    story += tab_header("🎥 Vidéo de la ligne", styles)
    story.append(Paragraph(
        "Une illustration vidéo du type de ligne de conditionnement utilisée pour packager l'Integrivex "
        "est disponible sur le site internet (onglet Vidéo de la ligne).",
        styles["body"],
    ))
    story.append(Paragraph(
        "Vidéo publique utilisée à des fins éducatives (Jornen Machinery) — www.jornen.com",
        ParagraphStyle("italic_small", parent=styles["body"], fontSize=8, textColor=colors.grey),
    ))

    # Onglet 2 — Diagramme fonctionnel
    story += tab_header("🔀 Diagramme fonctionnel", styles)
    story.append(Paragraph(
        "Ce schéma représente de façon simplifiée les différentes étapes du procédé de conditionnement :",
        styles["body"],
    ))
    for item in [
        "Packaging primaire : emballage en contact direct avec le produit, qui le contient et le protège jusqu'à son utilisation.",
        "Packaging secondaire : emballage facilitant la présentation, l'information et la protection supplémentaire.",
        "Packaging tertiaire : emballage destiné au transport et au stockage en volume.",
    ]:
        story.append(Paragraph(f"• {item}", styles["bullet"]))

    diag_path = ASSETS / "Diagramme Condi.png"
    if diag_path.exists():
        story.append(Spacer(1, 0.3 * cm))
        story.append(RLImage(str(diag_path), width=16 * cm, height=10 * cm, kind="proportional"))
    story.append(Paragraph(
        "Les flux d'information sont nombreux et représentés de façon simplifiée. "
        "L'analyse de la SOP de conditionnement et du dossier de lot permettront de comprendre "
        "finement les mouvements de données.",
        styles["body"],
    ))

    # Onglets 3 & 4 — Work in Progress
    story += tab_header("📋 SOP de conditionnement", styles)
    story.append(Paragraph("🚧 Work in Progress — contenu à venir.", styles["body"]))

    story += tab_header("🧾 Dossier de lot", styles)
    story.append(Paragraph("🚧 Work in Progress — contenu à venir.", styles["body"]))

    story.append(PageBreak())
    return story


# ── Page 5 : Glossaire ────────────────────────────────────────────────────────
def build_glossaire(styles):
    story = []
    story += section_header("📖 Glossaire — Intégrité des données", styles)

    story.append(Paragraph(
        "Retrouvez ici les définitions des termes clés liés à l'intégrité des données "
        "dans l'industrie pharmaceutique.",
        styles["body"],
    ))
    story.append(Spacer(1, 0.3 * cm))

    yaml_path = ASSETS / "glossaire_data_integrity.yaml"
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    current_letter = None
    for item in data["glossaire"]:
        lettre = item["terme"][0].upper()
        if lettre != current_letter:
            current_letter = lettre
            story.append(Spacer(1, 0.2 * cm))
            story.append(HRFlowable(width="100%", thickness=1, color=BLEU_CLAIR))
            story.append(Paragraph(lettre, ParagraphStyle(
                "letter_sep", fontSize=13, textColor=BLEU_CLAIR,
                fontName="Helvetica-Bold", spaceBefore=4, spaceAfter=2,
            )))

        story.append(KeepTogether([
            Paragraph(f"🏷  {item['terme']}", styles["glossary_term"]),
            Paragraph(item["definition"].strip(), styles["glossary_def"]),
        ]))

    return story


# ── Page finale : Mentions légales & Copyrights ───────────────────────────────
def build_legal_page(styles):
    story = []
    story.append(PageBreak())
    story += section_header("⚖️ Mentions légales & Droits d'auteur", styles)

    # Bloc développeurs
    story += tab_header("Équipe de création", styles)
    devs = [
        ("Application développée par",  "Arnaud Duigou",     "Data-Boost"),
        ("En partenariat avec",         "Cédric Maunourri",  "Oravis"),
        ("",                            "Christophe Meunier","Humanim"),
    ]
    table_data = []
    for role, nom, struct in devs:
        table_data.append([
            Paragraph(role,  ParagraphStyle("td_role",  fontSize=9,  textColor=colors.grey,  fontName="Helvetica")),
            Paragraph(nom,   ParagraphStyle("td_nom",   fontSize=10, textColor=BLEU,         fontName="Helvetica-Bold")),
            Paragraph(struct,ParagraphStyle("td_struct",fontSize=10, textColor=colors.black, fontName="Helvetica")),
        ])
    t = Table(table_data, colWidths=[5*cm, 6*cm, 6*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), GRIS_FOND),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("LINEBELOW",     (0, 0), (-1, -2), 0.5, GRIS_BORD),
        ("ROUNDEDCORNERS",[4]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.6 * cm))

    # Bloc copyright
    story += tab_header("Copyright", styles)
    story.append(Paragraph(
        f"© 2026 Data-Boost / Oravis / Humanim – Tous droits réservés.",
        styles["body_bold"],
    ))
    story.append(Paragraph(
        "Cette application et l'ensemble de ses contenus (textes, données, visuels, structure pédagogique) "
        "constituent une œuvre protégée par le droit d'auteur au sens des articles L.111-1 et suivants "
        "du Code de la propriété intellectuelle.",
        styles["body"],
    ))
    story.append(Spacer(1, 0.2 * cm))

    # Bloc propriété
    story += tab_header("Propriété & Restrictions d'usage", styles)
    story.append(Paragraph(
        "Cette œuvre est la propriété exclusive de ses auteurs et partenaires. "
        "Toute reproduction, distribution, modification ou réutilisation, totale ou partielle, "
        "du code, du contenu ou des supports associés, sans autorisation écrite préalable, "
        "est strictement interdite.",
        styles["body"],
    ))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "Ce document est mis à disposition à des fins exclusivement pédagogiques dans le cadre "
        "du serious game IntegriPharm. Toute utilisation commerciale ou diffusion publique "
        "sans accord préalable des ayants droit est prohibée.",
        styles["body"],
    ))
    story.append(Spacer(1, 0.4 * cm))

    # Bloc contact
    story += tab_header("Contact", styles)
    for line in [
        "Data-Boost — Arnaud Duigou",
        "Oravis — Cédric Maunourri",
        "Humanim — Christophe Meunier",
    ]:
        story.append(Paragraph(f"• {line}", styles["bullet"]))

    story.append(Spacer(1, 1 * cm))
    story.append(HRFlowable(width="100%", thickness=1, color=BLEU))
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(
        f"Document généré le {datetime.today().strftime('%d/%m/%Y')} — IntegriPharm Data & IA Dashboard",
        ParagraphStyle("center_grey", fontSize=8, textColor=colors.grey,
                       alignment=TA_CENTER, fontName="Helvetica"),
    ))
    return story


# ── En-tête / pied de page ────────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    w, h = A4

    # En-tête
    canvas.setFillColor(BLEU)
    canvas.rect(0, h - 1.2 * cm, w, 1.2 * cm, fill=1, stroke=0)
    canvas.setFillColor(BLANC)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(1.5 * cm, h - 0.8 * cm, "IntegriPharm — Data & Intégrité des données")

    # Pied de page
    canvas.setFillColor(GRIS_FOND)
    canvas.rect(0, 0, w, 1 * cm, fill=1, stroke=0)
    canvas.setFillColor(colors.grey)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(1.5 * cm, 0.35 * cm,
                      f"© 2026 Data-Boost / Oravis / Humanim – Document généré le "
                      f"{datetime.today().strftime('%d/%m/%Y')}")
    canvas.drawRightString(w - 1.5 * cm, 0.35 * cm, f"Page {doc.page}")
    canvas.restoreState()


# ── Assemblage ────────────────────────────────────────────────────────────────
def generate():
    print(f"Génération du PDF : {OUTPUT}")

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.5 * cm,
        title="IntegriPharm — Rapport complet",
        author="Data-Boost / Oravis / Humanim",
    )

    styles = build_styles()
    story = []

    story += build_cover(styles)
    story += build_toc(styles)
    story += build_home(styles)
    story += build_profil(styles)
    story += build_enquete(styles)
    story += build_warning_letter(styles)
    story += build_conditionnement(styles)
    story += build_glossaire(styles)
    story += build_legal_page(styles)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF généré avec succès : {OUTPUT}")
    return str(OUTPUT)


if __name__ == "__main__":
    generate()
