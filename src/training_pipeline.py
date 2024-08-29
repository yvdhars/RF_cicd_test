from train import TrainModel_rf
from sklearn.ensemble import RandomForestClassifier
from components.constants import config, start_time
import os

cwd = os.getcwd()

class RFModelTrain:

    def main(self):
        model = TrainModel_rf()
        model.load_model(model= RandomForestClassifier, ModelParameters = config.ModelParametrs)
        model.load_data(df_path = os.path.join(cwd, config.ModelAssets.common_dir.replace('start_time', start_time), "processed.csv"))
        X, Y = model.SplitDataIntoXY()
        X_train, Y_train, X_test, Y_test = model.split_train_test(X = X, Y = Y, save_data=True)
        model.train(X_train= X_train, Y_train= Y_train)
        predictions = model.predict(X_test=X_test)
        model.test_model(y_test= Y_test, predictions= predictions)
