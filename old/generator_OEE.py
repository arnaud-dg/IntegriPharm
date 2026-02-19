import random
from datetime import datetime, timedelta
import pandas as pd


def mock_trs(n: int = 200, seed: int | None = 42) -> pd.DataFrame:
    """
    Génère un tableau TRS (OEE) simulé.
    
    Colonnes :
    - date
    - atelier
    - planned_hours
    - run_hours
    - availability
    - performance
    - quality
    - TRS_OEE

    n : nombre de lignes (par défaut 200)
    """
    if seed is not None:
        random.seed(seed)

    base_date = datetime(2025, 10, 1)
    ateliers = ["Fermentation", "Purification"]

    rows = []

    for i in range(n):
        date = base_date + timedelta(days=i)

        # Heures planifiées (ex : 2x8h à 3x8h)
        planned_hours = random.randint(16, 24)

        # Heures réellement produites (pannes, arrêts, nettoyage, etc.)
        downtime = random.randint(0, 6)
        run_hours = max(0, planned_hours - downtime)

        # Composantes TRS
        availability = run_hours / planned_hours if planned_hours else 0
        performance = random.uniform(0.75, 0.98)
        quality = random.uniform(0.90, 0.995)

        trs_oee = availability * performance * quality

        rows.append({
            "date": date.date().isoformat(),
            "atelier": random.choice(ateliers),
            "planned_hours": planned_hours,
            "run_hours": run_hours,
            "availability": round(availability, 3),
            "performance": round(performance, 3),
            "quality": round(quality, 3),
            "TRS_OEE": round(trs_oee, 3),
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df_trs = mock_trs(n=200)
    df_trs.to_csv("data/trs_mock.csv", index=False)
    print("Fichier généré : data/trs_mock.csv")
