import numpy as np
import pandas as pd
import os 
import sys
import pickle
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from src.utils import save_object




## DATA TRANSFORMATION CONFIG:
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')
    
    
## DATA TRANSFORMATION CLASS:
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformation_object(self):
        try:
            logging.info('Data transformation started')
            
            categorical_column=['car_name', 'brand', 'model', 'seller_type', 'fuel_type',
            'transmission_type']
            numerical_column=['vehicle_age', 'km_driven', 'mileage', 'engine', 'max_power', 'seats']
            
            logging.info('Pipeline Intiated')
            
            num_pipeline=Pipeline(steps=[
            ('imputer',SimpleImputer(strategy='median')),
            ('scaler',StandardScaler())   
            ])
            
            cat_pipeline=Pipeline(steps=[
            ('imputer',SimpleImputer(strategy='most_frequent')),
            ('encoder',OrdinalEncoder()),
            ('scaler',StandardScaler())   
            ])
            
            
            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_column),
            ('cat_pipeline',cat_pipeline,categorical_column)
            ])
            
            logging.info('Pipeline Complted')
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
            logging.info('Some Error Occured Into get_data_transformation_obj Method')
            
            
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info('Read Train and Test Data Completed')
            logging.info(f'Train DataFrame Head :\n{train_df.head().to_string()}')
            logging.info('Test DataFrame Head : \n{test_df.head().to_string()}')
            
            logging.info('Obtaining Preprocessor Object')
            
            preprocessor_obj=self.get_data_transformation_object()
            
            target_column_name='selling_price'
            drop_columns=[target_column_name]
            
            input_feature_train_df=train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            logging.info('Training and Testing Data is Transform')
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)          
            
            
            logging.info('Applying preprocessing object on training and testing dataset')
            
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
            
            logging.info(train_arr)
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            
            logging.info('Preprocessr pickle in created and saved')
            
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
            
            
        except Exception as e:
            raise CustomException(e,sys)
            logging.info('Some Error Occured Into initiate Data Transformation Method')
        