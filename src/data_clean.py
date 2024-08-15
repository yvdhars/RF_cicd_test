from abc import abstractmethod, ABC
import pandas as pd
import numpy as np

class data_load_clean_abstract(ABC):
    """
    creating abstract class to load data from different sources
    """

    @abstractmethod
    def load_data(self,df_path: str)-> None:
        return None
    
    @abstractmethod
    def clean_data(self,df: pd.DataFrame)-> None:
        return None
    


class data_load_clean_strategy(data_load_clean_abstract):

    def __init__(self, df_path: str):
        self.df_path = df_path

    def load_data(self) -> pd.DataFrame:
        df = pd.DataFrame()
        if self.df_path.endswith(".xlsx"):
            df = pd.read_excel(self.df_path) 
        elif self.df_path.endswith(".csv"):
            df = pd.read_csv(self.df_path)
        else:
            print("not able to load and clean data from the given input file please check the input")
        return df
    
    def clean_data(self,df: pd.DataFrame) -> pd.DataFrame:
        df.dropna(inplace=True)
        df.reset_index(inplace=True)
        return df