from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: list
    data_dir: list


@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: Path
    dir_names: list
