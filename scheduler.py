import pandas as pd
import sys
import random

# TODO validate length of command line arguments
# TODO validate first argument is csv file
# TODO allow user to have second argument of number of weeks, validate argument is number, validate that number isn't larger than number of rows in csv - 1

file = sys.argv[1]
schedule_length = int(sys.argv[2])

teams_dataframe = pd.read_csv(file)

# create round robin schedule, keep number of weeks requested, and return dataframe
# TODO figure out how to do this without having to create a round robin schedule first
# TODO if uneven number of teams, give one team a bye each week
def create_schedule(teams, weeks):
    first_row = random.sample(teams, len(teams))
    permutes = random.sample(range(len(teams)), len(teams))
    
    schedule = [first_row[i:] + first_row[:i] for i in permutes]

    schedule_df = pd.DataFrame(schedule)
    schedule_df.columns = ['team_name'] + list(schedule_df.columns[1:])
    schedule_df = schedule_df.iloc[:, :weeks + 1]
    
    return schedule_df

schedule = create_schedule(teams_dataframe["team_name"].tolist(), schedule_length)

final_schedule = teams_dataframe.merge(schedule, how='inner', on='team_name')

print(final_schedule)

# TODO output to csv and/or excel
# TODO user interface