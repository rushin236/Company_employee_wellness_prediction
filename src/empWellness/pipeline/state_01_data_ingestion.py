from empWellness.components.data_ingestion import DataIngestion
from empWellness.config.configration import ConfigurationManager


class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.ingest()
