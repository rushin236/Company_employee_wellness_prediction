import os

from empWellness.config.configration import DataValidationConfig
from empWellness.utils.common import create_directries


class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config

    def validate(self):
        create_directries([self.config.root_dir])

        dir_list = os.listdir(self.config.root_dir)

        validation_status: bool = True

        if dir_list.sort() == list(self.config.dir_names).sort():
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

        else:
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {not validation_status}")
