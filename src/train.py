from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
import os, sys
from typing import Union
from time import time
from pathlib import Path
from sklearn.base import ClassifierMixin, RegressorMixin
from sklearn.metrics import accuracy_score, r2_score
from sklearn.model_selection import train_test_split


from components.constants import config, start_time


class TrainModel_abstract(ABC):
    
    @abstractmethod
    def split_train_test(self, X: pd.DataFrame, Y: pd.Series) -> None:
        """Splits the data into training and test sets."""
        pass
    
    @abstractmethod
    def load_model(self) -> Union[ClassifierMixin, RegressorMixin]:
        """Returns an instance of the model to be trained."""
        pass

    @abstractmethod
    def load_data(self, df_path: Path) ->None:
        """Loads cleanded df from the assets dir """
        pass
    
    @abstractmethod
    def train(self, model: Union[ClassifierMixin, RegressorMixin], X_train: pd.DataFrame, y_train: pd.Series) -> None:
        """Trains the model on the training data."""
        pass
    
    @abstractmethod
    def predict(self, model: Union[ClassifierMixin, RegressorMixin], X_test: Union[pd.DataFrame, pd.Series]) -> pd.Series:
        """Makes predictions using the trained model."""
        pass
    
    @abstractmethod
    def test_model(self, y_test: pd.Series, predictions: pd.Series) -> None:
        """Evaluates the model's performance on the test data."""
        pass

class TrainModel_rf(TrainModel_abstract):
    def __init__(self):
        self.model = None
        self.df = None

    def load_model(self, model: Union[ClassifierMixin, RegressorMixin], ModelParameters : dict) -> Union[ClassifierMixin, RegressorMixin]:
        self.model = model(**ModelParameters)
        return self.model
    
    def load_data(self, df_path: Path) -> pd.DataFrame:
        self.df = pd.read_csv(df_path)
        return self.df    
    
    def SplitDataIntoXY(self) -> Union[pd.DataFrame, pd.Series]:
         X= self.df.iloc[:, :-1]
         Y= self.df.iloc[:, -1]
         return X, Y


    def split_train_test(self, X: pd.DataFrame, Y: pd.Series, save_data: bool = False) -> None:
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 42, test_size= 0.2)
        if save_data:
            cwd = os.getcwd()
            df_train = pd.concat([X_train, Y_train], axis=1)
            df_test = pd.concat([X_test, Y_test], axis=1)
            df_train.to_csv(os.path.join(cwd, config.ModelAssets.dir, start_time, "train.csv"))    
            df_test.to_csv(os.path.join(cwd, config.ModelAssets.dir, start_time, "test.csv"))     
        return X_train, Y_train, X_test, Y_test

    def train(self, X_train: pd.DataFrame, Y_train: pd.Series) -> None:
        self.model.fit(X_train, Y_train)
        return None

    def predict(self, X_test: Union[pd.DataFrame, pd.Series]) -> Union[pd.Series, np.array]:
        return self.model.predict(X_test)

    def test_model(self, y_test: pd.Series, predictions: pd.Series) -> float:
        accuracy = accuracy_score(y_test, predictions)
        print(f"Accuracy: {accuracy:.2f}")
        return accuracy
    
    def get_model(self) -> Union[RegressorMixin, ClassifierMixin]:
        return self.model
