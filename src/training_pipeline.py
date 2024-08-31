from train import TrainModel_rf
from sklearn.ensemble import RandomForestClassifier
from components.constants import config, start_time
import mlflow
import os

cwd = os.getcwd()
model_assets_dir = os.path.join(cwd, config.ModelAssets.dir)

# Ensure the model assets directory URI starts with 'file:///'
tracking_uri = f"file:///{model_assets_dir}"
registry_uri = f"file:///{model_assets_dir}"

# Set MLflow tracking URI and registry URI
mlflow.set_tracking_uri(tracking_uri)
mlflow.set_registry_uri(registry_uri)


mlflow.set_experiment(config.experiment_name)


class RFModelTrain:

    def main(self):
        with mlflow.start_run() as run:
            model = TrainModel_rf()
            model.load_model(model= RandomForestClassifier, ModelParameters = config.ModelParametrs)
            model.load_data(df_path = os.path.join(cwd, config.ModelAssets.dir, "processed.csv"))
            X, Y = model.SplitDataIntoXY()
            X_train, Y_train, X_test, Y_test = model.split_train_test(X = X, Y = Y)
            model.train(X_train= X_train, Y_train= Y_train)
            predictions = model.predict(X_test=X_test)
            accuracy = model.test_model(y_test= Y_test, predictions= predictions)
            rf_model = model.get_model()
            mlflow.sklearn.log_model(rf_model, "model")
            mlflow.log_params(config.ModelParametrs)
            mlflow.log_metric("accuracy", accuracy)
