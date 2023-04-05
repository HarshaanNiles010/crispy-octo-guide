import os
import sys
import pandas as pd
import numpy as np 
from src.exception import CustomException
from src.logger import logging
#from keras.models import Sequential
#from keras.layers import Dense,Dropout,LSTM
from dataclasses import dataclass

from src.utils import save_object

@dataclass
class ModelTrainerConfig():
    trainer_model_file_path:str = os.path.join('artifacts','model.pkl')

class ModelTrainer():
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initate_model_trainer(self,train_array,test_array):
        logging.info("initiating model training")
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)