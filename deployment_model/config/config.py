import pathlib
import deployment_model

ROOT_DIR = pathlib.Path(deployment_model.__file).resolve().parent
TRAINED_DIR = ROOT_DIR / "trained_model"
DATASETS_DIR = ROOT_DIR / "datasets"

TEST_DATA = "test.csv"
TRAIN_DATA = "train_data"
TARGET = 'SalePrice'

CATEGORICAL = [ 'MSZoning','Street','Alley','LotShape','LandContour',
				'Utilities','LotConfig','LandSlope','Neighborhood','Condition1',
				'Condition2','BldgType','HouseStyle','RoofStyle','RoofMatl',
				'Exterior1st','Exterior2nd','MasVnrType','ExterQual','ExterCond',
				'Foundation','BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1',
				'BsmtFinType2','Heating','HeatingQC','CentralAir','Electrical',
				'KitchenQual','Functional','FireplaceQu','GarageType',
				'GarageFinish','GarageQual','GarageCond','PavedDrive',
				'PoolQC','Fence','MiscFeature','SaleType','SaleCondition']

YEAR = ['YearBuilt', 'YearRemodAdd', 'GarageYrBlt', 'YrSold']

CONTINOUS = ['LotFrontage','LotArea','MasVnrArea','BsmtFinSF1',
			 'BsmtFinSF2','BsmtUnfSF','TotalBsmtSF','1stFlrSF',
			 '2ndFlrSF','GrLivArea','GarageArea','WoodDeckSF',
			 'OpenPorchSF','EnclosedPorch','ScreenPorch']

DISCRETE = ['MSSubClass','OverallQual','OverallCond','LowQualFinSF',
			'BsmtFullBath','BsmtHalfBath','FullBath','HalfBath',
			'BedroomAbvGr','KitchenAbvGr','TotRmsAbvGrd','Fireplaces',
			'GarageCars','3SsnPorch','PoolArea','MiscVal','MoSold']

YEAR_VARIABLE = 'YrSold'

SELECTED_FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood',
		            'OverallQual', 'OverallCond', 'YearRemodAdd',
		            'RoofStyle', 'MasVnrType', 'BsmtQual', 'BsmtExposure',
		            'HeatingQC', 'CentralAir', '1stFlrSF', 'GrLivArea',
		            'BsmtFullBath', 'KitchenQual', 'Fireplaces', 'FireplaceQu',
		            'GarageType', 'GarageFinish', 'GarageCars', 'PavedDrive',
		            'LotFrontage','YrSold']

ADD_MISSING_INDICATOR = ['LotFrontage','GarageYrBlt']
