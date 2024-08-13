import numpy as np
import pandas as pd
import os 
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object

class PredictionPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')
            
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            
            data_scaled=preprocessor.transform(features)
            pred=model.predict(data_scaled)
            
            return pred
        
        
        except Exception as e:
            raise CustomException(e,sys)
            logging.info('some error Occured into predict method')
            
class CustomData:
    def __init__(self,
                car_name:str,
                brand:str,
                model:str,
                vehicle_age:int,
                km_driven:int,
                seller_type:str,
                fuel_type:str,
                transmission_type:str,
                mileage:float,
                engine:int,
                max_power:float,
                seats:int 
                ):
        self.car_name=car_name
        self.brand=brand
        self.model=model
        self.vehicle_age=vehicle_age
        self.km_driven=km_driven
        self.seller_type=seller_type
        self.fuel_type=fuel_type
        self.transmission_type=transmission_type
        self.mileage=mileage
        self.engine=engine
        self.max_power=max_power
        self.seats=seats
        
        
    
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict={
                'car_name':[self.car_name],
                'brand':[self.brand],
                'model':[self.model],
                'vehicle_age':[self.vehicle_age],
                'km_driven':[self.km_driven],
                'seller_type':[self.seller_type],
                'fuel_type':[self.fuel_type],
                'transmission_type':[self.transmission_type],
                'mileage':[self.mileage],
                'engine':[self.engine],
                'max_power':[self.max_power],
                'seats':[self.seats]
                
            }
        
            df=pd.DataFrame(custom_data_input_dict)
            logging.info('DataFrame Gathered')
            return df
                
        except Exception as e:
            raise CustomException(e,sys)
            logging.info('Some Error Occured into get data as dataframe method')
            
        