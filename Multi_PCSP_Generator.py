from csv import DictReader
import datetime
from Generate_PCSP import generate_pcsp
from Generate_PCSP_extra_shots import generate_pcsp_extra_shots
from Generate_PCSP_prev_shots import generate_pcsp_prev_shots
from generate_pcsp_helpers.read_file import read_data_from_csv
import sys

start_line, end_line = int(sys.argv[1]), int(sys.argv[2])
print(start_line, end_line)

with open('MDP_pred.csv', newline='') as pred_file:
    data = read_data_from_csv()
    pred_reader = DictReader(pred_file)

    for i, row in enumerate(pred_reader):
        if start_line <= i + 1 <= end_line:
            date_obj = datetime.datetime.strptime(row['date'], '%Y-%m-%d')
            end_date = date_obj - datetime.timedelta(days=1)
            generate_pcsp(
                data, end_date.strftime('%Y-%m-%d'), row['P1Name'], row['P2Name'],
                row['P1Hand'], row['P2Hand'], "./pcsp_files/" + f"{i + 1}.pcsp"
            )
            generate_pcsp_extra_shots(
                data, end_date.strftime('%Y-%m-%d'), row['P1Name'], row['P2Name'],
                row['P1Hand'], row['P2Hand'], "./pcsp_files/" + f"{i + 1}_EXTRA_SHOTS.pcsp"
            )
            generate_pcsp_prev_shots(
                data, end_date.strftime('%Y-%m-%d'), row['P1Name'], row['P2Name'], 
                row['P1Hand'], row['P2Hand'], "./pcsp_files/" + f"{i + 1}_PREV_SHOTS.pcsp"
            )
            print(f"Generated {i + 1}.pcsp, {i + 1}_EXTRA_SHOTS.pcsp, {i + 1}_PREV_SHOTS.pcsp")
