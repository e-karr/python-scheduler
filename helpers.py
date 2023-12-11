import pandas as pd
import os
import random

def is_csv_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.csv'

def validate_arguments(args):
    if len(args) < 3:
        raise ValueError('Command-line aruguments must include csv file and desired length of schedule')
    
    if not args[2].isdigit() or int(args[2]) <= 0:
        raise ValueError('Final argument must be an integer greater than 0')
    
    if not is_csv_file(args[1]):
        raise ValueError('Must submit csv file')
    
    df = pd.read_csv(args[1])

    if int(args[2]) >= len(df.index):
        raise ValueError('Desired length of schedule must be less than total number of teams')
    
    if 'team_name' not in df.columns:
        raise ValueError('CSV must include team_name column')

# create round robin schedule, keep number of weeks requested, and return dataframe
# TODO figure out how to do this without having to create a round robin schedule first (tried in another branch and got infinite loops and recursion errors)  
def create_schedule(teams, weeks):

    if len(teams) % 2 != 0:
        teams.append('bye')

    first_row = random.sample(teams, len(teams))
    permutes = random.sample(range(len(teams)), len(teams))
    
    schedule = [first_row[i:] + first_row[:i] for i in permutes]

    schedule_df = pd.DataFrame(schedule)
    schedule_df.columns = ['team_name'] + list(schedule_df.columns[1:])
    schedule_df = schedule_df.iloc[:, :weeks + 1]
    
    return schedule_df