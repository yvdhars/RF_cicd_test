from src.data_clean import data_load_clean_strategy
import pandas as pd
import numpy as np

class DataCleanLoad:
    def __init__(self, df_path: str, parser_strategy):
        self.df_path = df_path
        self.parser_strategy = parser_strategy
    
    def LoadData_method(self):
        return self.parser_strategy.load_data()
    
    def CleanData_methoode(self):
        return self.parser_strategy.clean_data(df = self.LoadData_method())


def load(df_path:str = "test_assets/titanic.csv") -> None:

    run = DataCleanLoad(df_path=df_path, parser_strategy=data_load_clean_strategy)
    df = run.CleanData_methoode()

    print(f"shape of the df is {df.shape}")

