import pandas as pd


def read_data_from_csv():
    # obtain shot-by-shot data
    file = './generate_pcsp_helpers/tennisabstract-v2-combined.csv'
    data = pd.read_csv(file, names=['ply1_name', 'ply2_name', 'ply1_hand', 'ply2_hand', 'ply1_points',
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
                                    'prev_prev_shot_fault_type', 'url', 'description'])

    return data
