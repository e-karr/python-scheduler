import pandas as pd
import os

def is_csv_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.csv'

def validate_arguments(args):
    if len(args) < 3:
        raise ValueError('Command-line aruguments must include csv file and desired length of schedule')
    
    if not args[2].isdigit() or int(args[2]) <= 0:
        raise ValueError('Final argument must be an integer greater than 0')
    
    if is_csv_file(args[1]) == False:
        raise ValueError('Must submit csv file')
    
    df = pd.read_csv(args[1])

    if int(args[2]) >= len(df.index):
        raise ValueError('Desired length of schedule must be less than total number of teams')