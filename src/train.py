from abc import ABC, abstractmethod
import pandas as pd
from typing import Union
from sklearn.base import ClassifierMixin, RegressorMixin
from sklearn.metrics import accuracy_score, r2_score
from sklearn.model_selection import train_test_split


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

    def load_model(self, model: Union[ClassifierMixin, RegressorMixin]) -> Union[ClassifierMixin, RegressorMixin]:
        self.model = model
        return self.model
    
    def SplitDataIntoXY(self, df: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
         X= df[:-1]
         Y= df.iloc[:, -1]
             
         return X, Y


    def split_train_test(self, X: pd.DataFrame, Y: pd.Series, save_data: bool = False) -> None:
        X_train, Y_train, X_test, Y_test = train_test_split(X, Y, random_state = 42)
        if save_data:
            df = 
        return X_train, Y_train, X_test, Y_test

    def train(self, model: Union[ClassifierMixin, RegressorMixin], X_train: pd.DataFrame, y_train: pd.Series) -> None:
        model.fit(X_train, y_train)

    def predict(self, model: Union[ClassifierMixin, RegressorMixin], X_test: Union[pd.DataFrame, pd.Series]) -> pd.Series:
        return model.predict(X_test)

    def test_model(self, y_test: pd.Series, predictions: pd.Series) -> None:
        accuracy = accuracy_score(y_test, predictions)
        print(f"Accuracy: {accuracy:.2f}")
