import os 
import sys
from src.logger import logging
from src.exception import CustomException
import pickle
import numpy as np
import pandas as pd



def save_object(file_path:str):
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
            
                
    except Exception as e:
        raise CustomException(e,sys)
        logging.info('Some Error Occured Into save objects method')
        
def evaluate_model(X_train,Y_train,X_test,y_test,models):
    try:
        pass
    
    except Exception as e:
        raise CustomException(e,sys)
        logging.info('Some Error Occured in model evaluation method')
        