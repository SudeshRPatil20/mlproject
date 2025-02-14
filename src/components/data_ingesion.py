import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_training import ModelTrainerConfig
from src.components.model_training import ModelTrainer



@dataclass
class DataIngesionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    
class DataIngesion:
    def __init__(self):
        self.ingesion_config=DataIngesionConfig()
        
    def initiate_data_ingesion(self):
        logging.info("Enter the data ingesion method or component")
        try:
            df=pd.read_csv('D:/sudesh/End to end project/notebook/data/Student.csv')
            logging.info('Read the dataset as dataframe')
            
            os.makedirs(os.path.dirname(self.ingesion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingesion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train test split initiate")
            
            train_set,test_set=train_test_split(df,test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingesion_config.train_data_path,index=False,header=True)
            
            test_set.to_csv(self.ingesion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingesion of data is incomplete")
            
            return(
                self.ingesion_config.train_data_path,
                self.ingesion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj=DataIngesion()
    train_data, test_data=obj.initiate_data_ingesion()
    
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data, test_data)
    
    
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))