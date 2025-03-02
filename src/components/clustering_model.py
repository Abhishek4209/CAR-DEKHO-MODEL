import numpy as np
import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.utils import save_object
from dataclasses import dataclass

@dataclass
## ClusterConfig Class:
class ClusterModelConfigClass:
    cluster_model_file_path=os.path.join('artifacts','cluster_model.pkl')


## Cluster Making:
@dataclass
class ClusterModel:
    def __init__(self):
        self.cluster_model_config=ClusterModelConfig()
        
    def initiate_cluster_model_trainer():
        try:
            pass
        
        except Exception as e:
            raise CustomException(e,sys)
            logging.info('Some Error Occured into initiate_cluster_model_trainer function')
            
        
        






