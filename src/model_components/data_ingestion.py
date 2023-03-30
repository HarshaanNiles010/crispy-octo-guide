import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
@dataclass
class DataIngestionConfig():
    train_data_path: str = os.join.path('artifacts','train.csv')
    test_data_path: str = os.join.path('artifacts','test.csv')
    raw_data_path: str = os.join.path('artifacts','data.csv')

class DataIngestion():
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initate_data_ingestion(self):
        logging.info("Beginning data Ingestion")
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    pass

