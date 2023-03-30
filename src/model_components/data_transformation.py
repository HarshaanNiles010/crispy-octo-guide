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
    
    def initiate_data_transformation():
        logging.info("Initiating data transformation")
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataTransformation()
    obj.initiate_data_transformation()