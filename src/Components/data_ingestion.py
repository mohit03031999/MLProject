import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class dataIngestionConfigs:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


class dataIngestion:
    def __int__(self):
        self.ingestion_conig = dataIngestionConfigs()

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        try:
            df = pd.read_csv('src/data/stud.csv')  #Raed the dataset
            logging.info("Read the dataset as DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_conig.train_data_path),exist_ok=True) #Create the directory and if exits keep

            df.to_csv(self.ingestion_conig.raw_data_path,index=False,header=True)

            train_set,test_set = train_test_split(df,test_size=0.3,random_state=42)

            train_set.to_csv(self.ingestion_conig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_conig.test_data_path,index=False,header=True)

            logging.info("Completed the Ingestion of Config")

            return (
                self.ingestion_conig.train_data_path,
                self.ingestion_conig.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
