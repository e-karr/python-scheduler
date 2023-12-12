import pandas as pd
import sys
from pathlib import Path
from helpers import validate_arguments, create_schedule

# ensure command line arguments are valid
validate_arguments(sys.argv)

file = sys.argv[1]
schedule_length = int(sys.argv[2])

# read csv into dataframe
teams_dataframe = pd.read_csv(file)

# create schedule, returns dataframe
schedule = create_schedule(teams_dataframe['team_name'].tolist(), schedule_length)

# merge schedule dataframe into teams dataframe
final_schedule = teams_dataframe.merge(schedule, how='inner', on='team_name')

# save schedule to csv
filepath = Path('./output/schedule.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
final_schedule.to_csv(filepath)

print(final_schedule)

# TODO user interface