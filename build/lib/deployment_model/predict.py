from deployment_model.processing.data_management import load_pipeline
from deployment_model.config import config
from deployment_model import __version__ as _version
import pandas as pd
import logging

_logger = logging.getLogger(__name__)

#load trained pipeline and then use it to make predictions
pipeline_name = f"{config.PIPELINE_FILE}{_version}.pkl"
price_pipe = load_pipeline(file_name = pipeline_name)

def make_prediction(*,input_data)-> dict:
	data = pd.read_json(input_data)
	prediction = price_pipe.predict(data)
	results = {
		"predictions": prediction,
		"version" : _version
	}

	_logger.info(
		f"Making predictions with version {_version}"
		f"Input: {data}"
		f"prediction : {results}"

	)
	return results