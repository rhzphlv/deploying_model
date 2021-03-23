from deployment_model.predict import make_prediction
from deployment_model.data_management.data_management import load_test_set
from deployment_model.config import config
import math

def test_single_value():
	#Given
	test_data = load_test_set(filename = config.TEST_DATA)
	json_test = test_data[0:2].to_json(orient = 'records')

	#When
	subject = make_prediction(input_data = json_test)

	#Then
	assert subject is not None
	assert isinstance(subject.get('preds')[0],float)
