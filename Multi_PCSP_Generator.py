from csv import DictReader
import datetime
from Generate_PCSP import generate_pcsp
from generate_pcsp_helpers.read_file import read_data_from_csv
import sys

start_line, end_line = int(sys.argv[1]), int(sys.argv[2])
print(start_line, end_line)

with open('MDP_pred.csv', newline='') as pred_file:
    data = read_data_from_csv()
    pred_reader = DictReader(pred_file)

    for i, row in enumerate(pred_reader):
        if start_line <= i + 1 <= end_line:
            print(row['date'])
            date_obj = datetime.datetime.strptime(row['date'], '%Y-%m-%d')
            end_date = date_obj - datetime.timedelta(days=1)
            pcsp_filename = f"{i + 1}.pcsp"
            generate_pcsp(
                data, end_date.strftime('%Y-%m-%d'), row['P1Name'], row['P2Name'], row['P1Hand'], row['P2Hand'], "./pcsp_files/" + pcsp_filename
            )
            print(f"Generated {pcsp_filename}")