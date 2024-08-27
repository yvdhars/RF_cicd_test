from abc import ABC, abstractmethod
import pandas as pd

class DataLoadCleanAbstract(ABC):
    """Abstract base class for data loading and cleaning strategies."""

    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        """Load data from the specified source."""
        pass
    
    @abstractmethod
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean the provided DataFrame."""
        pass

class DataLoadCleanStrategy(DataLoadCleanAbstract):
    """Concrete strategy for loading and cleaning data."""

    def __init__(self, df_path: str):
        self.df_path = df_path

    def load_data(self) -> pd.DataFrame:
        """Load data from file based on its extension."""
        if self.df_path.endswith(".xlsx"):
            return pd.read_excel(self.df_path)
        elif self.df_path.endswith(".csv"):
            return pd.read_csv(self.df_path)
        else:
            raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean the DataFrame by dropping NA values and applying specific transformations."""
        df.dropna(inplace=True)
        df.reset_index(drop=True, inplace=True)
        df['class'].replace({'Iris-setossa': 'Iris-setosa', 'versicolor': 'Iris-versicolor'}, inplace=True)
        df = df[~((df['sepal_width_cm'] < 2.5) & (df['petal_width_cm'] < 0.5))]
        return df
