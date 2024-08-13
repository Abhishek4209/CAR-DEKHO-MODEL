import numpy as np
import pandas as pd
import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
# from xgboost import XGBoostRegressor

from src.utils import save_object,evaluate_model





## MODEL TRAINER CONFIG:
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

## MODEL TRAINER:
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        
    def intiate_model_trainer(self,train_array,test_array):
        try:
            logging.info('Spliting Dependent and Independent Variables from train and test data')
            
            X_train, Y_train, X_test, Y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                
                test_array[:,:-1],
                test_array[:,-1]
            )
            
            models = {     
            "Linear Regression": LinearRegression(),
            'Ridge Regression':Ridge(),
            'Lasso Regression':Lasso(),
            'Elasticnet Regression':ElasticNet(),
            'SVR':SVR(),
            "Decision Tree": DecisionTreeRegressor(),
            'KNeighborsRegressor':KNeighborsRegressor(algorithm='auto'),
            "Random Forest": RandomForestRegressor(criterion='absolute_error',max_features=None,n_estimators=256),
            'AdaboostRegressor':AdaBoostRegressor(),
            # "XGBRegressor": XGBRegressor(learning_rate=0.01,n_estimators=32),
            }
            
        
            model_report:dict=evaluate_model(X_train, Y_train,X_test,Y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            raise CustomException(e,sys)
            logging.info('Some Error Occured into Intiate model trainer Class')
            
            