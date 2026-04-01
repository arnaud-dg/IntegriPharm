import streamlit as st
import base64
from pathlib import Path
import textwrap

def sidebar_logo(path: str, logo_height: int = 120, reserve_space: int = 90, margin_top: int = 10):
    b64 = base64.b64encode(Path(path).read_bytes()).decode()

    css = f"""
    <style>
      /* Réserve juste ce qu'il faut (pas forcément = logo_height) */
      section[data-testid="stSidebar"] > div:first-child {{
        padding-top: {reserve_space}px;
      }}

      /* Logo affiché en "overlay" */
      section[data-testid="stSidebar"]::before {{
        content: "";
        display: block;
        height: {logo_height}px;
        margin: {margin_top}px 10px 0 10px;
        background-image: url("data:image/png;base64,{b64}");
        background-repeat: no-repeat;
        background-size: contain;
        background-position: center;
      }}
    </style>
    """
    st.sidebar.markdown(textwrap.dedent(css), unsafe_allow_html=True)

    # Logos partenaires en bas de sidebar avec tooltip mentions légales au survol
    logos_b64 = base64.b64encode(Path("assets/Logos.png").read_bytes()).decode()

    legal_html = f"""
    <style>
      .legal-wrap {{
        position: fixed;
        bottom: 18px;
        left: 0;
        width: 240px;
        padding: 0 14px;
        z-index: 9999;
      }}
      .legal-wrap img {{
        width: 100%;
        display: block;
        cursor: default;
      }}
      .legal-tooltip {{
        display: none;
        position: absolute;
        bottom: calc(100% + 8px);
        left: 0;
        width: 280px;
        background: #ffffff;
        border: 1px solid #d0d0d0;
        border-radius: 10px;
        padding: 14px 16px;
        font-size: 12px;
        line-height: 1.6;
        color: #333;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        white-space: normal;
      }}
      .legal-wrap:hover .legal-tooltip {{
        display: block;
      }}
    </style>
    <div class="legal-wrap">
      <div class="legal-tooltip">
        <strong>Application développée par</strong><br>
        Arnaud Duigou — Data-Boost<br><br>
        <strong>En partenariat avec</strong><br>
        Cédric Maunourri — Oravis<br>
        Christophe Meunier — Humanim<br>
        <hr style="margin:8px 0; border-color:#eee;">
        © 2026 Data-Boost / Oravis / Humanim – All rights reserved.<br><br>
        Cette application constitue une œuvre protégée par le droit d'auteur.
        Elle est la propriété exclusive de ses auteurs et partenaires.<br><br>
        Toute reproduction, distribution, modification ou réutilisation,
        totale ou partielle, du code, du contenu ou des supports associés,
        sans autorisation écrite préalable, est strictement interdite.
      </div>
      <img src="data:image/png;base64,{logos_b64}" alt="Logos partenaires">
    </div>
    """
    st.sidebar.markdown(legal_html, unsafe_allow_html=True)


def pdf_download_button():
    """Propose le téléchargement du PDF complet (à placer dans la page principale)."""
    root = Path(__file__).resolve().parent
    pdf_path = root / "assets" / "IntegriPharm_rapport.pdf"

    if pdf_path.exists():
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Télécharger le contenu",
                data=f.read(),
                file_name="IntegriPharm_rapport.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
