import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from utils import save_object
from dataclasses import dataclass
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer

@dataclass
class DataTransformationConfig():
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation():
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        logging.info("Looking for the prediction feilds")
        try:
            numerical_columns = [
                "Date",
                "Open",
                "High",
                "Low",
                "Close",
                "Adj Close",
                "Volume"
            ]
            logging.info("Starting Numerical Pipeline")
            num_pipeline = Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scalar",StandardScaler())
                ]
            )
            logging.info("Numerical cloumns completed")
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    
    
    def initiate_data_transformation(self):
        logging.info("Initiating data transformation")
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataTransformation()
    obj.initiate_data_transformation()