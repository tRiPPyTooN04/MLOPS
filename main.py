import sys
from pathlib import Path

# Tell Python to look inside src/
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from ML_ops_end_end_ import logger
from ML_ops_end_end_.pipeline.data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e