import numpy as np
import pandas as pd
import os
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


## DATA INGESTION CONFIG CLASS:
@dataclass
class DataIngestionConfig:
    raw_data_path=os.path.join('artifacts','raw.csv')
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    
## DATA INGESTION CLASS:

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info('Starting data ingestion')
        try:
            df=pd.read_csv(os.path.join('notebooks/data','cardekho_dataset.csv'))
            logging.info('Data set read as Pandas DataFrame') 
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            
            
            logging.info('Train Test Split')

            train_set,test_set=train_test_split(df,test_size=0.25,random_state=45)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info('Data Ingestion Completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )  
        
        except Exception as e:
            raise CustomException(e,sys)
            logging.info('Some Error Occured Into Data Ingestion Class')     