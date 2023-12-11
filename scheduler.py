import pandas as pd
import sys
import random
from pathlib import Path

# TODO validate length of command line arguments
# TODO validate first argument is csv file
# TODO allow user to have second argument of number of weeks, validate argument is number, validate that number isn't larger than number of rows in csv - 1

file = sys.argv[1]
schedule_length = int(sys.argv[2])

teams_dataframe = pd.read_csv(file)

# create round robin schedule, keep number of weeks requested, and return dataframe
# TODO figure out how to do this without having to create a round robin schedule first
# TODO if uneven number of teams, give one team a bye each week
# def create_schedule(teams, weeks):
#     first_row = random.sample(teams, len(teams))
#     permutes = random.sample(range(len(teams)), len(teams))
    
#     schedule = [first_row[i:] + first_row[:i] for i in permutes]

#     schedule_df = pd.DataFrame(schedule)
#     schedule_df.columns = ['team_name'] + list(schedule_df.columns[1:])
#     schedule_df = schedule_df.iloc[:, :weeks + 1]
    
#     return schedule_df

def create_schedule(teams, weeks):
    schedule = []
    for team in teams:
        team_schedule = []
        team_schedule.append(team)

        for i in range(weeks):
            opponent = random.choice(teams)
            max_attempts = 10
            attempts = 0
            while (
                opponent in team_schedule or 
                any(opponent == sublist[i + 1] for sublist in schedule)
            ):
                attempts += 1
                if attempts >= max_attempts:
                    create_schedule(teams, weeks)
                opponent = random.choice(teams)

            team_schedule.append(opponent)
    
        schedule.append(team_schedule)

    schedule = pd.DataFrame(schedule)
    schedule.columns = ['team_name'] + list(schedule.columns[1:])

    return schedule

schedule = create_schedule(teams_dataframe["team_name"].tolist(), schedule_length)

final_schedule = teams_dataframe.merge(schedule, how='inner', on='team_name')

# filepath = Path('./output/schedule.csv')
# filepath.parent.mkdir(parents=True, exist_ok=True)

# final_schedule.to_csv(filepath)

print(final_schedule)

# TODO output to csv and/or excel
# TODO user interface