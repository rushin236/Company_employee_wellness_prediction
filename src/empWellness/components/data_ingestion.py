import os

import requests

from empWellness.entity import DataIngestionConfig
from empWellness.logging import logger
from empWellness.utils.common import create_directries


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def ingest(self):
        try:
            logger.info("Ingestion started!")

            create_directries([self.config.root_dir])

            file_name = ["train.csv", "test.csv", "submission.csv"]

            for i in range(len(self.config.source_URL)):
                file_path = os.path.join(
                    self.config.root_dir, self.config.data_dir[i], file_name[i]
                )

                if not os.path.exists(file_path):
                    file_dir = os.path.join(
                        self.config.root_dir, self.config.data_dir[i]
                    )
                    create_directries([file_dir])
                    logger.info(f"created dirctory: {file_dir[i]} for {file_name[i]}")

                    response = requests.get(self.config.source_URL[i])
                    raw_data = response.content.decode(
                        encoding="utf-8", errors="ignore"
                    )
                    logger.info(f"File: {file_name[i]} downloaded!")

                    with open(file_path, "w") as f:
                        f.write(raw_data)
                        logger.info(f"File: {file_name[i]} saved to {file_dir[i]}")

                else:
                    logger.info(f"File: {file_name} already exists!")

        except Exception as e:
            raise e
