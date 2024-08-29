from data_cleaning_pipeline import DataCleanLoad
from training_pipeline import RFModelTrain


print("__________________________________________ data cleaning initiated __________________")
try:
    data = DataCleanLoad()
    df = data.main()
except Exception as e:
    print("error", e)


print("__________________________________________ data cleaning Completed __________________")




print("__________________________________________ model training initiated __________________")
train_model = RFModelTrain()
train_model.main()

print('___________________________________________ model training is completed ____________________')
