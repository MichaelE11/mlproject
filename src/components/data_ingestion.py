import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

#to create imputs where raw data, training data and test data will be saved
# this is creating a path called artifact where it saves the train, test and raw data.

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', "train.csv") #this state where to store the train csv
    test_data_path: str=os.path.join('artifacts', "test.csv") #this state where to store the test csv
    raw_data_path: str=os.path.join('artifacts', "data.csv") #this state where to store the data csv
 #name of the folder where they are stored is artifact
    #to start the data injestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # calling this willtriger the use of Dataingestion config


    def initiate_data_ingestion(self):
        logging.info("Enter the data injestion method or component")
        try:
            df=pd.read_csv("notebook\data\stud.csv") #reading the data
            logging.info("Read the dataset as data frame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            #making the path of train data in artifact. this will go through self.ingestion_config and the pic dfor the train data

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            #saves the data to raw data path. note the index is removed

            logging.info(" Train test split initated")

            train_set, test_set=train_test_split(df, test_size=0.3, random_state=42)
            #spplitting data to train set and test set

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            # save train_set as csv in train data path
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            # save test set to test data path
            logging.info("Ingestion of the data is completed")
            return{
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path 
            }

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    Obj=DataIngestion()
    train_data, test_data=Obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)

