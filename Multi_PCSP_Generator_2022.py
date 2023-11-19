from csv import DictReader
import datetime
from Generate_PCSP_approach import generate_pcsp_approach
from Generate_PCSP_baseline import generate_pcsp_baseline
from common_helpers.read_file import read_data_from_csv
import sys


with open('MDP_pred_2022.csv', newline='') as pred_file:
    data = read_data_from_csv()
    pred_reader = DictReader(pred_file)

    for i, row in enumerate(pred_reader):
        date_obj = datetime.datetime.strptime(row['date'], '%Y-%m-%d')
        end_date = date_obj - datetime.timedelta(days=1)

        generate_pcsp_approach(
            data, end_date.strftime('%Y-%m-%d'), row['P1Name'], row['P2Name'],
            row['P1Hand'], row['P2Hand'], "./pcsp_files_2022/" + f"{i + 1}_APPROACH.pcsp"
        )

        generate_pcsp_baseline(
            data, end_date.strftime('%Y-%m-%d'), row['P1Name'], row['P2Name'], 
            row['P1Hand'], row['P2Hand'], "./pcsp_files_2022/" + f"{i + 1}_BASELINE.pcsp"
        )
