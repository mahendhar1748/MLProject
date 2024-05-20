import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#forming data injestion path config  ---> Routing

@dataclass
class DataIngestionConfig:
    raw_data_path: str=os.path.join('artifacts','data.csv')
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        #this below variable holds the above paths of data 
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # here only we can read the data., like sql,mongodb..etc. for our case we are taking csv
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the data set as the Data Frame")
            
            os.makedirs((self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("train test split initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=40)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            train_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of Data Completed")
            #pass

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
            #pass

if __name__=="__main_":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

