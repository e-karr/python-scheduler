import sys
from pathlib import Path

from helpers import create_schedule, validate_schedule_length
from file_handler import Csv, Excel

def main(args):

    # validate args length
    if len(args) < 3:
        raise ValueError('Command-line aruguments must include a file and desired length of schedule')

    file = args[1]

    # validate file type
    if Csv.validate(file):
        file = Csv(file)
    elif Excel.validate(file):
        file = Excel(file)
    else:
        raise ValueError('Must submit CSV or Excel file type')

    # read into dataframe
    teams_dataframe = file.read_file()

    # validate schedule length
    schedule_length = validate_schedule_length(args[2], teams_dataframe)

    # create schedule, returns dataframe
    schedule = create_schedule(teams_dataframe['team_name'].tolist(), schedule_length)

    # merge schedule dataframe into teams dataframe
    final_schedule = teams_dataframe.merge(schedule, how='inner', on='team_name')

    # save schedule to csv
    filepath = Path('./output/schedule.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    final_schedule.to_csv(filepath)

    print(final_schedule)

if __name__ == '__main__':
    main(sys.argv)