import requests

from empWellness.constants import *
from empWellness.entity import DataIngestionConfig
from empWellness.utils.common import create_directries, read_yaml


class ConfigurationManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ) -> None:
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directries([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            data_dir=config.data_dir,
        )

        return data_ingestion_config
