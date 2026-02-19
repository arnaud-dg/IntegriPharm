import streamlit as st
import pandas as pd
from pathlib import Path
from pygwalker.api.streamlit import StreamlitRenderer
from utils import sidebar_logo

# --- Page config (UNE SEULE FOIS) ---
st.set_page_config(
    page_title="Dataset — IntegriPharm",
    page_icon="📚",
    layout="wide",
)

sidebar_logo("assets/logo_ebi_a3p.png", logo_height=250, reserve_space=0, margin_top=10)

st.title("📚 Bases de données de l'entreprise IntegriPharm")

# --- Paths ---
DATA_DIR = Path("data")
IMG_PATH = DATA_DIR / "ChatGPT Image 20 janv. 2026, 11_36_17.png"
TRS_CSV_PATH = DATA_DIR / "trs_mock.csv"
LOGBOOK_CSV_PATH = DATA_DIR / "logbook.csv"

# ---------- UI ----------
tab1, tab2, tab3, tab4 = st.tabs(
    ["📓 Scans Log book", "🎙️ Saisie Log book", "📈 Données TRS", "🧪 Données Analytiques LIMS"]
)

# -----------------
# TAB 1 : Scan image
# -----------------
with tab1:
    st.subheader("📓 Scans Log book")

    if IMG_PATH.exists():
        st.image(str(IMG_PATH), caption=IMG_PATH.name, use_container_width=True)
    else:
        st.error(f"Image introuvable : {IMG_PATH}")

# -----------------
# TAB 2 : Logbook CSV
# -----------------
with tab2:
    st.subheader("🎙️ Saisie Log book")

    if LOGBOOK_CSV_PATH.exists():
        df_logbook = pd.read_csv(LOGBOOK_CSV_PATH)
        st.dataframe(df_logbook, use_container_width=True)
        st.caption(f"{len(df_logbook)} lignes • {len(df_logbook.columns)} colonnes")
    else:
        st.error(f"Fichier introuvable : {LOGBOOK_CSV_PATH}")

# -----------------
# TAB 3 : TRS + PyGWalker
# -----------------
with tab3:
    st.subheader("📈 Données TRS")

    if TRS_CSV_PATH.exists():
        df_trs = pd.read_csv(TRS_CSV_PATH)

        with st.expander("Aperçu des données", expanded=True):
            st.dataframe(df_trs, use_container_width=True)
            st.caption(f"{len(df_trs)} lignes • {len(df_trs.columns)} colonnes")

        st.divider()
        st.markdown("### Exploration interactive (PyGWalker)")

        # ✅ API PyGWalker embedded dans Streamlit
        renderer = StreamlitRenderer(df_trs, spec="./gw_config.json", spec_io_mode="rw")
        renderer.explorer()
    else:
        st.error(f"Fichier TRS introuvable : {TRS_CSV_PATH}")

# -----------------
# TAB 4 : placeholder LIMS
# -----------------
with tab4:
    st.subheader("🧪 Données Analytiques LIMS")
    st.info("À connecter : export LIMS (CSV/SQL/API) + schéma (sample_id, test, result, unit, spec, OOS, etc.).")
