import numpy as np
import pandas as pd
import os 
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__ == '__main__':
    # DATA INGESTION START:
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)
    logging.info('Data Ingestion Class Succesfully Complted')
    
    # DATA TRANSFORMATION START:
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    
    
    # MODEL TRAINER START:
    model_trainer=ModelTrainer()
    model_trainer.intiate_model_trainer(train_arr,test_arr)
