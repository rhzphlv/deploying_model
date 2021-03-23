from deployment_model.config import config
import pandas as pd

def validate_data(*,input_data)->pd.DataFrame:
	validated_data = input_data.copy()
	features = config.CATEGORICAL + config.DISCRETE + config.CONTINOUS + config.YEAR
	selected_features = [i for i in features if i in config.SELECTED_FEATURES]
	
	#check missing values from every variables
	if validated_data[selected_features].isna().any().any():
		validated_data = validated_data.dropna(
			axis = 0,
			subset = selected_features
			)

	return validated_data

