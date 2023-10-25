import pandas as pd
import numpy as np

def preprocess():
    print("Vamos processar os dados!")

def load_data():
    # Ler o arquivo CSV usando pandas
    df = pd.read_csv("titanic_dataset.csv")

    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Removendo linhas que contêm valores NaN
    cleaned_df = df.dropna()

    return cleaned_df

if __name__ == '__main__':
    preprocess()
