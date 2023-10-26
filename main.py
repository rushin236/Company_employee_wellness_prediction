from empWellness.logging import logger
from empWellness.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from empWellness.pipeline.stage_02_data_validation import DataValidationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} Started! <<<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> {STAGE_NAME} Successfully Completed! <<<<<<<<<<<")
except Exception as e:
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} Started! <<<<<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>> {STAGE_NAME} Successfully Completed! <<<<<<<<<<<")
except Exception as e:
    raise e
