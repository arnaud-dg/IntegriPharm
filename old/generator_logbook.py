from __future__ import annotations

import os
import random
from datetime import datetime, timedelta
from typing import Optional, Dict, List

import pandas as pd


EQUIPEMENTS = ["R-101", "R-102", "C-201"]
STATUTS = ["Production", "Arrêt", "Nettoyage"]
VISAS = ["EBO", "GTE", "JDE", "ISA", "OPI", "BAI", "CSI", "MME", "PZW", "TFR"]

COMMENTS_BY_STATUS: Dict[str, List[str]] = {
    "Production": [
        "Début de production",
        "Production en cours",
        "Contrôle en cours : paramètres conformes",
        "Prélèvement IPC réalisé",
        "Ajustement mineur du débit",
        "Fin de production",
    ],
    "Arrêt": [
        "Arrêt programmé",
        "Arrêt suite à fin de lot",
        "Arrêt pour investigation",
        "Arrêt suite à alarme",
        "Attente autorisation de redémarrage",
    ],
    "Nettoyage": [
        "Début de nettoyage",
        "Nettoyage en cours",
        "Rinçage final réalisé",
        "Contrôle visuel en cours",
        "Fin de nettoyage",
    ],
}


def _choose_comment(status: str, phase: str) -> str:
    """
    phase: "start" | "middle" | "end"
    """
    if status == "Production":
        if phase == "start":
            return "Début de production"
        if phase == "end":
            return "Fin de production"
    if status == "Nettoyage":
        if phase == "start":
            return "Début de nettoyage"
        if phase == "end":
            return "Fin de nettoyage"

    pool = COMMENTS_BY_STATUS.get(status, ["RAS"])
    if phase == "middle":
        pool = [c for c in pool if not c.lower().startswith(("début", "fin"))] or pool
    return random.choice(pool)


def generate_logbook_csv(
    n_rows: int,
    output_csv_path: str = "data/logbook.csv",
    start_datetime: Optional[datetime] = None,
    seed: Optional[int] = 42,
    min_step_minutes: int = 5,
    max_step_minutes: int = 90,
    batch_prefix: str = "B",
    batch_start_number: int = 200,
) -> pd.DataFrame:
    """
    Génère un logbook chronologique et l'enregistre en CSV dans `output_csv_path`.

    Ajoute une colonne Batch:
      - Démarre à "B200" (par défaut)
      - S'incrémente à chaque *démarrage de production* (entrée en Production)
      - Un lot est lié à un seul équipement (un batch ne "migre" jamais)
      - Durant une séquence Production, l'équipement reste fixe et le batch reste le même
      - Hors Production, Batch est vide (chaîne vide)

    Retourne aussi le DataFrame.
    """
    if n_rows <= 0:
        raise ValueError("n_rows doit être > 0")

    if seed is not None:
        random.seed(seed)

    if start_datetime is None:
        now = datetime.now()
        start_datetime = now.replace(hour=7, minute=0, second=0, microsecond=0)

    os.makedirs(os.path.dirname(output_csv_path) or ".", exist_ok=True)

    current_dt = start_datetime

    # Etat "run" (séquence) courant
    current_status = random.choice(STATUTS)
    current_equipment = random.choice(EQUIPEMENTS)

    # Gestion batch
    batch_counter = batch_start_number
    current_batch: Optional[str] = None
    current_batch_equipment: Optional[str] = None

    # Runs plus réalistes : on garde (status + equip) sur plusieurs lignes
    remaining_in_run = random.randint(3, 10)

    rows = []

    for _ in range(n_rows):
        # Horodatage strictement croissant
        current_dt += timedelta(minutes=random.randint(min_step_minutes, max_step_minutes))

        # Démarre un nouveau run si besoin
        if remaining_in_run <= 0:
            # Transition plausible de statut
            if current_status == "Production":
                next_status = random.choices(["Arrêt", "Nettoyage", "Production"], weights=[4, 3, 1])[0]
            elif current_status == "Nettoyage":
                next_status = random.choices(["Arrêt", "Production", "Nettoyage"], weights=[4, 3, 1])[0]
            else:  # Arrêt
                next_status = random.choices(["Production", "Nettoyage", "Arrêt"], weights=[4, 2, 1])[0]

            current_status = next_status

            # Règle clé : pendant une production, l'équipement ne change pas.
            # On choisit un équipement au début d'un run, et on le garde pour tout le run.
            # Pour les runs non-production, on peut changer d'équipement librement.
            if current_status == "Production":
                # Choix d'équipement au démarrage du run de Production
                current_equipment = random.choice(EQUIPEMENTS)
            else:
                # Non-production : on peut changer ou non (un peu de stabilité)
                if random.random() < 0.5:
                    current_equipment = random.choice(EQUIPEMENTS)

            remaining_in_run = random.randint(3, 10)

        # Détection entrée en production (pour incrément batch)
        # Condition : status Production et aucun batch actif (ou batch pas cohérent)
        entering_production = current_status == "Production" and (
            current_batch is None or current_batch_equipment != current_equipment
        )

        if entering_production:
            current_batch = f"{batch_prefix}{batch_counter}"
            current_batch_equipment = current_equipment
            batch_counter += 1

        # Si on n'est pas en production, batch vide (et on "ferme" le batch actif)
        if current_status != "Production":
            current_batch = None
            current_batch_equipment = None

        # Phase dans le run (start/middle/end)
        # Ici, remaining_in_run correspond aux lignes restantes dans ce run (incluant celle-ci)
        if remaining_in_run == max(remaining_in_run, 1):  # start heuristique
            phase = "start" if remaining_in_run in (3, 4, 5, 6, 7, 8, 9, 10) else "middle"
        if remaining_in_run == 1:
            phase = "end"
        elif remaining_in_run not in (1,):
            # Si c'est la 1ère ligne du run, on la marque start.
            # On approxime en utilisant un flag simple : start quand on vient de recharger remaining_in_run.
            # Comme on ne le stocke pas, on force start si entering_production (et sinon middle).
            phase = "start" if entering_production else "middle"

        comment = _choose_comment(current_status, phase)

        rows.append(
            {
                "Date": current_dt.date().isoformat(),
                "Heure": current_dt.time().strftime("%H:%M:%S"),
                "Equipement": current_equipment,
                "Statut": current_status,
                "Batch": current_batch or "",
                "Commentaires": comment,
                "Visa": random.choice(VISAS),
            }
        )

        remaining_in_run -= 1

    df = pd.DataFrame(
        rows, columns=["Date", "Heure", "Equipement", "Statut", "Batch", "Commentaires", "Visa"]
    )

    # Sécurité : tri chronologique (normalement déjà OK)
    df["_dt"] = pd.to_datetime(df["Date"] + " " + df["Heure"])
    df = df.sort_values("_dt").drop(columns=["_dt"]).reset_index(drop=True)

    # Vérification simple : un batch ne doit apparaître que sur un seul équipement
    # (si jamais tu modifies la logique plus tard, ça te protège)
    batch_to_equips = df[df["Batch"] != ""].groupby("Batch")["Equipement"].nunique()
    if (batch_to_equips > 1).any():
        bad = batch_to_equips[batch_to_equips > 1].index.tolist()
        raise RuntimeError(f"Règle violée : batch(s) présent(s) sur plusieurs équipements : {bad}")

    df.to_csv(output_csv_path, index=False, encoding="utf-8")
    return df


if __name__ == "__main__":
    # Exemple : génère 200 lignes dans data/logbook.csv
    generate_logbook_csv(n_rows=200, output_csv_path="data/logbook.csv", seed=123)
    print("CSV généré : data/logbook.csv")
