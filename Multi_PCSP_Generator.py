from csv import DictReader
import datetime
from Generate_PCSP import generate_pcsp

with open('MDP_pred.csv', newline='') as pred_file:
    pred_reader = DictReader(pred_file)
    row_num = 1
    for row in pred_reader:
        print(row['date'])
        date_obj = datetime.datetime.strptime(row['date'], '%Y-%m-%d')
        end_date = date_obj - datetime.timedelta(days=1)
        pcsp_filename = f"{row_num}.pcsp"
        generate_pcsp(
            end_date.strftime('%Y-%m-%d'), row['P1Name'], row['P2Name'], row['P1Hand'], row['P2Hand'], "./pcsp_files/" + pcsp_filename
        )
        print(f"Generated {pcsp_filename}")
        row_num += 1
