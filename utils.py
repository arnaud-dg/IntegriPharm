import streamlit as st
import base64
from pathlib import Path
import textwrap

def sidebar_logo(path: str, logo_height: int = 120, reserve_space: int = 90, margin_top: int = 10):
    b64 = base64.b64encode(Path(path).read_bytes()).decode()

    css = f"""
    <style>
      /* Réserve juste ce qu’il faut (pas forcément = logo_height) */
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