from data_cleaning_pipeline import DataCleanLoad



data = DataCleanLoad()

df = data.main()

print(df.shape)