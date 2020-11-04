import pandas as pd
from src.parameters import intervention_file


def backup_interventions(interventions):
    df = pd.DataFrame(interventions)
    df.to_csv(intervention_file)
