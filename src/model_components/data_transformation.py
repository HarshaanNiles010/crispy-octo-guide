import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from dataclasses import dataclass
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder,MinMaxScaler
from sklearn.compose import ColumnTransformer
@dataclass
class DataTransformationConfig():
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')
    temp_train_result_path = os.path.join('artifacts','trainResult.csv')
    temp_train_target_result_path = os.path.join('artifacts','trainTargetResult.csv')
    temp_test_result_path = os.path.join('artifacts','testResult.csv')
    temp_test_target_result_path = os.path.join('artifacts','testTargetResult.csv')

class DataTransformation():
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        logging.info("Looking for the prediction feilds")
        try:
            numerical_columns = [
                "Open",
                "High",
                "Low",
                "Adj Close",
                "Volume"
            ]
            logging.info("Starting Numerical Pipeline")
            num_pipeline = Pipeline(
                steps=[
                ("min_max_scalar",MinMaxScaler(feature_range=(0,1)))
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
    
    
    def initiate_data_transformation(self,train_path:str,test_path:str):
        logging.info("Initiating data transformation")
        try:
            """ logging.info("Reading train and test data")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")
            preprocessing_obj=self.get_data_transformer_object()
            target_column_name="Close"
            numerical_column_name = [
                "Date",
                "Open",
                "High",
                "Low",
                "Close",
                "Adj Close",
                "Volume"
            ]
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info(f"Saved preprocessing object.")
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            ) """
            """ logging.info("Reading train and test data")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")
            new_scalar = MinMaxScaler(feature_range=(0,1))
            scaled_data = new_scalar.fit_transform(train_df['Close'].values.reshape(-1,1))
            prediction_days = 60
            x_train = []
            y_train = []
            for i in range(prediction_days,len(scaled_data)):
                x_train.append(scaled_data[i-prediction_days:i,0])
                y_train.append(scaled_data[i,0])
            x_train, y_train = np.array(x_train), np.array(y_train)
            x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
            return(
                x_train,
                y_train,
                self.data_transformation_config.preprocessor_obj_file_path
            ) """
            logging.info("Reading train and test data")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()
            logging.info("Preprocessor object obtained")
            target_column_name="Close"
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]
            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]
            logging.info("Applying preprocessing object on training dataframe and testing dataframe.")
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info(f"Saved preprocessing object.")
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            ) 
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataTransformation()
    obj.initiate_data_transformation()