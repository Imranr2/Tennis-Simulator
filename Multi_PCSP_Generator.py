from csv import DictReader
from datetime import date, timedelta

from Generate_PCSP import generate_pcsp

with open('MDP_pred.csv', newline='') as pred_file:
    pred_reader = DictReader(pred_file)
    row_num = 1
    for row in pred_reader:
        end_date = date.fromisoformat(row['date']) - timedelta(days=1)
        pcsp_filename = f"{row_num}.pcsp"
        generate_pcsp(
            end_date.isoformat(), row['P1Name'], row['P2Name'], row['P1Hand'], row['P2Hand'], pcsp_filename
        )
        print(f"Generated {pcsp_filename}")
        row_num += 1
