import pandas as pd


file = './common_helpers/tennisabstract-v2-combined.csv'

# Replace 'your_file.csv' with the path to your CSV file.
# Set header to None to indicate that the CSV has no headers.
df = pd.read_csv(file, header=None)

# Replace 'header1', 'header2', etc. with your desired header names.
df.columns = ['ply1_name', 'ply2_name', 'ply1_hand', 'ply2_hand', 'ply1_points',
                'ply2_points', 'ply1_games', 'ply2_games', 'ply1_sets', 'ply2_sets', 'date',
                'tournament_name', 'shot_type', 'from_which_court', 'shot', 'direction',
                'to_which_court', 'depth', 'touched_net', 'hit_at_depth', 'approach_shot',
                'shot_outcome', 'fault_type', 'prev_shot_type', 'prev_shot_from_which_court',
                'prev_shot', 'prev_shot_direction', 'prev_shot_to_which_court', 'prev_shot_depth',
                'prev_shot_touched_net', 'prev_shot_hit_at_depth', 'prev_shot_approach_shot',
                'prev_shot_outcome', 'prev_shot_fault_type', 'prev_prev_shot_type',
                'prev_prev_shot_from_which_court', 'prev_prev_shot', 'prev_prev_shot_direction',
                'prev_prev_shot_to_which_court', 'prev_prev_shot_depth',
                'prev_prev_shot_touched_net', 'prev_prev_shot_hit_at_depth',
                'prev_prev_shot_approach_shot', 'prev_prev_shot_outcome',
                'prev_prev_shot_fault_type', 'url', 'description']

# Replace 'column_name' with the actual name of the column you want to analyze.
value_distribution = df.query('approach_shot == 1')['shot'].value_counts()
print(value_distribution)
