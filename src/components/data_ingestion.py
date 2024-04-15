import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


#to create imputs where raw data, training data and test data will be saved
# this is creating a path called artifact where it saves the train, test and raw data.

@dataclass
class DataInjgestionConfig:
    train_data_path: str=os.path.join('artifacts', "train.csv")
    test_data_path: str=os.path.join('artifacts', "test.csv")
    raw_data_path: str=os.path.join('artifacts', "data.csv")

    #to start the data injestion class
class DataInjestion:
    def __init__(self):
        self.injestion_config=DataInjgestionConfig()

    def initiate_data_injestion(self):
        logging.info("Enter the data injestion method or component")
        try:
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as data frame")

            os.makedirs(os.path.dirname(self.injestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.injestion_config.raw_data_path, index=False, header=True)

            logging.info(" Train test split initated")

            train_set, test_set=train_test_split(df, test_size=0.3, random_state=42)

            train_set.to_csv(self.injestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.injestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is completed")
            return{
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path,
            }

        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__":
    Obj=DataInjestion()
    Obj.initiate_data_injestion()

