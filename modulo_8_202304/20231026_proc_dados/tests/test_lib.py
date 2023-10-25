import intelidata.lib as intelidata
import pandas as pd
import numpy as np


def test_preprocess_output(capfd):  # capfd é um "fixture" do pytest para capturar saídas impressas.
    intelidata.preprocess()
    out, err = capfd.readouterr()
    assert out == "Vamos processar os dados!\n", "A saída impressa não corresponde ao esperado"

def test_load_data():
    df = intelidata.load_data()
    assert isinstance(df, pd.DataFrame), "A função não retorna um DataFrame do pandas."
    # Supondo que o arquivo "titanic_dataset.csv" tenha pelo menos uma linha (sem contar o cabeçalho)
    assert not df.empty, "O DataFrame retornado está vazio."

def test_clean_data():
    # Criando um DataFrame de exemplo com valores NaN
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, np.nan, 6],
        'C': [np.nan, 8, 9],
    })

    cleaned_df = intelidata.clean_data(df)
    assert cleaned_df.shape[0] == 1, "O DataFrame limpo deve conter apenas uma linha."
    assert cleaned_df.shape[1] == 3, "O DataFrame limpo deve conter três colunas."
    assert not cleaned_df.isnull().any().any(), "O DataFrame limpo não deve conter valores NaN."
