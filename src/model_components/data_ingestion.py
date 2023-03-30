import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
@dataclass
class DataIngestionConfig():
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')

class DataIngestion():
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initate_data_ingestion(self):
        logging.info("Beginning data Ingestion")
        try:
            file_path: str = "artifacts/tickerData.csv"
            df = pd.read_csv(file_path)
            logging.info(f"Data is being consumed from: {file_path}")
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Beginning train test data split")
            train_set,test_set = train_test_split(df,test_size=0.2)
            logging.info("Saving different files")
            train_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            logging.info("split completed")
            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initate_data_ingestion()

