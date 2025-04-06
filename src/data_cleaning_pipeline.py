import pandas as pd
import os
from pathlib import Path
from components.constants import config, start_time
from data_clean import DataLoadCleanStrategy

cwd = os.getcwd()

class DataCleanLoad:
    def __init__(self, parser_strategy: DataLoadCleanStrategy = DataLoadCleanStrategy(config.data.input_file)):
        self.df_path = Path(config.data.input_file)
        self.parser_strategy = parser_strategy

    def load_data(self) -> pd.DataFrame:
        """Load data using the provided parser strategy."""
        return self.parser_strategy.load_data()

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean the data using the provided parser strategy."""
        return self.parser_strategy.clean_data(df)

    def main(self) -> pd.DataFrame:
        """Main method to load and clean data, and print the DataFrame shape."""
        df = self.load_data()
        cleaned_df = self.clean_data(df)
        print(f"Shape of the cleaned DataFrame: {cleaned_df.shape}")
        cleaned_df.to_csv(os.path.join(cwd, config.ModelAssets.dir, "processed.csv"))
        return cleaned_df

if __name__ == "__main__":
    pipeline = DataCleanLoad()
    pipeline.main()
