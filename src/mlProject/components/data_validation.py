from mlProject.entity.config_entity import DataValidationConfig
from mlProject.config.configuration import ConfigurationManager
import os
from mlProject import logger
import pandas as pd

class DataValidation:
    def __init__(self, config:DataValidationConfig) :
        self.config = config

    def validate_all_columns(self):
        try:
            validation_status = None
            df = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(df.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation status: {validation_status}")
            return validation_status

        except Exception as e:
            raise e