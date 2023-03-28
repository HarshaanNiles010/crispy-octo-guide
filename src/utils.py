import os
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        logging.info(f"Saving the object on file path: {file_path}")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
        logging.info(f"File object saved successfully")
    except Exception as e:
        raise CustomException(e,sys)

def load_obj(file_path):
    try:
        logging.info(f"Loading file object from the given file path: {file_path}")
        with open(file_path,'rb') as file_obj:
            logging.info("File object loaded successfully")
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)