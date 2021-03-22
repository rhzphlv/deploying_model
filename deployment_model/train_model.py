from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
import joblib

from deployment_model import pipeline
from deployment_model.config import config
from deployment_model.data_management.data_management import load_and_split, save_pipeline 

def run_training()->None:
	x_train, x_test, y_train, y_test= load_and_split(filename=config.TRAIN_DATA)

	pipeline.house_pipe.fit(x_train, y_train)
	

	print("Model Preformance")
	pred = pipeline.house_pipe.predict(x_train)
	print("\n")
	print("Training results: \n")
	print('Train mse\t: {}'.format(mean_squared_error(y_train, pred)))
	print('Train rmse\t: {}'.format(sqrt(mean_squared_error(y_train, pred))))
	print('Train r2 \t: {}'.format(r2_score(y_train, pred)))
	print("\n")

	pred = pipeline.house_pipe.predict(x_test)
	print("\n")
	print("Test results: \n")
	print('Test mse\t: {}'.format(mean_squared_error(y_test, pred)))
	print('Test rmse\t: {}'.format(sqrt(mean_squared_error(y_test, pred))))
	print('Test r2 \t: {}'.format(r2_score(y_test, pred)))
	print("\n")

	save_pipeline(pipeline_to_persist = pipeline.house_pipe)

if __name__ == "__main__":
	run_training()
