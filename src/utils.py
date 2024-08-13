import os 
import sys
from src.logger import logging
from src.exception import CustomException
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

def save_object(file_path:str,obj):
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
        report={}
        for i in range(len(models)):
            model=list(models.values())[i] 
            model.fit(X_train,Y_train)
            
            y_test_pred=model.predict(X_test)
            
            test_model_score=r2_score(y_test,y_test_pred)
            
            report[list(models.keys())[i]]=test_model_score
            
        return report

    
    except Exception as e:
        raise CustomException(e,sys)
        logging.info('Some Error Occured in model evaluation method')
        
def load_object(file_path):
    try:
        logging.info('Loading Objects from file')
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
            

    except Exception as e:
        raise CustomException(e,sys)
        logging.info('Some Error Occured into in load object function in utils file')
        