import os
from urllib import request
from src.ML_ops_end_end_ import logger
import zipfile
from ..entity.config_entity import DataIngestionConfig

##component - data ingestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    #downlaoding the file from the source URL
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename , headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with headers:\n  {headers}")

        else:
            logger.info("file already exists")


    #unzip the file
    def extract_zip_file(self):
      """
          zip_file_path: str
          extracts the zip file into the data directory 
          function returns none
      """
      unzip_path = self.config.unzip_dir
      os.makedirs(unzip_path, exist_ok=True)
      with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
          zip_ref.extractall(unzip_path)
      


