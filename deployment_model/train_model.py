import pandas as pd
from sklearn.model_selection import train_test_split as tts
import joblib

from deployment_model import pipeline
from deployment_model.config import config

def save_pipeline(*,pipeline_to_persist) -> None:
	save_file_name = "regression_model.pkl"
	save_path = config.TRAINED_DIR / save_file_name
	joblib.dump(pipeline_to_persist,save_path)

	print('Save pipeline :\tDone')

def run_training()->None:
	data = pd.read_csv(config.DATASETS_DIR/config.TRAIN_DATA)
	x_train, x_test, y_train, y_test = tts(
		data[config.SELECTED_FEATURES],
		data[config.TARGET],
		test_size = 0.1,
		random_state = 0
		)

	pipeline.house_pipe.fit(x_train, y_train)
	
	pred = pipeline.houseprice.predict(x_train)
	print('train mse: {}'.format(mean_squared_error(y_train, pred)))
	print('train rmse: {}'.format(sqrt(mean_squared_error(y_train, pred))))
	print('train r2: {}'.format(r2_score(y_train, pred)))


	save_pipeline(pipeline_to_persist = pipeline.house_pipe)

if __name__ == "__main__":
	run_training()
