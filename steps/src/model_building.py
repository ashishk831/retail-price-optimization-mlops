import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Tuple,List

class DataSplitter:

    def __init__(self,df: pd.DataFrame, features: List[str], target: str, test_size: float=0.2) -> None:
        self.df = df
        self.features = features
        self.target = target
        self.test_size = test_size

    def split(self) -> Tuple[pd.DataFrame,pd.DataFrame,pd.Series,pd.Series]:
        X = self.df[self.features]
        y = self.df[self.target]
        X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=self.test_size,shuffle=False)
        return X_train, X_test,y_train,y_test

#class ModelRefinement:
#    """Singleton class for refining a given model."""
#
#    _instance = None
#
#    def __new__(cls, *args, **kwargs):
#        if not cls._instance:
#            cls._instance = super(ModelRefinement, cls).__new__(cls)
#        return cls._instance
#
#    def __init__(self, model, data):
#        self.model = model
#        self.data = data
#        self.predictors = [x for x in self.model.model.exog_names if x != 'const']
#        self.target = self.model.model.endog_names
#        self.rmse = None