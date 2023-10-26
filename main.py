from empWellness.logging import logger
from empWellness.pipeline.state_01_data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} Started! <<<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> {STAGE_NAME} Successfully Completed! <<<<<<<<<<<")
except Exception as e:
    raise e
