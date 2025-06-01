# entity - return type of the function
from collections import namedtuple # file_format

DataIngestionConfig = namedtuple("DatasetConfig", ["dataset_download_url",
                                                   "raw_data_dir",
                                                   "ingested_dir"]) # dataset directory is not required