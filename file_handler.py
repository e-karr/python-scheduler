import os

import pandas as pd

class FileHandler:
    def __init__(self, file):
        self.file = file

    def validate(self):
        raise NotImplementedError("Subclasses must implement the 'validate' method")
    
    def read_file(self):
        raise NotImplementedError("Subclasses must implement the 'read_file' method")
    
    @staticmethod
    def check_columns(df):
        if 'team_name' not in df.columns:
            raise ValueError("File must include 'team_name' column")
    
class Csv(FileHandler):
    @staticmethod
    def validate(file):
        _, file_extension = os.path.splitext(file)
        return file_extension.lower() == '.csv'
        
    def read_file(self):
        df = pd.read_csv(self.file)
        self.check_columns(df)
        return df
    
class Excel(FileHandler):
    @staticmethod
    def validate(file):
        _, file_extension = os.path.splitext(file)
        return file_extension.lower() in ['.xls', '.xlsx']
        
    def read_file(self):
        df = pd.read_excel(self.file)
        self.check_columns(df)
        return df
