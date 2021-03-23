from deployment_model.data_management.data_management import load_pipeline
from deployment_model.config import config
import pandas as pd

#load trained pipeline and then use it to make predictions
price_pipe = load_pipeline(file_name = config.PIPELINE_NAME)
def make_prediction(*,input_data)-> dict:
	data = pd.read_json(input_data)
	prediction = price_pipe.predict(data)
	response = {"preds": prediction}
	return response