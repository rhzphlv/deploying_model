from sklearn.preprocessing import MaxAbsScaler
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline

from feature_engine.discretisation import DecisionTreeDiscretiser as DTD

from feature_engine.encoding import (
    DecisionTreeEncoder as DTE,
    RareLabelEncoder as RLE
)

from feature_engine.imputation import (
    AddMissingIndicator as AMI,
    ArbitraryNumberImputer as ANI,
    CategoricalImputer as CI
)

from deployment_model.config import config

#normal sklearn pipeline
#define what feature that we want to engineer
house_pipe = Pipeline([
    
    ('missing_ind', AMI(
        variables=[i for i in config.ADD_MISSING_INDICATOR if i in config.SELECTED_FEATURES])),
    
    ('imputer_num', ANI(
        arbitrary_number=0,
        variables=[i for i in config.YEAR if i in config.SELECTED_FEATURES]+\
		          [i for i in config.DISCRETE if i in config.SELECTED_FEATURES]+\
		          [i for i in config.CONTINOUS if i in config.SELECTED_FEATURES])),
		    
    ('imputer_cat', CI(
        variables=[i for i in config.CATEGORICAL if i in config.SELECTED_FEATURES])),
    
    ('discretisation',DTD(
        random_state=1,
        variables=[i for i in config.YEAR if i in config.SELECTED_FEATURES]+\
		          [i for i in config.DISCRETE if i in config.SELECTED_FEATURES]+\
		          [i for i in config.CONTINOUS if i in config.SELECTED_FEATURES])),

    ('rare_label_enc', RLE(
        tol=0.007, 
        n_categories=1, 
        variables=[i for i in config.CATEGORICAL if i in config.SELECTED_FEATURES])),
    
    ('categorical_enc',DTE(
        random_state=1,
        variables= [i for i in config.CATEGORICAL if i in config.SELECTED_FEATURES])),

    ('scaler', MaxAbsScaler()),
    
    ('lasso', Lasso(random_state=0))
])