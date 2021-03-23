import pandas as pd
import joblib
from sklearn.model_selection import train_test_split as tts
from deployment_model.config import config
from deployment_model.processing.validation import validate_data

#i create this funtion to avoid split test and train data
def load_and_split(*,filename: str) -> pd.DataFrame:
	data=pd.read_csv(f"{config.DATASETS_DIR}/{filename}")
	x_train, x_test, y_train, y_test = tts(
		data[config.SELECTED_FEATURES],
		data[config.TARGET],
		test_size = 0.1,
		random_state = 0
	)
	return x_train, x_test, y_train, y_test

def load_test_set(*,filename: str)->pd.DataFrame:
	_data = pd.read_csv(f"{config.DATASETS_DIR}/{filename}")
	_data = validate_data(input_data = _data)
	_data = _data[config.SELECTED_FEATURES]
	return _data


def save_pipeline(*,pipeline_to_persist) -> None:
	save_file_name = config.PIPELINE_NAME
	save_path = config.TRAINED_DIR / save_file_name
	joblib.dump(pipeline_to_persist,save_path)

	print('Save pipeline done')

def load_pipeline(*,file_name: str) -> None:
	file_path = config.TRAINED_DIR / file_name
	loaded_pipeline = joblib.load(filename=file_path)
	return loaded_pipeline 
