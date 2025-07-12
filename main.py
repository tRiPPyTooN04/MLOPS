import sys
from pathlib import Path

# Tell Python to look inside src/
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from ML_ops_end_end_ import logger
from ML_ops_end_end_.pipeline.data_ingestion import DataIngestionTrainingPipeline
from ML_ops_end_end_.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e