import random

import pandas as pd

def validate_schedule_length(length, df_file):
    if not length.isdigit() or int(length) <= 0:
        raise ValueError('Final argument must be an integer greater than 0')
    
    if int(length) >= len(df_file.index) and len(df_file.index) % 2 == 0:
        raise ValueError('Desired length of schedule must be less than total number of teams')
    elif len(df_file.index) % 2 != 0 and int(length) > len(df_file.index):
        raise ValueError('Desired length of schedule must be less than or equal to total number of teams')
    
    return int(length)

# create round robin schedule, keep number of weeks requested, and return dataframe 
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