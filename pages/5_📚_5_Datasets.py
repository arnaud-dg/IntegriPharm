import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Dataset — IntegriPharm", page_icon="📚", layout="wide")

st.title("📚 Dataset (mock) — Consultation par onglets")
st.caption("Données d’exemple : remplace par tes sources (CSV/SQL/API).")

# ---------- Helpers (mock data) ----------
def mock_logbook(n=40):
    base = datetime(2025, 12, 1, 8, 0, 0)
    rows = []
    for i in range(n):
        ts = base + timedelta(hours=i * 6)
        rows.append({
            "timestamp": ts.isoformat(sep=" ", timespec="minutes"),
            "atelier": random.choice(["Fermentation", "Purification"]),
            "equipement": random.choice(["R-101", "R-102", "C-201", "SKID-3"]),
            "type_evenement": random.choice(["Info", "Déviation", "Maintenance", "Nettoyage"]),
            "commentaire": random.choice([
                "RAS",
                "Écart mineur, suivi en cours",
                "Arrêt court pour vérification capteur",
                "Changement filtre, test OK",
            ]),
            "auteur": random.choice(["Camille D.", "Mehdi L.", "Sophie R.", "Nina K."]),
        })
    return pd.DataFrame(rows)

def mock_retranscriptions(n=15):
    base = datetime(2025, 12, 5, 9, 0, 0)
    rows = []
    for i in range(n):
        ts = base + timedelta(days=i)
        rows.append({
            "date": ts.date().isoformat(),
            "source": random.choice(["Daily meeting", "Shift handover", "Investigation interview"]),
            "speaker": random.choice(["Camille D.", "Eric M.", "Julien P.", "Laura S."]),
            "texte": random.choice([
                "On a eu un souci d’accès aux données ce matin, j’ai attendu l’export.",
                "Les chiffres TRS divergent encore, on doit verrouiller une formule unique.",
                "On a besoin d’une règle claire de nommage, sinon on perd le fil.",
                "Le système ne parle pas au LIMS, on fait des contournements.",
            ]),
        })
    return pd.DataFrame(rows)

def mock_trs(n=60):
    base = datetime(2025, 10, 1)
    rows = []
    for i in range(n):
        d = base + timedelta(days=i)
        planned = random.randint(18, 24)
        run = max(0, planned - random.randint(0, 6))
        perf = random.uniform(0.75, 0.98)
        qual = random.uniform(0.90, 0.995)
        availability = run / planned if planned else 0
        oee = availability * perf * qual
        rows.append({
            "date": d.date().isoformat(),
            "atelier": random.choice(["Fermentation", "Purification"]),
            "planned_hours": planned,
            "run_hours": run,
            "availability": round(availability, 3),
            "performance": round(perf, 3),
            "quality": round(qual, 3),
            "TRS_OEE": round(oee, 3),
        })
    return pd.DataFrame(rows)

def mock_lims(n=35):
    base = datetime(2025, 11, 10, 10, 0, 0)
    rows = []
    for i in range(n):
        ts = base + timedelta(hours=i * 10)
        rows.append({
            "sample_id": f"SMP-{10000+i}",
            "timestamp": ts.isoformat(sep=" ", timespec="minutes"),
            "test": random.choice(["Bioburden", "Endotoxins", "Assay", "pH", "Conductivity"]),
            "result": round(random.uniform(0.1, 120.0), 3),
            "unit": random.choice(["CFU/mL", "EU/mL", "%", "", "mS/cm"]),
            "status": random.choice(["PASS", "PASS", "PASS", "OOS"]),
            "batch": random.choice(["B25-1101", "B25-1102", "B25-1201"]),
        })
    return pd.DataFrame(rows)

# ---------- UI ----------
tab1, tab2, tab3, tab4 = st.tabs(["📓 Log book", "🎙️ Retranscription", "📈 TRS", "🧪 LIMS"])

with tab1:
    st.subheader("📓 Log book (mock)")
    df = mock_logbook()
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.download_button("Télécharger CSV", df.to_csv(index=False).encode("utf-8"), "logbook.csv", "text/csv")

with tab2:
    st.subheader("🎙️ Retranscription (mock)")
    df = mock_retranscriptions()
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.download_button("Télécharger CSV", df.to_csv(index=False).encode("utf-8"), "retranscription.csv", "text/csv")

with tab3:
    st.subheader("📈 TRS / OEE (mock)")
    df = mock_trs()
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.caption("Astuce : branche ici tes règles de calcul officielles (data dictionary) pour éviter les divergences.")
    st.download_button("Télécharger CSV", df.to_csv(index=False).encode("utf-8"), "trs.csv", "text/csv")

with tab4:
    st.subheader("🧪 LIMS (mock)")
    df = mock_lims()
    st.dataframe(df, use_container_width=True, hide_index=True)

    only_oos = st.checkbox("Afficher uniquement OOS", value=False)
    if only_oos:
        st.dataframe(df[df["status"] == "OOS"], use_container_width=True, hide_index=True)

    st.download_button("Télécharger CSV", df.to_csv(index=False).encode("utf-8"), "lims.csv", "text/csv")

st.divider()
st.info(
    "Prochaine étape logique : remplacer les mocks par tes sources réelles (CSV/SQL/S3/API) "
    "et ajouter un ‘data contract’ (schéma, contrôles, règles de calcul, ownership)."
)
