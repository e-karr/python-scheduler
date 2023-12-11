import pandas as pd
import os
import sys
import random
from pathlib import Path
from helpers import validate_arguments

validate_arguments(sys.argv)

file = sys.argv[1]
schedule_length = int(sys.argv[2])

teams_dataframe = pd.read_csv(file)

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

schedule = create_schedule(teams_dataframe["team_name"].tolist(), schedule_length)

final_schedule = teams_dataframe.merge(schedule, how='inner', on='team_name')

filepath = Path('./output/schedule.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)

final_schedule.to_csv(filepath)

print(final_schedule)

# TODO user interface